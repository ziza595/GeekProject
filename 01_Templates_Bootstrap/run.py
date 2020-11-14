from flask import Flask, render_template


# créer une première instance qui représente notre application
app = Flask(__name__)


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


# lancer notre application
if __name__ == "__main__":
    app.run(debug=True)
