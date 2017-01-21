from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cs499')
@app.route('/cs499/<name>')
def hello(name=None):
    return render_template('aboutme.html', name=name)


if __name__ == '__main__':
    app.run()
