"""Main application file"""

from flask import Flask

MESSAGE = "Hello from Deniz!\n"
PORT = 51679
app = Flask(__name__)

@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    return "".join(reversed(random_string))

@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

