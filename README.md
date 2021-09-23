# ios-sticker-pack-website-template
A configurable Python Flask web template to fulfill the website requirements of a sticker pack app in the Apple App Store.

# Setup

Set up a Python virtual env (optional).

    $ python3 -m virtualenv venv
    $ source venv/bin/activate

Install dependencies.

    $ pip install -r requirements.txt

Create .env environment file

    $ cp env_prod .env

# Customize

Customize in Visual Studio Code (optional).

    $ open workspace.code-workspace

Edit content files
    $ nano content/stickers.csv

    $ nano content/privacy_policy.MD

    $ nano content/support.json

Format code with PEP 8 compliant formatter 'black' (optional).

    $ black .

# Run

    $ python index.py