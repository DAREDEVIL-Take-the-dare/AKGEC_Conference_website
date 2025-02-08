from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')  # Corrected route with '/'
def about():
    return render_template('about.html')

@app.route('/committee')  # Corrected route with '/'
def committee():
    return render_template('commettee.html')

if __name__ == '__main__':
    app.run(debug=True)
