from flask import Flask, render_template
from data_processing import DataProcessing

app = Flask(__name__)


@app.route('/covid')
def index():
    DataProcessing().creating_map()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
