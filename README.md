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

# Customize (optional)

Customize in Visual Studio Code (optional).

    $ open workspace.code-workspace

Format code with PEP 8 compliant formatter 'black' (optional).

    $ black .

# Run

    $ python index.py