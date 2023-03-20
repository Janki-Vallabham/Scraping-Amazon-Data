import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', {'class': 's-result-item'})
for product in products:
    # Extract product data
    product_name = product.find('h2').text.strip()
    product_url = product.find('a')['href']
    if product.find('span', {'class': 'a-price-whole'}) is not None:
        product_price = product.find('span', {'class': 'a-price-whole'}).text.strip()
    else:
        product_price = 'N/A'

    rating = product.find('span', {'class': 'a-icon-alt'}).text.strip().split()[0]
    reviews = product.find('span', {'class': 'a-size-base'}).text.strip()
    

    # Store data in a dictionary or data structure of your choice
    data = {
        'Product Name': product_name,
        'Product URL': product_url,
        'Product Price': product_price,
        'Rating': rating,
        'Number of Reviews': reviews
    }


import csv
import requests
from bs4 import BeautifulSoup

# Initialize an empty list to store the data
data_list = []

for i in range(1, 21):
    url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&page={i}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'class': 's-result-item'})
        for product in products:
            # Extract product data
            try:
                product_name = product.find('h2').text.strip()
                product_url = product.find('a')['href']
                product_price = product.find('span', {'class': 'a-price-whole'}).text.strip()
                rating = product.find('span', {'class': 'a-icon-alt'}).text.strip().split()[0]
                reviews = product.find('span', {'class': 'a-size-base'}).text.strip()
            except Exception as e:
                # Skip over any products that do not have the expected HTML structure
                print(f"Error extracting data from product: {str(e)}")
                continue

            # Store data in a dictionary and append it to the list
            data = {
                'Product Name': product_name,
                'Product URL': product_url,
                'Product Price': product_price,
                'Rating': rating,
                'Number of Reviews': reviews
            }
            data_list.append(data)

        # Write data to a CSV file
        with open('amazon_bags.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data_list[0].keys())
            writer.writeheader()
            writer.writerows(data_list)

    except Exception as e:
        print(f"Error scraping page {i}: {str(e)}")
        # Print out the HTML content of the webpage that caused an error
        print(response.content)
