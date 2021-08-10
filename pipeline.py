# This file will take the input and write to a new file the formatted country codes
import pandas as pd
import requests

def extract_country_codes():
	x = requests.get('https://www.att.com/support_media/images/pdf/Country_Code_List.pdf')
	with open("./wiki_country_codes.txt", 'w') as f:
		print(x.text)

#phone_code_dict = {'USA':, 'UK', 'FRANCE', 'SPAIN'}
def strip_number():
	df = pd.read_csv("./input.csv")
	for country, num in zip(df['country'], df['phone_number']):
		print (f'{country}  {num}')

if __name__ == "__main__":
	extract_country_codes()
	strip_number()
