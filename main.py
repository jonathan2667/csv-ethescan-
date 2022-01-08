from etherscan import Etherscan
import csv
import os

holders = {}

with open('export-tokenholders-for-contract-0x476c5E26a75bd202a9683ffD34359C0CC15be0fF.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        try:
            holders[line[0]] = int(float(line[1]))
        except ValueError:
            do_nothing = 1

    sort_holders = sorted(holders.items(), key = lambda x:x[1], reverse= True)


with open('SerumHolders.csv','w', newline="") as new_file:
    csv_writer = csv.writer(new_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for i in range(99):
        csv_writer.writerow([str(sort_holders[i][0])])


serum = "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff"

eth = Etherscan(YOUR_API_KEY)

with open('SerumHolders.csv')  as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(eth.get_acc_balance_by_token_and_contract_address(serum, line[0]))

