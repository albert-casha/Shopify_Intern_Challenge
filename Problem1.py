import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

filename = '2019_Winter_Data_Science_Intern_Challenge_Data_Set.csv'

#Define dictionaries and lists to store the data

amount_per_shop = {} # Dictionary to record the total value of transactions per shop
amount_per_user = {} # Dictionary to record the total value of transactions per user
orders_per_shop = {} # Dictionary to record the number of orders placed at each shop
orders_per_user = {} # Dictionary to record the number of orders placed by each user
first_trans = {}     # Dictionary to record the first transaction placed by each user
repeat_trans = []    # List of any repeat transactions by any user

with open(filename) as csvfile:
	csv_reader = csv.DictReader(csvfile, delimiter=',')
	for row in csv_reader:
		#Filter out corrupted/not applicable data
		if float(row['order_amount']) > 10000:
			continue

	        #Record the value of transactions and number of orders as a function of the shop
		if(row['shop_id'] in amount_per_shop):
			amount_per_shop[row['shop_id']] += float(row['order_amount'])
			orders_per_shop[row['shop_id']] += 1
		else:
	            amount_per_shop[row['shop_id']] = float(row['order_amount'])
        	    orders_per_shop[row['shop_id']] = 1

	        #Record the value of transactions and number of orders as a function of the user
        	if(row['user_id'] in amount_per_user):
	            amount_per_user[row['user_id']] += float(row['order_amount'])
        	    orders_per_user[row['user_id']] += 1
	        else:
        	    amount_per_user[row['user_id']] = float(row['order_amount'])
	            orders_per_user[row['user_id']] = 1

		#Parse date and time from the datetime string
		date = row['created_at'].split(' ')[0].split('-')
		time = row['created_at'].split(' ')[1].split(':')
		datetime = dt.datetime(int(date[0]), int(date[1]), int(date[2]),
			    	int( time[0]), int(time[1]), int(time[2]))
	
        	# As the transactions are not in time order, check if the timestamp on the transaction
	        # occurs before the previously recorded one.
        	# If so, replace the first transaction with the current one
		if row['user_id'] in first_trans.keys():
			if first_trans[row['user_id']][1] > datetime:
				repeat_trans.append(first_trans[row['user_id']][0])
				first_trans[row['user_id']] = [ float(row['order_amount']), datetime ]
	        	else:
				# Append repeat transactions to the repeat list		
				repeat_trans.append(float(row['order_amount']))
		else:
  		        # If this is the first transaction by the user in the dataset, add the order value and timestamp
  			first_trans[row['user_id']] = [ float(row['order_amount']), datetime ]

#Calculate the AOV for first time customers
sum_of_first_AOV = 0
for key in first_trans.keys():
	sum_of_first_AOV += first_trans[key][0]
first_AOV = sum_of_first_AOV/len(first_trans.keys())
print "first_AOV: ", first_AOV

# Calculate AOV for repeat customers
repeat_AOV = sum(repeat_trans)/len(repeat_trans)
print "repeat_AOV: ", repeat_AOV

# Calculate the AOV for the entire dataset
AOV = (sum_of_first_AOV + sum(repeat_trans))/(len(first_trans.keys()) + len(repeat_trans))
print "AOV: ", AOV

# Calculate the AOV as a function of store/customer and produce a histogram
def AOV_hist(order_amounts, number_of_orders, title, nbins):
        
	AOV = []
        for key in order_amounts.keys():
	        AOV.append(order_amounts[key]/number_of_orders[key])

	print title, ' Average AOV: ', sum(AOV)/len(AOV)	
	plt.figure()
	plt.hist(AOV, bins=nbins)
	plt.xlabel('Average Order Value')
	plt.ylabel('Entries')
	plt.title(title)
	plt.savefig(title + '.png')

AOV_hist(amount_per_shop, orders_per_shop, 'AOV per Shop',  np.linspace(100,700,13))
AOV_hist(amount_per_user, orders_per_user, 'AOV per Customer', 16)
