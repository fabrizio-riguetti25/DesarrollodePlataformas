from flask import Flask, render_template, request, url_for 

app = Flask(__name__) 
 
@app.route("/")
def index():
    return render_template("Login_curriculum.html")
 

@app.route("/", methods=["GET","POST"])
def hola():
    email = request.form.get("email") 
    email=email
    if email == "fabrizio.riguetti@ucsp.edu.pe":
        return render_template("Curriculum.html")
        
    elif email == "Italo.Cancha@ucsp.edu.pe":
        return render_template("Curriculumb.html")
        
    elif email == "Samir.carrera@ucsp.edu.pe":
        return render_template("Curriculumc.html")
    else:
        return "Datos errroneos , revisar nuevamente"