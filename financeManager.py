import csv
import gspread
import time

# Update Month depending on which CSV we are using
MONTH = 'may'

file = f"chase_{MONTH}.CSV"

transactions = []

def chaseFin(file):
    with open(file, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[1]
            name = row[2]
            amount = float(row[3])
            category = ''
            if "PAYPAL" in name:
                category = 'PAYPAL'
            elif "GRUBHUB" or "DOORDASH" in name:
                category = 'FOOD'
            elif "SUSHI" or "BURRITO" in name:
                category = 'FOOD'
            else:
                category = 'other'
            transaction = (date, name, amount, category)
            transactions.append(transaction)
        return transactions
    
sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = chaseFin(file)

for row in rows:
    wks.insert_row([row[0], row[1], row[3], row[2]], 7)
    time.sleep(2)
