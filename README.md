# udemy-automated-software-testing-python
1. [Automated Software Testing with Python](https://www.udemy.com/course/automated-software-testing-with-python/)
2. Used with Pylance extension to practice typed annotations with Python as well.
3. Install pipenv: `py -m pip install pipenv`
4. Create new pipenv project: `py -m pipenv --python 3.9`, temporary disable uwsgi and psycopg2 first
5. Update .vscode settings with virtualenv location
```
"python.analysis.extraPaths": [
    "C:\\Users\\Kaiser\\.virtualenvs\\udemy-automated-software-testing-python-7MNovFjM\\Lib\\site-packages",
],
```
6. Install dependencies: `py -m pipenv install --dev`
7. Run pipenv: `py -m pipenv shell`, `py -m pipenv run cmd`
8. Check pipenv dependencies: `py -m pipenv graph`
9. Exit pipenv: `exit`
10. Run black formatting: `black .`
11. Make sure the bottom intepreter is selected as the pipenv python.


# Testing
1. Change path for the project you are using at `.vscode/settings.json`, under `python.testing.unittestArgs` if using unittest
2. Set .env path to project folder if using pytest `PYTHONPATH=`
3. `py -m unittest tests/unit/post_test.py`

# Postman
1. Create test collection and enviornment and export file without spaces.
2. Install newman `npm install -g newman`
3. Make sure app is running and run: `newman run postman/tests.postman_collection.json -e postman/tests.postman_environment.json`
4. install Make for windows: `choco install make` as administrator.
5. Run makefile: `make run-tests clear-db=true`

