def add_two_number(i:int, j:int) -> int or TypeError:
    if type(i)!= int or type(j)!=int:
        raise TypeError()
    return i+j

import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """_summary_

    Returns:
        _type_: _description_
    """
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

if __name__ == "__main__":
    """_summary_
    """
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))