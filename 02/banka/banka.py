# Nasimulujte bankovní systém
#
# V adresáři jsou soubory pojmenované číslem účtu obsahující zůstatek účtu
# Implementujte skript banka.py, který bude ovládán parametry:
#
# Částka se bude čerpat z účtu 111 pomocí --from 111
# Částka se bude připisovat na účet 222 pomocí --to 222
# Převod částky 1000 se určí parametrem --amount 1000
#
# Snažte se řešit různé chyby:
# * účet neexistuje
# * zůstatek by šel do záporu
#
# Příklad použití:
#
#   python banka.py --from 111 --to 222 --amount 1000
#
# V praxi se píší skripty, kde nezáleží na pořadí pojmenovaných parametrů, tj.
# ideální je, když funguje libovolné pořadí parametrů při spuštění:
#
#   python banka.py --from 111 --amount 1000 --to 222
#   python banka.py --amount 1000 --from 111 --to 222
#
# Pro tento pokročilý způsob je však třeba použít pokročilou knihovnu pro práci
# s parametry příkazové řádky, jako např. argparse nebo click.

import argparse

def amount_in_account(account_num):
    try:
        with open(account_num) as file:
            return int(file.read())
    except FileNotFoundError:
        print("The sender's account doesn't exist.")
        exit()

    

# Create parser
parser = argparse.ArgumentParser(description="bank transfer")

# Adding arguments
parser.add_argument('--from', type=str, help="senders_account", required=True, dest = "from_account")
parser.add_argument('--to', type=str, help="income_account", required=True)
parser.add_argument('--amount', type=int, help="amount", required=True)


args = parser.parse_args()


# Finding the amounts in the respective accounts
senders_amount = amount_in_account(args.from_account)
recipient_amount = amount_in_account(args.to)


# Transaction
if senders_amount >= args.amount:
    senders_amount = senders_amount - args.amount
    recipient_amount = recipient_amount + args.amount
    
    # Write the new amounts into the files
    with open(args.from_account, mode='w') as file:
        print(senders_amount, file=file)
        
    with open(args.to, mode='w') as file:
        print(recipient_amount, file=file)  
else:
    print('There is not enough money in the account for this transaction')