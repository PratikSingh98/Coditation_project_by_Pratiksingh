from flask import Flask, render_template, request
from flask.typing import TemplateFilterCallable
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Codation.db"
app.config["SQLALCHEMY_TRCK_MODIFICATIONS"] = False
db= SQLAlchemy(app)

class Codation(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method== "POST":
        print("post")
    codation = Codation(title="First Category", desc="abcdefghi")
    db.session.add(codation)
    db.session.commit()
    allCodation = Codation.query.all()
    return render_template("index.html", allCodation= allCodation)
    #return "<p>Hello, World!</p>"

@app.route("/show")
def products():
    allCodation = Codation.query.all()
    print(allCodation)
    return "<p>This is product page</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)