from models.Email import Email


def main():
    html = """
    <h4>Dit is een titel</h4>
    <ul>
        <li>Bolleke 1</li>
        <li>Bolleke 2</li>
        <li>Bolleke 3</li>
    </ul>
    
    <img src="https://i.ebayimg.com/00/s/NTQ1WDcyOA==/z/TJUAAOSwYihc2YXa/$_86.JPG" alt="nen auto">
    """

    Email(
        'interessantenieuwtjes@gmail.com',
        'simonvdhende@outlook.com',
        'testje met html',
        html
    )


if __name__ == '__main__':
    main()
