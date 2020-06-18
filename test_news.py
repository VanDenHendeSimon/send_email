import requests
from bs4 import BeautifulSoup
from models.Email import Email
from datetime import datetime


def get_current_day():
    return datetime.strftime(datetime.now(), '%D')


def get_relevant_articles(interests):
    # Convert url into soup
    html = requests.get('https://news.ycombinator.com/').text
    soup = BeautifulSoup(html, 'html.parser')

    # Extract headlines that include at least one of your interests
    relevant_articles = {
        link.text: {
            'link': link.get('href'),
            'interests': [
                interest for interest in interests
                if interest.lower() in link.text.lower()
            ]
        } for link in soup.findAll('a', {'class': 'storylink'})
        if any([interest.lower() in link.text.lower() for interest in interests])
    }

    return relevant_articles


def construct_email(articles):
    html = '<h4 style="text-decoration:underline;">%d new articles today:</h4>' % len(articles.keys())
    html += '<ol>'

    for article in articles.keys():
        html += """
        <li style="margin-bottom:12px;list-style-type:decimal;">
            <a href="%s" style="text-decoration:none;color:currentColor;">%s</a>
        </li>
        """ % (
            articles[article]['link'], article
        )

    html += '</ol>'

    return html


def main():
    interests = [
        'Snapchat',
        'Zoom',
        'Covid-19',
        'SQL',
        'Apple',
        'Tesla',
        'TSLA',
        'Docker',
        'AWS',
    ]

    articles = get_relevant_articles(interests)
    html = construct_email(articles)

    Email(
        'interessantenieuwtjes@gmail.com',
        'simonvdhende@outlook.com',
        'Daily Digest %s' % get_current_day(),
        html
    )


if __name__ == '__main__':
    main()
