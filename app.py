from flask import Flask , request

app = Flask(__name__)
@app.route('/')
def home():
    return '''
        <form method="POST" action="/matches">
            <label for="test_string">Test String:</label>
            <input type="text" id="test_string" name="test_string"><br><br>
            <label for="regex">Regex:</label>
            <input type="text" id="regex" name="regex"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''
import re


@app.route('/matches', methods=['POST'])
def matches():
    test_string = request.form['test_string']
    regex = request.form['regex']
    matches = re.findall(regex, test_string)
    return f'Matches: {matches}'
if __name__ == '__main__':
    app.run(debug = True)
