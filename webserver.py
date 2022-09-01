from flask import Flask, jsonify, request, render_template, url_for, redirect
from captchaSolver import getCaptcha

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		url = request.form["link"]
		resp = getCaptcha(url)
		resultjson = jsonify(resp)
		result = resultjson.json["success"]
		if result == False:
			result = resultjson.json["msg"]
		else:
			result = resultjson.json["captcha"]
		return render_template("index.html", result = result)
	else:
		return render_template("index.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000', threaded=True)
