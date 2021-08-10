import random as r
import csv

countries = ['USA', 'UK', 'FRANCE', 'SPAIN']
headers = ['country', 'phone_number']

def populate_csv():

	with open('/input.csv', 'w') as f:
		writer = csv.writer(f)

		writer.writerow(headers)

		for i in range(1000):
			temp_data = []
			temp_data.append(countries[r.randint(0,2)])
			
			ph_no = []
			ph_no.append(r.randint(6, 9))
			for i in range(1, 10):
			    ph_no.append(r.randint(0, 9))

			temp_data.append("".join(ph_no))




