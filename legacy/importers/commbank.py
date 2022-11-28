
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

class CommbankImporter(importer.ImporterProtocol):
    def __init__(self, account, match, guess_dict=None):
        self.account = account
        self.match = match
        self.guess_dict = guess_dict

    def identify(self, f):
        match = re.match(self.match, os.path.basename(f.name))
        return match

    def file_account(self, f):
        return self.account

    def extract(self, f):
        entries = []

        with open(f.name) as f:
            fields = ['Date','Amount','Detail','Balance']
            for index, row in enumerate(csv.DictReader(f, fieldnames=fields)):
                trans_date = parse(row['Date'], dayfirst=True, yearfirst=False).date()

                #rstrip removes trailing new line characters
                trans_desc = row['Detail'].strip()

                trans_amt = row['Amount']

                meta = data.new_metadata(f.name, index)

                second_post = guess_post(trans_desc, self.guess_dict)

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
