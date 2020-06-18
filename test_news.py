import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://news.ycombinator.com/'
    interests = [
        'snapchat',
        'zoom',
        'covid-19',
        'sql',
    ]

    # Convert url into soup
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    # Extract headlines that include at least one of your interests
    relevant_articles = {
        link.text: link.get('href') for link in soup.findAll('a', {'class': 'storylink'})
        if any([interest in link.text.lower() for interest in interests])
    }

    print(relevant_articles)


if __name__ == '__main__':
    main()
