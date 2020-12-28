from flask import Flask, render_template, request

import os
import requests
import subprocess


app = Flask(__name__)


LANGUAGES = ["japanese", "korean", "chinese"]


def get_output(language, input_text):
    res = subprocess.check_output(
        [cmd.format("katakana", input_text)],
        shell=True
    )
    output = ''.join(res.decode('utf-8').split()[1:])
    return output

@app.route('/', methods=("GET", "POST"))
def index():
    if request.method == "POST":
        language = request.form.get("language")
        input_text = request.form["input_text"]
        result = {}
        # call phonetisaurus to get prediction
        cmd = "phonetisaurus predict --model models/{}_ps_1/model.fst {}"
        if language == "japanese":
            output = get_output("katakana", input_text)
        elif language == "korean":
            output = get_output("korean", input_text)
        elif language == "chinese":
            output = get_output("chinese", input_text)
        else:
            result["prediction"] = "Bad input, try again"
            return render_template('index.html', languages=LANGUAGES, res=result)
        # format output
        result["prediction"] = "It's {}".format(output)
        return render_template('index.html', languages=LANGUAGES, res=result)
    return render_template('index.html', languages=LANGUAGES, res=None)