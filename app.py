from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    gender = request.form.get("gender")
    dob = request.form.get("dob")
    address = request.form.get("address")

    if not name or not email or not phone or not password:
        return render_template(
            "register.html",
            message="Please fill in all required fields."
        )

    # Check password
    if password != confirm_password:
        return render_template(
            "register.html",
            message="Passwords do not match."
        )
    print("New User Registered")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Gender:", gender)
    print("Date of Birth:", dob)
    print("Address:", address)

    return render_template(
        "register.html",
        success="Registration successful! Welcome, " + name + "!"
    )


if __name__ == "__main__":
    app.run(debug=True)