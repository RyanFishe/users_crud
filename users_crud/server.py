from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("home.html", all_users = users)

@app.route('/user/show/<int:id>')
def show(id):
    # calling the get_one method and supplying it with the id of the user we want to get
    user=User.get_one(id)
    return render_template("show_user.html",user=user)

@app.route('/user/createpage')
def user_page():
    return render_template("create.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def show_edit(id):
    user=User.get_one(id)
    return render_template("edit.html",user=user)


@app.route('/user/update/<int:id>',methods=['POST'])
def update(id):
    User.update(request.form, id)
    return redirect("/")

@app.route('/user/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')
            
if __name__ == "__main__":
    app.run(debug=True)
