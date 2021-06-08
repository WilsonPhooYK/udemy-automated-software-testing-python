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
7. Run pipenv: `py -m pipenv shell`
8. Check pipenv dependencies: `py -m pipenv graph`
9. Exit pipenv: `exit`
10. Run black formatting: `black .`
