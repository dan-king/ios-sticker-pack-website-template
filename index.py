import markdown
import pandas as pd
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


# Product page route
@app.route("/product")
def product() -> "html":
    stickers_csv = pd.read_csv("content/stickers.csv")
    print(f"stickers_csv: {stickers_csv}")
    sticker_list = []
    for index, row in stickers_csv.iterrows():
        print(row['Sticker'], row['License'])
        sticker = row['Sticker']
        image = row['Image']
        license = row['License']
        license_page = row['license_page']
        copyright_year = row['copyright_year']
        copyright_name = row['copyright_name']
        copyright_link = row['copyright_user_link']
        s = [
            sticker,
            image,
            license,
            license_page,
            copyright_year,
            copyright_name,
            copyright_link
        ]
        sticker_list.append(s)

    return render_template(
        "product.html",
        stickers_csv=stickers_csv,
        sticker_list=sticker_list,
    )


# Privacy page route
@app.route("/privacy")
def privacy() -> "html":
    with app.open_resource("content/privacy_policy.MD") as f:
        privacy_policy_md = f.read()
    privacy_policy = privacy_policy_md.decode("utf-8")
    privacy_policy_html = markdown.markdown(privacy_policy)
    return render_template(
        "privacy.html",
        privacy_policy_html=privacy_policy_html,
    )


# Support page route
@app.route("/support")
def support() -> "html":
    with app.open_resource("content/support.json") as f:
        support = f.read()
    support_json = support.decode("utf-8")
    return render_template("support.html", support_json=support_json)


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
