from typing import Any
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/') # http://www.mysite.com/blog
def home() -> Any:
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run()
    