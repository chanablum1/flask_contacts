from flask import Flask , render_template

# from servise.add import add_contacts

app = Flask(__name__)

my_contacts = [
    {
        "name": "chana",
        "age": 24,
        "pone": "0583275113",
        "email": "c0583275113@gmail.com",
    },
    {
        "name": "shmuel",
        "age": 26,
        "pone": "0548589107",
        "email": "s0548589107@gmail.com",
    },
]


@app.route("/")
def contacts_list():
    return render_template("contact_list.html", contacts = my_contacts)

   #  final_html_str = ""
   #  for contact in my_contacts:
   #      final_html_str += f"{contact['name']} - {contact['age']} - {contact['pone']} - {contact['email']}<br>"
   #  return final_html_str


# @app.route("/single_contact/<int:index>")
# def single_contact(index):
#     return f"<h1>Single Contact Page </h1><h2>{my_contacts[index]['name']} - {my_contacts[index]['age']}</h2>"

# @app.route("/add_contacts")
# def add_contacts():
#     return '''
#     <html>
#     <head>
#         <style>
#             button {
#                 background-color: blue;
#                 color: white;
#                 padding: 10px 20px;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#             }
#             button:hover {
#                 background-color: darkblue;
#             }
#         </style>
#     </head>
#     <body>
#         <button> Hello, Chana! </button>
#     </body>
#     </html>
#     '''

# @app.route("/add_contacts")
# def add_contacts():
#    return f"<bottom> Hello, chana! </bottom>"



if __name__ == "__main__":
    app.run(debug=True)
   
