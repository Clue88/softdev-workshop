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


### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

---

Accurate as of (last update): 2022-01-18

#### Contributors:  
Christopher Liu, pd1  
Lucas Lee, pd1  
Emma Buller, pd1  
