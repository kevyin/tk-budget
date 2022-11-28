
from beancount.core.number import D
from beancount.ingest import importer
from beancount.core import amount
from beancount.core import flags
from beancount.core import data

from dateutil.parser import parse

from titlecase import titlecase
from prepost import guess_post

import csv
import os
import re

class MacquarieImporter(importer.ImporterProtocol):
    def __init__(self, account, match):
        self.account = account
        self.match = match

    def identify(self, f):
        match = re.match(self.match, os.path.basename(f.name))
        return match

    def file_account(self, f):
        return self.account

    def extract(self, f):
        entries = []

        with open(f.name) as f:
            for index, row in enumerate(csv.DictReader(f)):
                trans_date = parse(row['Transaction Date'], yearfirst=False).date()

                #rstrip removes trailing new line characters
                trans_desc = titlecase(row['Category'].strip() + ' ' + row['Subcategory'] + ' ' + row['Details'].strip())

                if bool(row['Debit']):
                    trans_amt = "-" + row['Debit']
                else:
                    trans_amt = row['Credit']


                meta = data.new_metadata(f.name, index)

                second_post = guess_post(trans_desc)

                txn = data.Transaction(
                    meta=meta,
                    date=trans_date,
                    flag=flags.FLAG_OKAY,
                    payee=trans_desc,
                    narration="",
                    tags=set(),
                    links=set(),
                    postings=[]
                )

                txn.postings.append(
                    data.Posting(self.account, amount.Amount(D(trans_amt),
                        'AUD'), None, None, None, None)
                )

                if second_post is not None:
                    txn.postings.append(second_post)

                entries.append(txn)

        return entries
