from flask import Flask

app = Flask('app')


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
