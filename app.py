from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/translate", methods=['POST'])
def translate():

    data = request.get_json()
    if 'from' not in data or 'to' not in data or 'msg' not in data is None:
        return jsonify({"status": 500,  "msg": "Please Enter From, Destination Language and Message in your API Resquest."})
    translator = Translator(from_lang=data['from'], to_lang=data['to'])
    print("Posted Data", data['msg'])
    translated_msg = translator.translate(data['msg'])
    return jsonify({"msg": str(translated_msg)})


app.run(host="0.0.0.0", port=5000)
