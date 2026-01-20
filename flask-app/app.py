from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Chuck Norris Monitor töötab!"

@app.route("/health")
def health():
    return {"status":"ok"}

app.run(host="0.0.0.0", port=5000)
