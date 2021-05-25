from fastapi import FastAPI
import random
app = FastAPI()

@app.get('/')
def home():
    return 'Salem!'


@app.get('/quotes')
def quote():
    quotes = [
        'Адамның ең ұлы қасиеті - бақытты болуға талпынуы',
        'Еңбек – бақыттың атасы',
        'Адам өміріндегі ең тамаша нәрсе – оның басқа адамдармен қарым – қатынасы.',
        'Жүрегі таза адам қиянатқа бармайды.'
    ]

    result = random.choice(quotes)
    return result
