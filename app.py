from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/generate-resume", methods = ["POST", "GET"])
def generate_resume():
    
    return render_template("generate_resume.html")                           

@app.route("/resume-template", methods = ["POST"])
def resume_template():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("number")
        address = request.form.get("address")
        career = request.form.get("career")
        skills = request.form.get("skills").split(",")
        college_name = request.form.get("college_name")
        degree_name = request.form.get("degree_name")
        education_year = request.form.get("education_year")
        cgpa = request.form.get("cgpa")
        experience = request.form.get("experience")
        projects = request.form.get("projects").split(",")
    return render_template("resume_template.html",
                           name=name,
                           email=email,
                           number = phone,
                           address = address,
                           career = career,
                           skills = skills,
                           college_name=college_name,
                           degree_name=degree_name,
                           education_year=education_year,
                           cgpa=cgpa,
                           experience = experience,
                           projects = projects
                           )

if __name__ == "__main__":
    app.run(debug = True)