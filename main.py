from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/politicas-de-privacidade')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/termos-de-uso')
def terms_of_use():
    return render_template('terms-of-use.html')

if __name__ == '__main__':
    app.run()
