thonimport requests
from bs4 import BeautifulSoup
import json
import os

def fetch_yc_data(url):
    """Fetches the Y Combinator company data."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    return parse_company_data(soup)

def parse_company_data(soup):
    """Parses company data from the HTML page."""
    data = []
    companies = soup.find_all('div', class_='company')
    for company in companies:
        company_data = {
            'company_name': company.find('h3').text.strip(),
            'batch': company.find('span', class_='batch').text.strip(),
            'status': company.find('span', class_='status').text.strip(),
            'location': company.find('span', class_='location').text.strip(),
            'website': company.find('a', class_='website')['href'],
            'company_id': company.get('data-id'),
            'founders': extract_founders(company),
        }
        data.append(company_data)
    return data

def extract_founders(company):
    """Extracts founder information."""
    founders = []
    founder_elements = company.find_all('div', class_='founder')
    for founder in founder_elements:
        founder_data = {
            'name': founder.find('span', class_='name').text.strip(),
            'linkedin': founder.find('a', class_='linkedin')['href'],
            'x': founder.find('a', class_='twitter')['href'],
        }
        founders.append(founder_data)
    return founders

def save_data(data, filename='data.json'):
    """Saves the data into a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    url = 'https://www.ycombinator.com/companies'
    data = fetch_yc_data(url)
    save_data(data)