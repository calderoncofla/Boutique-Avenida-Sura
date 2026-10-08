from pathlib import Path
from flask import Flask, send_from_directory

app = Flask(__name__)
carpeta = Path(__file__).resolve().parent


@app.route("/")
def inicio():
    return send_from_directory(str(carpeta), "index.html")


if __name__ == "__main__":
    app.run()