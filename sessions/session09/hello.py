from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Class!</h1>"
   

if __name__ == "__main__":
    app.run(debug=True)






# return render_template("hello.html") 
