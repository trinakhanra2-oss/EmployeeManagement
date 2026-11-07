# Employee Management Portal

print("Employee Management Portal")
print("Project initialized successfully")

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Employee Management Portal</h1>
    <p>Welcome to our Employee Management System.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
