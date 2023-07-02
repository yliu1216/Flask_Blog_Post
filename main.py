from flask import Flask, render_template, request
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/09f08c6e3a7e82bc6bb7"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", posts=requested_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form['username']
        password = request.form['password']
    return f"<h1>Name:{name}, Password:{password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
