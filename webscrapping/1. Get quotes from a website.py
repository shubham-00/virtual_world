from bs4 import BeautifulSoup
import requests

response = requests.get('http://quotes.toscrape.com/')
# print(response)
# print(response.__dir__())
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

# quote = soup.find('span', {'class': 'text'})  # Find span element having quote class
# print(quote)
# print(quote.text)

# quotes = soup.find_all('span', {'class': 'text'})
# print(quotes)
# print(list(quotes)[0])
# print(list(quotes)[1])
# print(list(quotes)[0].text)
# print(list(quotes)[1].text)
# for quote in quotes:
  # print(quote.text)

'''Quotes on the page'''
# quotes_and_authors = soup.find_all('div', {'class': 'quote'})
# for quote_and_author in quotes_and_authors:
#   quote = quote_and_author.find('span', {'class': 'text'})
#   author = quote_and_author.find('small', {'class': 'author'})  # No need to provide class...
#   print("Quote:", quote.text)
#   print("Author:", author.text)
#  print()
