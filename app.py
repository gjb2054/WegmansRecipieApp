from flask import Flask

app = Flask(__name__)


@app.route('/')
def wegmans_app():
    return 'Hello World!'

@app.route('/recipes')
def recipes():
    return ''



if __name__ == '__main__':
    app.run()
