import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
   raise RuntimeError("API_KEY not set")



@app.route("/")
@login_required
def index():

    rows =db.execute("""
    SELECT symbol, SUM(shares) as totalShares
    FROM transactions WHERE user_id = :user_id
    GROUP BY symbol
    HAVING totalShares > 0;
    """, user_id = session["user_id"])

    holdings = []
    grand_total = 0
    for row in rows:
        stock = lookup(row["symbol"])
        holdings.append ({
            "symbol":stock['symbol'],
            "name": stock["name"],
            "shares": row['totalShares'],
            "price" : usd(stock ["price"]),
            "total": usd(stock['price']*row ["totalShares"])
        })
        grand_total += stock['price'] + row ['totalShares']
    rows = cash = db.execute("Select cash from users where id = :id", id = session["user_id"])
    cash  = rows[0]["cash"]
    grand_total += cash
    return render_template("index.html", holdings = holdings, cash = usd(cash), grand_total = usd(grand_total))





    #return apology("TODO")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method =='GET':
        return render_template("sell.html")
    else:
        if not request.form.get("symbol"):
            return apology("no symbol searched", 400)
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        if stock == None:
            return apology("invalid symbol entered", 400)

        shares_selling = int(request.form.get("shares"))
        if not request.form.get ("shares").isdigit():
            return apology("invalid shares (negative)", 403)

        rows = db.execute ("SELECT SUM(shares) as totalshares from transactions where symbol=:symbol and user_id =:id group by symbol", symbol =symbol, id= session["user_id"])
        shares_bought = rows[0]['totalshares']

        if shares_selling > shares_bought:
            return apology("not enough shares", 400)

        if shares_bought <= 0:
            return apology("invalid amount", 400)

        #finding previous owned csah and adding new cash to the server in the next couple of lines
        user  = db.execute("SELECT * FROM users where id = :id", id = session["user_id"])
        oldcash = user[0]['cash']

        newcash  = shares_selling * stock ['price']

        #old method
            #updated_cash = newcash + oldcash
        db.execute ("UPDATE users SET cash = cash + :selling where id =:id", selling =newcash , id = session["user_id"])
        #fix this inquiry need to update the new shares
            #db.execute ("UPDATE transaactions SET shares=:newshares where id = :id and symbol = :symbol group by symbol",
            #newshares=shares_bought-shares_selling, id = session["user_id"], symbol = symbol)


        db.execute ("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:id,:symbol,:shares,:price)",
                id = session['user_id'], symbol = symbol , shares=-shares_selling , price= newcash)

        flash('sold')



        return render_template("checker.html", rows = rows, share = shares_bought)

    #return apology("TODO")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'POST':
        if not request.form.get("symbol"):
            return apology("no symbol searched", 400)
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        if stock == None:
            return apology("invalid symbol entered", 400)
        shares = int(request.form.get("shares"))
        if not request.form.get ("shares").isdigit():
            return apology("invalid shares (negative)", 403)

        #select cash from id
        rows = db.execute ("SELECT cash FROM users WHERE id=:id", id= session["user_id"])
        cash = rows[0]['cash']
        cashneeded = stock['price'] * shares
        updatedcash = cash - cashneeded
        if updatedcash<0:
            return apology("your broke", 400)
        db.execute("UPDATE users SET cash=:updatedcash WHERE id=:id",
                    updatedcash=updatedcash, id=session["user_id"])
        #stock that was bought and the number of shares and who bought the stock-personal to user
        db.execute("INSERT INTO transactions (user_id, symbol ,shares,price) VALUES (:user_id,:symbol, :shares, :price)",
                    user_id= session["user_id"],
                    symbol = symbol,
                    shares = shares,
                    price= stock['price'])
        flash ("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html")

    #return apology("TODO")


@app.route("/history")
@login_required
def history():
    transactions = db.execute("SELECT symbol, shares, price, transacted from transactions where user_id =:id ", id = session["user_id"])
    return render_template("history.html", transactions = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'POST':
        if not request.form.get("symbol"):
            return apology("no symbol searched", 400)
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        if stock == None:
            return apology("invalid symbol entered", 400)

        return render_template("quoted.html", stock = stock )
    else:
        return render_template("quote.html")


    #return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        if not request.form.get ("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide username", 403)
        if request.form.get("password") != request.form.get("confirmation"):
            return apology ("passwords do not match", 403)
        row = db.execute ("SELECT * FROM users WHERE username = :username",
                        username = request.form.get("usrname"))
        if len (row) >= 1:
            return apology ("username exits", 403)
        username = request.form.get("username")
        hash = generate_password_hash(request.form.get("password"))

        primkey = db.execute ("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                    username = username , hash = hash)

        if primkey is None:
            return apology("Registration error, check if username already exists", 403)
        session["user_id"] = primkey
        return redirect("/")
    #return apology("TODO")




def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
