from flask import app


@app.route("/add_contacts")
def add_contacts():
    return '''
    <html>
    <head>
        <style>
            button {
                background-color: blue;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: darkblue;
            }
        </style>
    </head>
    <body>
        <button> Hello, Chana! </button>
    </body>
    </html>
    '''
