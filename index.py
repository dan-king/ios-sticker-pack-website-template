import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_from_directory,
    session,
    url_for,
)
from dotenv import load_dotenv


# Configure environment
load_dotenv()
print(f"FLASK_APP: {os.environ.get('FLASK_APP')}")
print(f"FLASK_ENV: {os.environ.get('FLASK_ENV')}")
print(f"FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")
print(f"FLASK_RUN_HOST: {os.environ.get('FLASK_RUN_HOST')}")
print(f"FLASK_RUN_PORT: {os.environ.get('FLASK_RUN_PORT')}")


# Create Flask app
app = Flask(__name__)


# Homepage route
@app.route("/")
def root() -> "302":
    return redirect("/home")


@app.route("/home")
def home() -> "html":

    return render_template(
        "home.html",
    )


# Start the Flask app if the current, active module is __main__.
print(f"__name__: {__name__}")
if __name__ == "__main__":
    print(
        f"Running app on host {os.environ.get('FLASK_RUN_HOST')} on port {os.environ.get('FLASK_RUN_PORT')}"
    )
    # app.run(debug=True)
    # app.run()
    # app.run(port=os.environ.get('FLASK_RUN_PORT'))
    app.run(
        host=os.environ.get("FLASK_RUN_HOST"), port=os.environ.get("FLASK_RUN_PORT")
    )
