from flask import Flask, redirect, render_template, url_for, request
from . import Config, User

app=Flask(__name__)


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
    return redirect(url_for("home"))

@app.get("/home")
def home():
    return render_template("home.html")

# from flask import Flask, render_template, redirect, url_for, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email, EqualTo, Length
# from database import db, User  # Importing database and user model



# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[
#         DataRequired(), EqualTo('password', message='Passwords must match.')
#     ])
#     submit = SubmitField('Register')


# class RegisterView:
#     def __init__(self, app):
#         self.app = app
#         # Define the route for both GET and POST methods
#         self.app.route('/register', methods=['GET', 'POST'])(self.register)

#     def register(self):
#         form = RegistrationForm()
#         if form.validate_on_submit():
#             # Adding user to the database
#             user = User(username=form.username.data, email=form.email.data, password=form.password.data)
#             db.session.add(user)
#             db.session.commit()
#             flash(f'Account created for {form.username.data}!', 'success')
#             return redirect(url_for('register'))  # Redirect to the correct endpoint
#         return render_template('register.html', form=form)


# if __name__ == '__main__':
#     app = WebApp()
#     register_view = RegisterView(app.app)
#     app.run()
