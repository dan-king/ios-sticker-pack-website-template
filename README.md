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
# Configure a Web Server Gateway Interface (WSGI)

## Test gunicorn binging (Stop with Control-C after running without error)
    $ gunicorn --bind 0.0.0.0:5001 wsgi:app

## Set up as a service

    $ sudo nano /etc/systemd/system/sticker_pack.service

    [Unit]
    Description=Gunicorn instance to serve sticker pack app
    After=network.target

    [Service]
    User=USER-NAME-HERE
    Group=www-data
    WorkingDirectory=/PATH/TO/PROJECT/ios-sticker-pack-website-template
    Environment="PATH=/PATH/TO/PROJECT/ios-sticker-pack-website-template/venv/bin"
    ExecStart=/PATH/TO/PROJECT/ios-sticker-pack-website-template/venv/bin/gunicorn --workers 3 --bind unix:sticker_pack.sock -m 007 wsgi:app

    [Install]
    WantedBy=multi-user.target

## Start server on system boot

    sudo systemctl start sticker_pack
    sudo systemctl enable sticker_pack

    sudo systemctl status sticker_pack


## Configure nginx

    server {
        listen 80;
        server_name your_domain www.your_domain;

        location / {
            include proxy_params;
            proxy_pass http://unix:/PATH/TO/PROJECT/ios-sticker-pack-website-template/sticker_pack.sock;
        }
    }

    $ sudo nginx -t
    $ sudo systemctl restart nginx

