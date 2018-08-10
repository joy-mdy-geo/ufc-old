from flask import Flask, render_template, jsonify, request
import controller
import pyperclip

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/_convert', methods=["POST"])
def convert():
    from_text = request.form['from_text']
    from_encoding = request.form['from_encoding']
    to_encoding = request.form['to_encoding']
    res = controller.convert(from_encoding, to_encoding, from_text)
    return jsonify(result=res)


@app.route('/_copy')
def copy():
    txt = request.args.get('to_text', '', type=str)
    pyperclip.copy(txt)
    return jsonify(result=txt)


if __name__ == "__main__":
    app.run(debug=True)
