from flask import Flask, redirect ,render_template, request

app = Flask(__name__)


@app.route('/search4', methods=['POST'] )
def do_search(phrase:str="life the univese and everything", letters:str="aeiou") -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are youre results: '
    results = str(sorted(set(phrase).intersection(set(letters))))
    return render_template('results.html',
    the_phrase=phrase,
    the_letters=letters,
    the_title = title,
    the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

app.run(debug=True)