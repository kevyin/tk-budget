#!/usr/bin/env python3

"""
Helper script to guess transaction accounts
"""

from beancount.core import data

guess_dict = {

    'Westpacchoice':'Assets:Westpac:Choice',
    'Westpacmain':'Assets:Westpac:OneMain',
    'Westpac Securities':'Assets:Westpac:Securities',


    'DEPOSIT-SALARY University of Te':'Income:UTS',
    'Deposit-Salary Gimr':'Income:Garvan',
    'SIDNEY CACHUELA':'Income:SidneyCachuela',
    'Montreal Zhang':'Income:MontrealZhang',
    'Min Huang':'Income:MinHuang',
    'Miranda Nsw':'Income:MinHuang',
    'Deposit Hurstville':'Income:MinHuang',
    'Atm Deposit Handybank Potts Point 10521062 31/07/17':'Income:MinHuang',
    'Caringbah Nsw':'Income:MinHuang',
    'DANQING YIN':'Income:DanqingYin',
    'Angela Yin':'Income:DanqingYin',
    'Niantao De':'Income:NiantaoDeng',
    'DEPOSIT Kevin Ying':'Income:KevinYing',
    'Car Spot':'Income:Wolli:CarRental',
    'Phil':'Income:PhillipLi',
    'GERALDINE SUWANG':'Income:Geraldine',

    'PYMT Kevin Ying':'Assets:Macquarie:Transaction',
    'Sweep' : 'Assets:Ubank:Sweep',
    'inward credit' : 'Assets:Westpac:OneMain',
    'deposit li li' : 'Assets:Lili:Checking',
    'Westpac One' : 'Assets:Westpac:OneMain',
    '738014' : 'Assets:Westpac:OneMain',
    'TFR Westpac Cho' : 'Assets:Westpac:Choice',

    'TFR Fixed Rate' : 'Liabilities:Mortgage:Fixed',

    'Interest for ' : 'Income:Ubank:Interest',
    'PLEASE NOTE INTEREST RATE EFFECTIVE FROM ' : 'Income:Ubank:Interest',
    'Regular Transfer to 738014 Move Out' : 'Income:Ubank:Interest',

    'BEEM IT' : 'Assets:BeemIT',

    # Macquarie catergories
    "Financial Cash Withdrawals" : "Expenses:Cash",
    "Financial Transfers FROM KEVIN YING" : "Assets:Kevin:Checking",
    "Food & Drink Alcohol & Bars" : "Expenses:Food:Drinks",
    "Food & Drink Groceries" : "Expenses:Food:Groceries",
    "Food & Drink Restaurants" : "Expenses:Food:Restaurant",
    "Home Furnishings" : "Expenses:Home:Furnishings",
    "Home Other Home Expenses" : "Expenses:Home:Other",
    "Home Rent" : "Expenses:Rhodes:Rent",
    "Home Supplies" : "Expenses:Home:Other",
    "Leisure Movies" : "Expenses:Leisure:Movies",
    "Transportation Fuel" : "Expenses:Transport:Fuel",
    "Transportation Parking & Tolls" : "Expenses:Transport:ParkingToll",
    "Travel Public Transit" : "Expenses:Leisure:Travel:Transit",
    "Travel Travel Entertainment" : "Expenses:Leisure:Travel:Entertainment",
    "Utilities Electricity, Gas" : "Expenses:Rhodes:Utilities:ElectricityGas",
    "Utilities Internet" : "Expenses:Rhodes:Utilities:Internet",



    ## Expenses 
    # living food
    'Yebisu Yakitori':'Expenses:Food:Restaurant',
    'CZL Investments':'Expenses:Food:Restaurant',
    'GYG Rhodes':'Expenses:Food:Restaurant',
    'Mogu Mogu':'Expenses:Food:Restaurant',
    'Sushi World':'Expenses:Food:Restaurant',
    'Cafe Bar':'Expenses:Food:Restaurant',
    'Ocean Palace':'Expenses:Food:Restaurant',
    'Menya':'Expenses:Food:Restaurant',
    'Tong Li':'Expenses:Food:Groceries',
    'Killiney Kopitiam':'Expenses:Food:Restaurant',
    'Spice Alley':'Expenses:Food:Restaurant',
    'Alex Lee':'Expenses:Food:Restaurant',
    'Mai Viet':'Expenses:Food:Restaurant',
    'Beauty Table':'Expenses:Food:Restaurant',
    'Ww Metro':'Expenses:Food:Restaurant',
    'Guzman Y Gomez':'Expenses:Food:Restaurant',
    'Cafe 10':'Expenses:Food:Restaurant',
    'Aldi':'Expenses:Food:Groceries',
    'Inshine':'Expenses:Food:Restaurant',
    'VIET STREET':'Expenses:Food:Restaurant',
    'SpiceAlley':'Expenses:Food:Restaurant',
    'Bombora Seafood':'Expenses:Food:Restaurant',

    'Coco Fresh Tea':'Expenses:Food:MilkTea:Coco',
    'McDonalds': 'Expenses:Food:Lunch',
    'pork': 'Expenses:Food:Lunch',
    'coles':'Expenses:Food:Groceries',
    'woolworths':'Expenses:Food:Groceries',
    'orange supermarket': 'Expenses:Food:Groceries',
    'Chai Time':'Expenses:Food:MilkTea:ChaiTime',
    'flexi cash' : 'Expenses:Cash',
    'Withdrawal at Cba Atm':'Expenses:Cash',
    'Withdrawal at Nab Atm':'Expenses:Cash',
    'Withdrawal at Bblsatm':'Expenses:Cash',
    'Atm Operator Fee':'Expenses:ATMFees',
    'Overdrawn Fee':'Expenses:Westpac:Fees:Overdrawn',
    'DAINTY SICHUAN NOODL':'Expenses:Food:Restaurant',
    'SMOKKIM':'Expenses:Food:Restaurant',
    'RHODES WATERFRONT':'Expenses:Food:Restaurant',
    'AZA AZA':'Expenses:Food:Restaurant',
    'DOUBLE BRIDGE PTY':'Expenses:Food:Restaurant',
    'AYADA THAI':'Expenses:Food:Restaurant',
    'SHNGHI FRD DMPLNG PL':'Expenses:Food:Restaurant',
    'SQ *MARRICKVILLE PORK':'Expenses:Food:Lunch',
    'Tracy Loi':'Expenses:Food:Lunch',
    'CRYSTAL SEAFOOD REST':'Expenses:Food:Restaurant',
    'BURWOOD BROTHERS PTY':'Expenses:Food:Restaurant',
    'Dumplings':'Expenses:Food:Restaurant',
    'Ruohai Pty Ltd':'Expenses:Food:Restaurant',
    'St George Rowing Clu':'Expenses:Food:Restaurant',
    'Chimney Cake':'Expenses:Food:Restaurant',
    'Piccadilly Operations':'Expenses:Food:Restaurant',
    'Kfc Sydney':'Expenses:Food:Restaurant',
    'Purchase Kfc':'Expenses:Food:Restaurant',
    'Phoenix Rhodes':'Expenses:Food:Restaurant',
    'Top Juice':'Expenses:Food:Restaurant',
    'Ramen Zundo':'Expenses:Food:Restaurant',
    'Hungry Jacks':'Expenses:Food:Restaurant',
    'Korean Bbq':'Expenses:Food:Restaurant',
    'CHAO MA PTY':'Expenses:Food:Restaurant',
    'Cooh Alexan':'Expenses:Food:Restaurant',
    'Deposit Mr Ke Li':'Expenses:Food:Restaurant',
    'Sushi Hub':'Expenses:Food:Lunch',
    'Withdrawal at Nab Atm Haymarket    2o00 094196 060418':'Expenses:Food:Lunch',
    'Coco Cubano':'Expenses:Food:Restaurant',
    'Llyz Pty Ltd':'Expenses:Food:Restaurant',
    'Palm Beach Fish':'Expenses:Food:Restaurant',
    'Eskippan':'Expenses:Food:Restaurant',
    'Ippudo':'Expenses:Food:Restaurant',
    'Dominos':'Expenses:Food:Restaurant',
    'Huang Traditional':'Expenses:Leisure:Restaurant',
    'WITHDRAWAL MOBILE 1090481 PYMT Chris on John Bday':'Expenses:Leisure:Restaurant',
    'POPUPPICNIC':'Expenses:Leisure:Restaurant',

    'Vaya':'Expenses:Utilities:Mobile:Vaya',
    'Yomojo':'Expenses:Utilities:Mobile:Yomojo',
    'Exetel':'Expenses:Utilities:Internet:Exetel',
    'WITHDRAWAL ONLINE 9021139 BPAY DEFT RENT Holding Dep':'Expenses:Rhodes:Rent',

    # mortgages
    '165849490' : 'Expenses:Mortgage:FixedInterest',
    '165849482': 'Expenses:Mortgage:VariableInterest',

    # Insurance
    'Gmhba 314348' : 'Expenses:Insurance:Health:Gmhba',
    'Unisuper' : 'Expenses:Insurance:Super',

    # Wolli
    'Water 52463171984':'Expenses:Wolli:Utilities:Water',
    'Water 52463171893':'Expenses:Wolli:Utilities:Water',
    'Bpay Sydney Wat':'Expenses:Wolli:Utilities:Water',
    'Deft Pay':'Expenses:Wolli:Utilities:Strata',
    'BPAY Whelan Bon':'Expenses:Wolli:Utilities:Strata',
    'Bpay Rockdale':'Expenses:Wolli:Utilities:Council',

    # Rhodes
    'City of Canada':'Expenses:Rhodes:Utilities:Council',

    'Bankcorp Direct Dr183359831':'Expenses:Rhodes:Mortgage:Payment',
    'Opal':'Expenses:Transport:Opal',
    'Uber':'Expenses:Transport:Uber',

    # Utilities
    'Agl Sales P/L' : 'Expenses:Utilities:Electricity',
    'Agl Sales Pty Lt 390008412297' : 'Expenses:Utilities:Electricity',
    'Agl Sales Pty Lt 180007721447' : 'Expenses:Utilities:Gas',
    'Agl Sales Pty Lt 180007458757' : 'Expenses:Utilities:Gas',
    'Agl Retail' : 'Expenses:Utilities:Gas',
    'Sydney Water':'Expenses:Rhodes:Utilities:Water',
    'EnergyAustralia 792577856736' : 'Expenses:Utilities:Electricity',
    'EnergyAustralia 383387948102' : 'Expenses:Utilities:Gas',
    'EnergyAustralia 792004199434' : 'Expenses:Utilities:Electricity',

    # recurring
    'Economist Subscription':'Expenses:Leisure:Economist',
    'Amznprimeau':'Expenses:Leisure:AmazonPrime',
    'Choice Marrickville':'Expenses:Leisure:Choice',

    # non necessities

    'Paypal':'Expenses:Paypal',
    'Hoyts Sydney':'Expenses:Leisure:Movies',
    'Decathlon':'Expenses:Shopping:Equipment',
    'Jb Hi Fi':'Expenses:Shopping:Electronics',
    'Jaycar':'Expenses:Shopping:Electronics',
    'Uniqlo':'Expenses:Shopping:Clothing:Uniqlo',
    'Myer':'Expenses:Shopping:Misc:Myer',
    'Rebel':'Expenses:Shopping:Equipment',
    'Ikea':'Expenses:IKEA',
    'PLINE':'Expenses:HealthAndBeauty',
    'Chemist Warehouse':'Expenses:HealthAndBeauty',
    'EVENT BURWOOD':'Expenses:Leisure:Movies',
    'V1153 06/06 THE AMBASSADOR CARD':'Expenses:Leisure:Movies',
    'BANNER SAGA':'Expenses:Leisure:Games',
    'Eb Games':'Expenses:Leisure:Games',
    '99 BIKES':'Expenses:Leisure:Equipment',
    'HARAJYUKU TOKYO':'Expenses:Leisure:Games',
    'Bing Lee':'Expenses:Shopping:Electronics',
    'Amazon Mktplc':'Expenses:Shopping:Amazon',
    'Audible':'Expenses:Shopping:Audible',

    # Travel
    'BLUE MOUNTAIN':'Expenses:Leisure:Travel',
    'Fast Foto':'Expenses:Leisure:Travel',
    'Rays Outdoors':'Expenses:Leisure:Equipment',
    'Anaconda':'Expenses:Leisure:Equipment',
    'Travel':'Expenses:Leisure:Travel',
    'Flights':'Expenses:Leisure:Travel',
    'Airbnb':'Expenses:Leisure:Travel',
    'TRIP.COM':'Expenses:Leisure:Travel',
    'Heinemann':'Expenses:Leisure:Travel',
    'TOKYODISNEYRESORT':'Expenses:Leisure:Travel',
    'HOKKAIDO':'Expenses:Leisure:Travel',
    'HANEDAKUUKORIYOKIYAKUT':'Expenses:Leisure:Travel',

    # Business
    'Amazon Web Ser':'Expenses:Business:AWS',
    'Salary Fowkner':'Income:Wolli:Rent',
    'Fowkner':'Expenses:Wolli:Maintenance',
    'Bunnings':'Expenses:Wolli:Maintenance',
    'Sunlite':'Expenses:Wolli:Maintenance',
    'Daiso':'Expenses:Wolli:Maintenance',
    'Debit Card Purchase Officeworks 0251 Sydney       Aus':'Expenses:Wolli:Maintenance',
    'PROMETHEASE':'Expenses:Business:Misc',

    # Learning
    'Tun Mau Li':'Expenses:Business:Driving',
    'Rms Internet/Ivr':'Expenses:Business:Driving',

    # Assets
    'Securiti B Gxy 26360758-00':'Assets:Securities:GXY',

    # Rhodes

    'PYMT Kevin and Household':'Expenses:Rhodes:Household',
    'PYMT Kevin and':'Expenses:Rhodes:Household',


    # commbank
    'xx7465 NetBank':'Assets:Commbank:Offset217k',
    'LN REPAY 782749883':'Expenses:Mortgage:VariableInterest',
    'LN REPAY 782749832':'Expenses:Mortgage:FixedInterest',
    'LN REPAY 782749904':'Expenses:Mortgage:VariableInterest',
    'LN REPAY ':'Expenses:Mortgage:FixedInterest',
    "Transfer From KEVIN YING CREDIT TO ACCOUNT":'Assets:Westpac:OneMain',
    "Transfer From KEVIN YING transfer":'Assets:Westpac:OneMain',
    "to other Bank NetBank Household":'Assets:Macquarie:Transaction',
    "Transfer to xx5860":'Assets:Commbank:Offset63k',
    "Transfer from xx5860":'Assets:Commbank:Offset63k',
    "Transfer to xx8781 NetBank":'Assets:Commbank:CDIA',

}

guess_dict_wolli = {
    "Interest charged":'Expenses:Wolli:MortgageInterest',
    "Fee for attending":'Expenses:Wolli:Fees',
    "Administrative fee for":'Expenses:Wolli:Fees',
}

def guess_post(trans_desc, guess_dict_type=None):
    trans_desc = trans_desc.lower()
    second_post = None
    if guess_dict_type == 'wolli':
        for key in guess_dict_wolli.keys():
            if key.lower() in trans_desc:
                second_post = data.Posting(guess_dict_wolli[key], None,
                    None, None, None, None)
                break
    else:
        for key in guess_dict.keys():
            if key.lower() in trans_desc:
                second_post = data.Posting(guess_dict[key], None,
                    None, None, None, None)
                break
    if second_post is None:
        second_post = data.Posting('Expenses:Unknown', None,
                None, None, None, None)


    return second_post
