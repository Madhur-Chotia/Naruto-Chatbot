import requests
from bs4 import BeautifulSoup

# Function to extract text from a webpage
def extract_text_from_webpage(url):
    # Making a GET request to the URL
    response = requests.get(url)

    # Checking if request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting text from the parsed HTML
        text = soup.get_text()

        return text
    else:
        # Printing an error message if the request was not successful
        print(f"Error: Unable to fetch webpage. Status code: {response.status_code}")
        return None
    

#creating a func to split one string into two as ans to former question and next questions are in one string
def split_strings_at_last_period(strings):
    result = []
    for text in strings:
        index_last_period = text.rfind('.')
        first_part = text[:index_last_period + 1].strip()
        second_part = text[index_last_period + 1:].strip()
        result.extend([first_part, second_part])
    return result

