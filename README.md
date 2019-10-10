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

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=<web-user>
Group=www-data
Environment=PYTHONPATH=*/path/to/project/root*
Environment=MARKETPLACE_DB_USER=*database username*
Environment=MARKETPLACE_DB_PASSWORD=*database user password*
Environment=MARKETPLACE_DB=*database name*
Environment=MARKETPLACE_DB_HOST=*database server host*
Environment=MARKETPLACE_DB_PORT=*database server port*
Environment=MARKETPLACE_SECRET_KEY=*Django server secret key*
WorkingDirectory=*/path/to/project/root*
ExecStart=*path/to/gunicorn* --workers 3 --bind unix:*/path/to/project/root*/gunicorn.sock marketplace.wsgi --preload --timeout 300

[Install]
WantedBy=multi-user.target
```

