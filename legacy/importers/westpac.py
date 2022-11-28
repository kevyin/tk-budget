
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

ACCOUNTS = {
    '732055700278' : 'Assets:Westpac:Choice',
    '732055738014' : 'Assets:Westpac:OneMain',

}

class WestpacImporter(importer.ImporterProtocol):
    def __init__(self, account, match):
        # self.account = account
        self.match = match

    def identify(self, f):
        match = re.match(self.match, os.path.basename(f.name))
        return match

    def get_account(self, acc_num):
        return ACCOUNTS[acc_num]

    def extract(self, f):
        entries = []

        with open(f.name) as f:
            for index, row in enumerate(csv.DictReader(f)):
                trans_date = parse(row['Date'], yearfirst=True).date()

                #rstrip removes trailing new line characters
                trans_desc = titlecase(row['Narrative'].rstrip())

                if bool(row['Debit Amount']):
                    trans_amt = "-" + row['Debit Amount']
                else:
                    trans_amt = row['Credit Amount']


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
                    data.Posting(self.get_account(row['Bank Account']),
                                 amount.Amount(D(trans_amt),
                        'AUD'), None, None, None, None)
                )

                if second_post is not None:
                    txn.postings.append(second_post)

                entries.append(txn)

        return entries
