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
    table = csv_to_list()
    update_line = ''
    if story_id:
        for line in table:
            if story_id == line[0]:
                update_line = line
    return render_template('form.html', story_id=story_id, update_line=update_line)


@app.route('/save-table', methods=['POST'])
def route_save():
    table = csv_to_list()
    if len(table) != 0:
        form = [str(int(table[-1][0])+1)]
    else:
        form = ['1']
    for element in ['storytitle', 'userstory', 'acceptance',
                    'value', 'estimation', 'status']:
        form.append(request.form[element])
    table.append(form)
    list_to_csv(table)
    return redirect('/')


@app.route('/delete/<story_id>')
def delete_story(story_id):
    table = csv_to_list()
    for element in table:
        if element[0] == story_id:
            table.remove(element)
    list_to_csv(table)
    return redirect('/')


@app.route('/update-table/<story_id>', methods=['POST'])
def update_story(story_id):
    table = csv_to_list()
    for element in table:
        if element[0] == story_id:
            items = ['storytitle', 'userstory', 'acceptance', 'value', 'estimation', 'status']
            for i in range(1, len(element)):
                element[i] = request.form[items[i-1]]
    list_to_csv(table)
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
    app.run(debug=True, port=5000)
