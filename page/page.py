#Its necessary to install flask: pip install flask
#imports
import json
from flask import Flask, render_template, redirect, url_for,request
app = Flask(__name__)

containers=[('Crunchyroll','Anime'),('Youtube','Videos'),('Twitter','Red Social'),('Facebook','Red Social'),('RedTube','Red Social')]
pages=[{"page":"namepage", "Column01":"data", "Column02":"data"},{"page":"namepage2", "Column01":"data", "Column02":"data"}]

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
    pagesList=[] #Paginas ya revisadas conforme a la categoria
    #Clasificacion de las paginas por categoria
    #for i in pages:
        #currentPage=json.load(i) #esto sirve para cargar el JSON
        #if(currentPage['Category']==cat): Esto sirve para clasificar la pagina conforme la categoria
            #pagesList.append(currentPage)
    print("La categoria es",cat)
    return render_template('index.jinja2',category=cat,data=pages)
        
    
if __name__=="__main__":
    app.run()

