### Create a Flask API

- You can choose what it does!
- Your API should respond to at least one GET and one POST request
- Add at least one extension eg. a database connection or an email service
- Follow documentation to add some tests using pytest

### Run Demo

- `cd flask-demo` 
- `pipenv install -r requirements.txt`
- `pipenv shell`
- Tell terminal which application to work with:
   - `export FLASK_APP=server.py` _(Linux/MacOS/GitBash)_ 
   - `set FLASK_APP=server.py` _(Windows Command Prompt)_ 
   - `$env:FLASK_APP = "server.py"` _(PowerShell)_
- Tell terminal which environment to work in:
   - `export FLASK_ENV=development` _(Linux/MacOS/GitBash)_ 
   - `set FLASK_ENV=development` _(Windows Command Prompt)_ 
   - `$env:FLASK_ENV="development"` _(PowerShell)_
- `flask run`
