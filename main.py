from flask import Flask, render_template, jsonify, request
import controller
import pyperclip

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/_convert')
def convert():
    from_text = request.args.get('from_text', '', type=str)
    to_text = request.args.get('to_text', '', type=str)
    from_encoding = request.args.get('from_encoding', '', type=str)
    to_encoding = request.args.get('to_encoding', '', type=str)
    # res = from_encoding + '\n' + to_encoding + '\n' + from_text
    res = controller.convert(from_encoding, to_encoding, from_text)
    return jsonify(result=res)


@app.route('/_copy')
def copy():
    txt = request.args.get('to_text', '', type=str)
    pyperclip.copy(txt)
    return jsonify(result=txt)


@app.route('/_paste')
def paste():
    txt = pyperclip.paste()
    return jsonify(result=txt)


@app.route('/_clear')
def clear():
    return jsonify(result='')


if __name__ == "__main__":
    app.run()
