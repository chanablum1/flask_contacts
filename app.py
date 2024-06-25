from flask import Flask

app = Flask(__name__)

@app.route("/")
def list_contacts():
   return "<p>Hello, World!</p>"


@app.route("/contacts")
def contacts():
   return "<p>Hello, blum!</p>"


@app.route("/addcontacts")
def add_contacts():
   return "<p>Hello, chana!</p>"

if __name__ == '__main__':
   app.run(debug=True)