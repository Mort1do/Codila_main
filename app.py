from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import config

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    Fname = db.Column(db.String(30), nullable=False)
    Lname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<users {self.id}>"


with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:                                                                #login form
            email = request.form['email_log']
            password = request.form['password_log']
            user = User(email=email, password=password)
            try:
                email_username = user.query.filter_by(email=email).first()
                Password = user.query.filter_by(password=password).first()
                if not email_username:
                    return render_template("/index.html", error_login="Такого пользователя не существует!") 
                if email_username and not Password:
                    return render_template("/index.html", error_login="Неверный пароль!")  
                else:
                    return render_template("/main.html")
            except:
                return "Ошибка входа"
        except:                                                             #registration form
            Fname = request.form['Fname_reg']
            Lname = request.form['Lname_reg']
            email = request.form['email_reg']
            password = request.form['password_reg']
            password_check = request.form['password_check_reg']
            if password!=password_check:
                return render_template("/index.html", error_register="Пароли не совпадают!", error_register_trigger="active")
            else:
                user = User(email=email, Fname=Fname, Lname=Lname, password=password)
                try:
                    Email = user.query.filter_by(email=email).first()
                    if Email != None:
                        return render_template("/index.html", error_register="Пользователь с такой почтой уже существует!", error_register_trigger="active")
                    else:
                        db.session.add(user)
                        db.session.commit()
                        return redirect('/')
                except:
                    return "Ошибка регистрации"
    else:
        return render_template("/index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("main/dashboard.html")


@app.route('/curses')
def curses():
    return render_template("main/curses.html")


@app.route('/personal_account')
def personal_account():
    return render_template("main/personal_account.html")


@app.route('/schedule')
def schedule():
    return render_template("main/schedule.html")


@app.route('/forum')
def forum():
    return render_template("main/forum.html")


if __name__ == ("__main__"):
    app.run(debug=True)
