from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homePage.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True) 

@app.route("/login")
def login():
   return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")