from flask import Flask, render_template, redirect, url_for, g, request

app = Flask(__name__)

@app.before_request
def get_users_info():
    with open('users.yaml', 'r') as file:
        content = file.readlines()
    users = []
    user = {}
    for idx, line in enumerate(content, start=1):
        if not line[0].isspace():
            if idx != 1:
                users.append(user)
                
            name = line.replace(":", "").strip()
            user = { 'name': name }
        elif line.lstrip().startswith("email"):
            email = line.strip().replace("email: ", "")
            user['email'] = email 
        elif line.lstrip().startswith("interests"):
            user['interests'] = []
        else:
            interest = line.replace("-", "").strip()
            user['interests'].append(interest)
        
        if idx == len(content): # last line
            users.append(user)
            
    g.users = users 
    g.num_users = len(users)
    g.total_likes = sum([len(user['interests']) for user in users])

@app.route("/")
def index():
    return redirect(url_for('users'))

@app.route("/users")
def users():
    return render_template("home.html", 
                           users=g.users,
                           num_users=g.num_users,
                           total_likes=g.total_likes)

@app.route("/users/<user_name>")
def profile(user_name):
    # invalid user_name: redirect to home directory "/"
    current_user = {}
    other_users = []
    for user in g.users:
        if user['name'] == user_name:
            current_user = user 
        else:
            other_users.append(user)

    return render_template('profile.html', 
                           user=current_user,
                           other_users=other_users,
                           num_users=g.num_users,
                           total_likes=g.total_likes)

@app.route("/add_user", methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        interests = request.form['interests']
        email_line = f'email: {email}'
        user_interests = interests.split(",") if interests else [] 
        print(user_interests)

        with open("users.yaml", "a") as file:
            file.write(f"\r\n{username}:")
            file.write(f"\r\n{email_line.rjust(len(email_line) + 2)}")
            
            if not user_interests:
                interest_line = "interests: []"
                file.write(f"\r\n{interest_line.rjust(len(interest_line) + 2)}")  
            else: 
                file.write(f"\r\n{"interests:".rjust(len("interests:") + 2)}")    
                for interest in user_interests:
                    interest_line = f"- {interest}"
                    file.write(f"\r\n{interest_line.rjust(len(interest_line) + 4)}")
            
        return render_template('form.html',
                           num_users=g.num_users,
                           total_likes=g.total_likes)

    # GET method
    return render_template('form.html',
                           num_users=g.num_users,
                           total_likes=g.total_likes)

if __name__ == "__main__":
    app.run(debug=True, port=5003)