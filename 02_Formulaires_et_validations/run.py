# modules internes
import secrets # pour créer une clé de sécurité
# modules externes
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


# créer une première instance qui représente notre application
app = Flask(__name__)


# créer une nouvelle clé à chaque que l'application est lancé
app_secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = app_secret_key


posts = [
    {
        'author': 'Matar SAMB',
        'title': 'Mon premier post',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis ratione modi ad eaque quidem porro temporibus reprehenderit earum cupiditate nisi, fugiat qui ipsum numquam culpa accusamus harum nostrum similique aliquid.',
        'date_posted': '08/11/2020'
    },
    {
        'author': 'Djiby SECK',
        'title': 'Mon deuxième post',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis ratione modi ad eaque quidem porro temporibus reprehenderit earum cupiditate nisi, fugiat qui ipsum numquam culpa accusamus harum nostrum similique aliquid.',
        'date_posted': '08/11/2020'
    },
    {
        'author': 'Fallou TOURE',
        'title': 'Mon troisième post',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis ratione modi ad eaque quidem porro temporibus reprehenderit earum cupiditate nisi, fugiat qui ipsum numquam culpa accusamus harum nostrum similique aliquid.',
        'date_posted': '08/11/2020'
    }
]


# créer une première route
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


# créer une deuxième route
@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


# créer une deuxième route
@app.route('/about')
def about():
    return render_template("about.html", title='A propos')


# registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm() # on crée une instance pour RegistrationForm
    if form.validate_on_submit():
        flash('Votre compte a été créer avec succès', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Inscription", form=form)


# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'email@gmail.com' and form.password.data == 'password':
            flash('Connexion réussie', 'success')
            return redirect(url_for('home'))
        else:
            flash('Identifiants incorrect.', 'danger')
            return redirect(url_for('login'))
    return render_template("login.html", title="Connexion", form=form)


# lancer notre application
if __name__ == "__main__":
    app.run(debug=True)