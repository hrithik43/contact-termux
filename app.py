from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']
        
        with open('user_data.txt', 'a') as file:
            file.write(f"Name: {name}\nEmail: {email}\nContact: {contact}\nAddress: {address}\n\n")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
