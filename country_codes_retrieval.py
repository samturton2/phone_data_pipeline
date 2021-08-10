import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
import json

url = "https://www.att.com/support_media/images/pdf/Country_Code_List.pdf"
x = requests.get(url)

parsed = json.loads(x.text)
print(parsed)