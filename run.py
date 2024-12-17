from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template ('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)