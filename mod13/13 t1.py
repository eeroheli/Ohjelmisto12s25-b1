from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    print(luku)
    luku = int(luku)
    isprime = True
    if luku < 2:
        isprime = False
    for i in range(2, luku):
        if luku % i == 0:
            isprime = False
    vastaus = {
        'Number': luku,
        'isPrime': isprime
    }
    return vastaus
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3001)
