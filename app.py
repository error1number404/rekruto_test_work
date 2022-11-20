import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    name, message = flask.request.args.get('name'), \
                    flask.request.args.get('message')
    if not any((name, message)):
        return 'Error'
    return f"Hello {name}! {message}!"


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 80)
