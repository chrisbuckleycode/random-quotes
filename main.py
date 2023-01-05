import random
from flask import Flask, render_template

app = Flask(__name__)

# Quotes changed due to copyright.

movieQuotes = [
    "moviequote1",
    "moviequote2",
    "moviequote3",
]

sportsQuotes = [
    "sportsquote1",
    "sportsquote2",
    "sportsquote3",
]

inspirationalQuotes = [
    "inspirationalquote1",
    "inspirationalquote2",
    "inspirationalquote3",
]

firstSentence = [
    "1stsentenceno.1",
    "1stsentenceno.2",
    "1stsentenceno.3",
]

secondSentence = [
    "2ndsentenceno.1",
    "2ndsentenceno.2",
    "2ndsentenceno.3",
]

thirdSentence = [
    "3rdsentenceno.1",
    "3rdsentenceno.2",
    "3rdsentenceno.3",
]


@app.route('/')
def get_quotes():
    movie_quote = random.choice(movieQuotes)
    sports_quote = random.choice(sportsQuotes)
    inspirational_quote = random.choice(inspirationalQuotes)
    return render_template('quotes.html', movie_quote=movie_quote, sports_quote=sports_quote, inspirational_quote=inspirational_quote)

@app.route('/twitterthread')
def get_twitterthread():
    first_sentence = random.choice(firstSentence)
    second_sentence = random.choice(secondSentence)
    third_sentence = random.choice(thirdSentence)
    return render_template('twitterthread.html', first_sentence=first_sentence, second_sentence=second_sentence, third_sentence=third_sentence)


if __name__ == '__main__':
    app.run()
