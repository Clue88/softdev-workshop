# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time. 

### Estimated Time Cost: 1 hour

### Prerequisites:

- A DigitalOcean droplet with Ubuntu 20.04.3 and Apache2 installed
- A Flask app with the following file structure (placeholder names will be used throughout the rest of this how-to):

```
APP_NAME  
├── APP_SCRIPTS  
    ├── static  
    ├── templates  
    └── __init__.py  
└── requirements.txt  
```

## Instructions

### Creating a Flask App
1. Install and enable WSGI. When you deploy a new app, you won't need to install the system dependencies again.
```
$ sudo apt-get install libapache2-mod-wsgi-py3 python-dev
$ sudo a2enmod wsgi
```
2. Install your app.
```
$ cd /var/www
$ sudo git clone REPO_CLONE_LINK
$ sudo apt-get install python3-pip
$ cd APP_NAME
$ sudo python3 -m venv env
$ source env/bin/activate
(env) $ sudo pip3 install -r requirements.txt
```
3. Test your app.
```
(env) $ sudo python3 app/__init__.py
```
You should see your app running on `127.0.0.1:5000`. Shut down the app for now.
```
(env) $ deactivate
```
4. Configure your virtual host. Note: you can use any text editor (nano, etc.) in place of vim.
```
$ sudo vim /etc/apache2/sites-available/APP_NAME.conf
```
Paste the following template in the `.conf` file:
```
<VirtualHost *:80>
    ServerName DROPLET_IP_ADDRESS
    ServerAdmin USERNAME@DROPLET_IP_ADDRESS
    WSGIScriptAlias / /var/www/APP_NAME/APP_NAME.wsgi
    <Directory /var/www/APP_NAME/APP_SCRIPTS/>
        Order allow,deny
	Allow from all
    </Directory>
    Alias /static /var/www/APP_NAME/APP_SCRIPTS/static
    <Directory /var/www/APP_NAME/APP_SCRIPTS/static/>
        Order allow,deny
	Allow from all
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Note: In order to deploy multiple apps, you won't be able to deploy both at the top-level route. You can change the `WSGIScriptAlias` from `/` and `/static` to `APP_NAME` and `APP_NAME/static`. [Include part about fixing Flask routes]

Save and close the file. For vim users, type `:wq`.

5. Enable the virtual host.
```
$ sudo a2ensite APP_NAME
```
To disable your site, use
```
$ sudo a2dissite APP_NAME
```
6. Create your `.wsgi` file.
```
$ cd /var/www/APP_NAME
$ sudo vim APP_NAME.wsgi
```
Paste the following template:
```python
#!/usr/bin/python
import sys
import logging
from os import urandom

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/APP_NAME/")
sys.path.insert(0,"/var/www/APP_NAME/APP_SCRIPTS/")

from APP_SCRIPTS import app as application
application.secret_key = urandom(32)
```
Save and close the `.wsgi` file.

7. Restart apache.
```
$ sudo service apache2 restart
```
You may see a warning message like this:
```
Could not reliably determine the VPS's fully qualified domain name, using 127.0.0.1 for ServerName
```
This is okay; you'll still able to access your virtual host without further issues.

8. Test your app by going to `http://DROPLET_IP_ADDRESS` in a web browser.

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

---

Accurate as of (last update): 2022-01-20

#### Contributors:  
Christopher Liu, pd1  
Lucas Lee, pd1  
Emma Buller, pd1  
