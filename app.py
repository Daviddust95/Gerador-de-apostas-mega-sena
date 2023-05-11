import random
from flask import Flask

app = Flask(__name__)

def gerar_aposta():
    numeros = []
    while len(numeros) < 6:
        numero = random.randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
    numeros.sort()
    return numeros

@app.route('/')
def index():
    numeros = gerar_aposta()
    return f'Números da aposta: {numeros}'

if __name__ == '__main__':
    app.run()

