from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/start')
def start_job():
    return 'start'


@app.route('/stop')
def end_job():
    return 'stop'


if __name__ == '__main__':
    app.run()
