import random as r
import csv
import pandas as pd

countries = ['USA', 'UK', 'FRANCE', 'SPAIN']
headers = ['country', 'phone_number']

def randomise_num(ph_no):
	if r.randint(0,13)%6 == 0:
		# Get in format XXXXX XXX XXX
		return f"0{ph_no[0:4]} {ph_no[4:7]} {ph_no[7:]}"
	elif r.randint(0,15)%5 == 0:
		# Get in format (XXXX) XXX XXX
		return f"({ph_no[0:4]}) {ph_no[4:7]} {ph_no[7:]}"
	elif r.randint(1,5)%3 == 0:
		# Get in format XXXX-XXX-XXX
		return f"{ph_no[0:4]}-{ph_no[4:7]}-{ph_no[7:]}"
	else:
		return ph_no





def populate_csv():

	# Open input csv file and write over it
	with open('./input.csv', 'w') as f:
		writer = csv.writer(f)

		# insert headers
		writer.writerow(headers)

		# Insert 1000 rows of data
		for i in range(1000):
			
			temp_data = []
			# Get random country from list
			temp_data.append(countries[r.randint(0,2)])
			
			# create phone number string
			ph_no = ''
			ph_no += str(r.randint(6, 9))
			for i in range(1, 10):
			    ph_no += str(r.randint(0, 9))

			# Randomise data
			ph_no = randomise_num(ph_no)

			# write to temp data 
			temp_data.append(ph_no)

			writer.writerow(temp_data)

def list_data():
	num = int(input("how many rows? : "))
	phone_numbers = pd.read_csv('./input.csv')
	print(phone_numbers.head(num))

if __name__ == '__main__':
	populate_csv()
	list_data()