from bs4 import BeautifulSoup
import requests

url = "https://www.hackerearth.com/challenges/?filters=competitive%2Chackathon%2Chiring%2Cuniversity"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

ongoing = soup.find('div', {'class': 'ongoing challenge-list'})
challenges = ongoing.find_all('div', {'class': 'challenge-card-modern'})

companies = []
participants = []
types = []
titles = []

for challenge in challenges:
  company = challenge.find('div', {'class': 'company-details ellipsis'})
  companies.append(company.text.strip())

  participant = challenge.find('div', {'class': 'registrations tool-tip align-left'})
  participants.append(participant.text.strip())

  type = challenge.find('div', {'class': 'challenge-type light smaller caps weight-600'})
  types.append(type.text.strip())

  title = challenge.find('span', {'class': 'challenge-list-title challenge-card-wrapper'})
  titles.append(title.text.strip())

for i in range(len(companies)):
  print("Company:", companies[i])
  print("Participants:", participants[i])
  print("Type:", types[i])
  print("Title:", titles[i])
  print()









