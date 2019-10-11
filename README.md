# Django Marketplace
A marketplace coding exercise with Django.

## Dependencies
Whether setting up in a production environment or locally for development, follow these steps to install the necessary packages.

1) Install pipenv if you don't already have it.
2) In a terminal, navigate to the root directory and run the following to set up the project's virtual environment
> pipenv install

## Usage
### Running the server
In a terminal at the project's root directory enter
> pipenv shell

to enter the virtual environment and then run the Django server with
> python manage.py runserver

### Interacting with the site
Users are able to view items for sale in various categories (links in the navbar). To post items users will need to sign up and log in. Items can be edited or removed by the user that has posted them.

### Interacting with the API
#### Authentication
The API uses basic auth. If you're using Curl with an endpoint that requires authentication you'd provide your credentials as shown by the following example:
> curl -X "DELETE" --user username:password  http://localhost:8000/api/items/8/

#### Endpoints

`/api/categories/`
- **GET**: List the categories available in the system.
`/api/categories/:category_id/`
- **GET**: Retrieve the details of a single category.

`/api/items/`
- **GET**: List the items available in the system.
- **POST**: Create a new item. _Requires authentication_

`/api/items/:item_id/`
- **PUT**: Set all fields of an item. _Requires authentication as the author of the item_
- **PATCH**: Allows for providing values for only the fields to set, and leaving out others that will remain unchanged. _Requires authentication as the author of the item_
- **DELETE**: Deletes an item from the marketplace. _Requires authentication as the author of the item_

## Deploying
This project can be run in production with Gunicorn. The following is an example systemctl unit that can be used to run the Gunicorn server as a socket. For additional security move the sensitive environment variables into a separate text file with restricted read permissions. Replace all fields surrounded by underscores with the system specific values (also removing the underscores).

```
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
```
