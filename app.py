from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def wegmans_app():
    return render_template('index.html', hello="hello")

@app.route('/recipes')
def recipes():
    return ''



if __name__ == '__main__':
    app.run()
