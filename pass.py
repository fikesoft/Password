from flask import Flask, render_template, request
import random
import string
import secrets
from database import Data


app = Flask(__name__)
app.template_folder = 'templates'


def assign_bool(number, symbols, uppercase):
    # This should be 1 or 0
    if number == "1":
        number = True
    else:
        number = False

    # This should be 1 or 0
    if symbols == "1":
        symbols = True
    else:
        symbols = False

    # This should be 1 or 0
    if uppercase == "1":
        uppercase = True
    else:
        uppercase = False

    return number, symbols, uppercase


def make_pass(length, number, symbols, uppercase):
    #Full dictionary 
    lowercase = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase  
    punctuation = string.punctuation
    digits = string.digits

    password = ""
    
    #Default choice 
    choices = lowercase

    if uppercase and symbols and number:
        choices += uppercase_chars + punctuation + digits
    elif uppercase and symbols:
        choices += uppercase_chars + punctuation
    elif uppercase and number:
        choices += uppercase_chars + digits
    elif symbols and number:
        choices += punctuation + digits
    elif uppercase:
        choices += uppercase_chars
    elif symbols:
        choices += punctuation
    elif number:
        choices += digits

    while len(password) <= int(length):
        password = password + str(secrets.choice(choices))

    return password


def save_database(password):
    class_database = Data()
    query = "INSERT INTO password_gen (password) VALUES ('{}')".format(password)
    try:
        class_database.execute(query)
    except:
        return render_template("wrong.html")




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    length = request.form.get("range")
    
    # Use a default value of "0" if not found
    number = request.form.get("numbers", "0") 
    
    # Use a default value of "0" if not found
    symbols = request.form.get("symbols", "0")  
   
    # Use a default value of "0" if not found
    uppercase = request.form.get("uppercase", "0")  
    
    number, symbols, uppercase = assign_bool(number, symbols, uppercase)
 
    password = make_pass(length, number, symbols, uppercase)

    save_database(password)
    
    return render_template('index.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)
