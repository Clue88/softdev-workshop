# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time. 

### Estimated Time Cost: 1 hour

### Prerequisites:

- A DigitalOcean droplet with Ubuntu 20.04.3 and Apache2 installed

## Instructions

### Creating a Flask App
1. Install and enable WSGI.
```
$ sudo apt-get install libapache2-mod-wsgi python-dev
$ sudo a2enmod wsgi
```
2. Move to the `/var/www` directory.
```
$ cd /var/www
```
3. Clone your app. Or, write a basic Flask app for testing.
```
$ sudo git clone https://github.com/path/to/your/repo.git
```
4. Install pip.
```
$ sudo apt-get install python3-pip
```
5. Create a new virtual environment.
```
$ cd your_repo
$ sudo python3 -m venv env
```
6. Change the owner of your virtual environment to your regular user.
```
$ sudo chown -R my_username:my_username env
```
7. Install your dependencies if necessary.
```
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
```
8. Test your app.
```
(env) $ python3 app/__init__.py
```
You should see your app running on `localhost:5000`.
9. Configure a new virtual host. Note: you can use any text editor (nano, etc.) in place of vim.
```
(env) $ deactivate
$ sudo vim /etc/apache2/sites-available/your_app_name.conf
```
10. Paste the following template, replacing the placeholder text as necessary. For `your_app_python_dir`, include the path to the directory that includes your app's Python files and the `static` and `template` directories (likely `your_app_dir_name/app`).
```
<VirtualHost *:80>
		ServerName YOUR_IP_ADDRESS
		ServerAdmin my_username@YOUR_IP_ADDRESS
		WSGIScriptAlias / /var/www/your_app_dir_name/your_app_name.wsgi
		<Directory /var/www/your_app_python_dir/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/your_app_python_dir/static
		<Directory /var/www/your_app_python_dir/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Save and close the file. For vim users, type `:wq`.
11. Enable the virtual host.
```
$ sudo a2ensite your_app_name
```
12. Create a .wsgi file.
```
$ cd /var/www/your_app_dir_name
$ sudo vim your_app_name.wsgi
```
Paste the following template, replacing the placeholders, and save and close the file.
```python
#!/usr/bin/python
import sys
import logging
from os import urandom

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/your_app_dir_name/")

from your_app_python_dir import app as application
application.secret_key = urandom(32)
```
13. Restart apache.
```
sudo service apache2 restart
```
You may see a warning message like this:
```
Could not reliably determine the VPS's fully qualified domain name, using 127.0.0.1 for ServerName
```
This is okay; you'll still able to access your virtual host without further issues.
14. Test your app by going to `YOUR_IP_ADDRESS:5000` in a web browser.

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

---

Accurate as of (last update): 2022-01-19

#### Contributors:  
Christopher Liu, pd1  
Lucas Lee, pd1  
Emma Buller, pd1  
