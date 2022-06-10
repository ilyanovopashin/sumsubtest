from flask import Flask, request, jsonify
import json
import requests
app = Flask(__name__)
HEADERS = {'Content-Type': 'application/json'}
URL_YANDEX = 'https://speller.yandex.net/services/spellservice.json/checkTexts'


@app.route('/', methods=['post'])
def spellcheck():
    incomingdata=request.json
    print(incomingdata)
    yandex_spellcheck_response = requests.get(URL_YANDEX, params = {'text': incomingdata['text']}).json()
    result_text = incomingdata['text']
    for i in range(len(yandex_spellcheck_response[0])):
        result_text = result_text.replace(yandex_spellcheck_response[0][0 + i]['word'],
                                          yandex_spellcheck_response[0][0 + i]['s'][0], 1)
    resp = jsonify(result= result_text)
    return resp

if __name__ == '__main__':
    app.run()