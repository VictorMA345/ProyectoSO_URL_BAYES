#Its necessary to install flask: pip install flask
#imports
from flask import Flask, render_template, redirect, url_for,request
app = Flask(__name__)

containers=[('Crunchyroll','Anime'),('Youtube','Videos'),('Twitter','Red Social'),('Facebook','Red Social'),('RedTube','Red Social')]
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        categorie=request.form["categoria"]
        return redirect(url_for("categories",cat=categorie))
    else:
        return render_template('index.html')

@app.route("/<cat>")
def categories(cat):
    #return f"<h1>{cat}</h1>"
    print("La categoria es",cat)
    return render_template('index.jinja2',category=cat)
        
    
if __name__=="__main__":
    app.run()

