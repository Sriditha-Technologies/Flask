from flask import Flask, render_template, request, g, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "123"  # Secret key for session management

# Define a user class to represent users
class User:
    def __init__(self, id, Username, Password):
        self.id = id
        self.Username = Username
        self.Password = Password

# List to hold user instances
users = []
users.append(User(id=1, Username="dhamu", Password="dhamu@123"))
users.append(User(id=2, Username="saba", Password="saba@123"))
users.append(User(id=3, Username="amul", Password="amul@123"))

@app.route('/', methods=['GET', 'POST'])  # Correct the 'methods' spelling
def login():
    if request.method == "POST":
        uname = request.form['uname']  # Correctly access form data
        upass = request.form['upass']  # Correctly access form data
        
        # Check credentials against the users list
        for data in users:
            if data.Username == uname and data.Password == upass:  # Correct attribute names
                session['user_id'] = data.id  # Store user ID in session
                return redirect(url_for('user'))  # Redirect to user route

        flash("Username or password mismatch....!!!", "danger")  # Flash an error message
        return redirect(url_for("login"))
    
    return render_template("login.html")  # Render the login template for GET requests

@app.before_request
def before_request():
    g.user = None  # Set default value for g.user
    if 'user_id' in session:  # Correct session key
        user_id = session['user_id']
        # Find the user by ID in the users list
        for data in users:
            if data.id == user_id:
                g.user = data  # Save the user object to g for later use

@app.route('/user')
def user():
    if not g.user:  # Check if user is logged in
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('user.html', username=g.user.Username)  # Pass username to template

@app.route('/logout')
def logout():
    session.clear()  # Clear the session
    return redirect(url_for('login'))  # Redirect to login

if __name__ == "__main__":
    app.run(debug=True)