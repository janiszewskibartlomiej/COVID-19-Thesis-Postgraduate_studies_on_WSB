from flask import Flask, render_template
from map_of_the_world import CreatingMap
app = Flask(__name__)


@app.route('/')
def index():
    CreatingMap().creating_map_of_the_world()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
