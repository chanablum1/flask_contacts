from flask import Flask

app = Flask(__name__)

@app.route("/list")
def list_contacts():
   return "chana<br>shmuel<br>binyamin<br>"


@app.route("/contacts")
def contacts():
   return "<p>Hello, chana blum!</p>"


@app.route("/add_contacts")
def add_contacts():
   return "<p>Hello, chana!</p>"

if __name__ == '__main__':
   app.run(debug=True)