from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Auckland Registered Clinical Psychologist')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/chinese")
def chinese():
    return render_template('chinese.html', title='思穎心理診所 | 奧克蘭註冊臨床心理師')

@app.route("/faq")
def faq():
    return render_template('faq.html', title='FAQ')

@app.route("/services")
def services():
    return render_template('services.html', title='Services')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/test")
def test():
    return render_template('test.html', title='test')

if __name__ == '__main__':
    app.run(debug=True)
