from flask import Flask, render_template
import requests

app = Flask(__name__)


response = requests.get(url=" https://api.npoint.io/53d19943d95addeca868")
response.raise_for_status()
data = response.json()
print(data)

@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", id=id, data=data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
