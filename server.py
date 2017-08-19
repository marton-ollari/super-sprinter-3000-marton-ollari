from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def index():
    return render_template('list.html')


@app.route('/story')
@app.route('/story/<story_id>')
def form(story_id=None):
    return render_template('form.html', story_id=story_id)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
