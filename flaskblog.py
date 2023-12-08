from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
 
app = Flask(__name__)

app.config['SECRET_KEY'] = '27511beac0d49190' 



posts = [
    {
        'author': 'Nida',
        'title': 'Blog 1',
        'content': 'Post 1',
        'date': '3 dec 2023'
    },
    {
        'author': 'Saqib',
        'title': 'Blog 2',
        'content': 'Post 2',
        'date': '5 dec 2023'
    }
]



@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = "About")


@app.route("/register")
def register():
    form = RegistrationForm()

    return render_template('Register.html', title = 'Register', form = form)



@app.route("/login")
def login():
    form = LoginForm()

    return render_template('login.html', title = 'Login', form = form)








if __name__ == '__main__':
    app.run(debug=True)