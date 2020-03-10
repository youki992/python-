from flask import Flask
app = Flask(__name__)
@app.route("/")
def XX():
    return "hello world"
if __name__ == '__main__':
    app.run(debug=True,port='8080',host='127.0.0.1')