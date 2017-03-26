# Run if packages not yet installed. (Usually installed if using Anaconda distribution)
! pip install pandas
! pip install bs4

# Import necessary Libraries
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

# Specify target URL
# Wikipedia has list pages, for an exmaple we will access the list of cryptocurrencies
wiki = "https://en.wikipedia.org/wiki/List_of_cryptocurrencies"

page = urllib.request.urlopen(wiki)

# Parse the desired page
soup = BeautifulSoup(page, "lxml")

print(soup.prettify)

# Navigate to correct tag
all_links = soup.find_all("a")
for link in all_links:
        print(link.get("href"))

all_tables = soup.find_all("table")
table = soup.find('table', { "class" : 'wikitable sortable'})
table

# If page has more than one table, find out the length (columns) of these tables
for i, row in enumerate(soup.findAll("tr")):
    cells = row.findAll("td")
    print(i, len(cells))
    
# Create empty lists of desired columns
release = [ ] # 1
currency = [ ] # 2
symbol = [ ] # 3
founder = [ ] # 4

for row in soup.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 8:
        release.append(cells[0].findAll(text = True))
        currency.append(cells[2].findAll(text = True))
        symbol.append(cells[3].findAll(text = True))
        founder.append(cells[4].findAll(text = True)) 

print(release)
print(currency)
print(symbol)
print(founder)

# Create a pandas dataframe of the data
df = pd.DataFrame({'Release': release, 'Currency': currency, 'Symbol': symbol, 'Founder': founder})

# Display the first 5 rows
df[:5]

# The data frame has textual artifacts such as \n. So we need to remove that.
clean_df = df.replace('\n', '')

# The data frame still has textual artifacts such as reference numbers enclosed in square brackets.
clean_df['Release'] = clean_df['Release'].str.get(0)
clean_df['Currency'] = clean_df['Currency'].str.get(0)
clean_df['Symbol'] = clean_df['Symbol'].str.get(0)
clean_df['Founder'] = clean_df['Founder'].str.get(0)        
clean_df

clean_df.set_value(3, "Founder", "[Baldur Odinsson (pseudonym)]")
clean_df.set_value(8, "Founder", "Evan Dufffield & Kyle Hagan")
clean_df.set_value(24, "Founder", "Chris Larsen & Jed McCaleb")
clean_df.to_csv("clean_df.csv")