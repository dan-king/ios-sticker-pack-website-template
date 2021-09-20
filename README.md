# ios-sticker-pack-website-template
A configurable Python Flask web template to fulfill the website requirements of a sticker pack app in the Apple App Store.

# Setup

Set up a Python virtual env (optional).

    $ python3 -m virtualenv venv
    $ source venv/bin/activate

Install dependencies.

    $ pip install -r requirements.txt

Create .env environment file

    $ cp env_dev .env

# Configure Content

    $ cp content/stickers_template.csv content/stickers.csv
    $ nano content/stickers.csv

    $ cp content/privacy_policy_template.MD content/privacy_policy.MD
    $ nano content/privacy_policy.MD

    $ cp content/support_template.json content/support.json
    $ nano content/support.json

# Customize (optional)

Customize in Visual Studio Code (optional).

    $ open workspace.code-workspace

Format code with PEP 8 compliant formatter 'black' (optional).

    $ black .

# Run

    $ python index.py