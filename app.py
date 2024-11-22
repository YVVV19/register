from flask import Flask, redirect, render_template, url_for, request
from . import Config, User, migrate

app=Flask(__name__)

migrate()


@app.get("/register")
def register():
    return render_template("register.html")


@app.post("/register")
def create_register():
    form = request.form
    if form:
        with Config.SESSION.begin() as session:
            register = [User(
                **form,
            )]
            session.add_all(register)
    return redirect(url_for("register"))

@app.get("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)