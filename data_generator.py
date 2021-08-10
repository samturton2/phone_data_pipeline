import random as r
import csv

countries = ['USA', 'UK', 'FRANCE', 'SPAIN']
headers = ['country', 'phone_number']

def populate_csv():

	# Open input csv file and write over it
	with open('/input.csv', 'w') as f:
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
			ph_no.append(str(r.randint(6, 9)))
			for i in range(1, 10):
			    ph_no.append(str(r.randint(0, 9)))
			# write to temp data 
			temp_data.append(ph_no)

			writer.writerow(temp_data)



if __name__ == '__main__':
	populate_csv()