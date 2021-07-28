from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import ContentRange
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    name = db.Column(db.String(200),primary_key = True)
    email = db.Column(db.String(200),nullable = False)
    phone = db.Column(db.String(12),nullable = False)
    desc = db.Column(db.String(200),nullable = False)
    date= db.Column(db.DateTime,default = datetime.utcnow)
class Services(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(500),nullable = False)
    date_crated = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        desc = request.form['desc']
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc,date=datetime.today())
        db.session.add(contact)
        db.session.commit()
    return render_template("contact.html")
@app.route("/services",methods = ['GET','POST'])
def services():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        services = Services(title=title,desc=desc)
        db.session.add(services)
        db.session.commit()
    allServices=Servies.query.all()
    alltodo = str(allServices)
    return alltodo


if __name__== "__main__" :
    app.run(debug = True)