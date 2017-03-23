# Run if packages not yet installed. (Usually installed if using Anaconda distribution)
! pip install lxml
! pip install requests
! pip install pandas

# Import necessary libraries
from lxml import html
import requests
from pandas import *

# The website below is a very simple webpage that includes only a div and a span,
# the former with a title "buyer-name" 
# the latter with a class "item-price"
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

# Obtain the data and save to variables
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')

# Print variables
print('Buyers: ', buyers)
print('Prices: ', prices)

# Tabulate and view the data
df = DataFrame({'Buyers': buyers, 'Prices': prices})
df