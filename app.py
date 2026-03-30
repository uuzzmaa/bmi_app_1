from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", name = "Uzma")

@app.route("/about")
def about():
    return render_template("about.html", description = " I have done skydiving twice!")

@app.route("/greet",methods = ["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("greet_result.html",name =name)
    return render_template("greet_form.html")

@app.route("/bmi",methods = ["GET", "POST"])
def bmi():
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])/ 100 
        bmi_value = round(weight/(height**2),1)

        if bmi_value <18.5:
            category = "Underweight"
        elif bmi_value < 25:
            category = "Normal weight"
        elif bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return render_template("bmi_result.html",weight =weight, height = float(request.form["height"]), bmi = bmi_value, category= category)
    return render_template("bmi_form.html")
if __name__ == "__main__":
    app.run(debug=True)
