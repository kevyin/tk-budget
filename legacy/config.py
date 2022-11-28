import os, sys

# beancount doesn't run from this directory
sys.path.append(os.path.dirname(__file__))

# importers located in the importers directory
from importers import westpac, macquarie, commbank

CONFIG = [
    # ubank.UbankImporter('Assets:Ubank:Checking', '0000'),
    #ubank.UbankImporter(),
    #airbnb.AirbnbImporter(),
    westpac.WestpacImporter('Assets:Westpac:Choice', 'westpac_choice_.*csv'),
    westpac.WestpacImporter('Assets:Westpac:OneMain', 'westpac_onemain_.*csv'),
    commbank.CommbankImporter('Assets:Commbank:Loan', 'commbank_loan.*csv','wolli'),
    commbank.CommbankImporter('Assets:Commbank:SmartAccess', 'commbank_smart.*csv', 'wolli'),
    #westpac.WestpacImporter('', 'westpac_.*csv'),
    #macquarie.MacquarieImporter('Assets:Macquarie:Transaction', 'macquarie_.*csv'),
    #commbank.CommbankImporter('Assets:Commbank:Offset217k', 'commbank_217k.*csv'),
    #commbank.CommbankImporter('Assets:Commbank:Offset63k', 'commbank_63k.*csv'),
    # chase.ChaseCCImporter('Liabilities:CC:Chase:Reserve', '0000'),
    # chase.ChaseBankImporter('Assets:Chase:Checking', '0000'),
    # schwab.SchwabBankImporter('Assets:Schwab:Checking', '8000'),
]
