from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def index():
    table = csv_to_list()
    return render_template('list.html', table=table)


@app.route('/story')
@app.route('/story/<story_id>')
def form(story_id=None):
    return render_template('form.html', story_id=story_id)


@app.route('/save-table', methods=['POST'])
def route_save():
    session['note'] = request.form['note']
    return redirect('/')


def csv_to_list():
    with open('table.csv', "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def list_to_csv(table):
    with open('table.csv', "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True, port=5000)
