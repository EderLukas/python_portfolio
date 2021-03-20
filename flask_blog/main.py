from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:id>")
def post(id):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    for blog_post in all_posts:
        if blog_post["id"] == id:
            post = blog_post
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
