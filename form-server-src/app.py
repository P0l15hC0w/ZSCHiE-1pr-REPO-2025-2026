from flask import Flask, request, render_template

app = Flask(__name__)

file=open("form.txt", "a")

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    print(request.form)
    name = request.form.get("name")
    age = request.form.get("age")
    email = request.form.get("email")
    color = request.form.get("color")
    file.write(f"{name}, {age}, {email}, {color}\n")
    file.close()

    return f"""
    <div style="max-width:500px;margin:40px auto;padding:32px;background:#f8f9fa;border-radius:16px;box-shadow:0 4px 24px rgba(0,0,0,0.08);font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
        <h1 style="color:#0078d7;text-align:center;margin-bottom:24px;">Dziękujemy za przesłanie danych!</h1>
        <div style="font-size:1.1em;line-height:1.7;">
            <p><b>Imię:</b> {name}</p>
            <p><b>Wiek:</b> {age}</p>
            <p><b>Email:</b> {email}</p>
            <p style="color: #fff; background-color: {color}; padding:8px 0; text-align:center; border-radius:8px; margin:16px 0;">
                Ulubiony kolor
            </p>
        </div>
        <div style="text-align:center;margin-top:24px;">
            <a href='/' style="display:inline-block;padding:10px 24px;background:#3182ce;color:#fff;border-radius:8px;text-decoration:none;font-weight:500;transition:background 0.2s;">Wróć do formularza</a>
        </div>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
    