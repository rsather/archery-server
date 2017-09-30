from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/contact")
def contact():
    return "You can contact me at 555-5555, or "
    " email me at test@example.com"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for handling login
        pass
    else:
        # Display login form
        pass

if __name__ == "__main__":
    app.run(port=5000, debug=True)
