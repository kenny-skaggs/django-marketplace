# Django Marketplace
A marketplace coding exercise with Django.

## Dependencies
Whether setting up in a production environment or locally for development, follow these steps to install the necessary packages.

install pipenv
pipenv install dependencies

## Development
pipenv shell


## Deploying
This project can be run in production with Gunicorn. The following is an example systemctl unit that can be used to run the Gunicorn server as a socket. For additional security move the sensitive environment variables into a separate text file with restricted read permissions. Replace all italicized values with the system specific values.

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=<web-user>
Group=www-data
Environment=PYTHONPATH=_/path/to/project/root_
Environment=MARKETPLACE_DB_USER=_database username_
Environment=MARKETPLACE_DB_PASSWORD=_database user password_
Environment=MARKETPLACE_DB=_database name_
Environment=MARKETPLACE_DB_HOST=_database server host_
Environment=MARKETPLACE_DB_PORT=_database server port_
Environment=MARKETPLACE_SECRET_KEY=_Django server secret key_
WorkingDirectory=_/path/to/project/root_
ExecStart=_path/to/gunicorn_ --workers 3 --bind unix:_/path/to/project/root_/gunicorn.sock marketplace.wsgi --preload --timeout 300

[Install]
WantedBy=multi-user.target
