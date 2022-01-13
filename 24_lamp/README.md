# how-to :: PROVISION A DIGITALOCEAN DROPLET AND INSTALL UBUNTU 20.04.3 AND APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time. 

### Estimated Time Cost: 1 hour

### Prerequisites:

- A DigitalOcean account with a payment method
- A computer with internet access

## Instructions

### Creating a Droplet
1. Navigate to the Projects panel on your DigitalOcean dashboard.
2. Click the green Create button at the top of the page and click Droplets.
3. We recommend using Ubuntu 20.04 (LTS) with the basic plan and a regular intel CPU with an SSD. This should cost about $5 per month. You won't need block storage. Select the datacenter region closest to you. Select "SSH keys" for authentication method.
4. Set up SSH keys on your computer. Your keys will be automatically stored in your `~/.ssh` directory.
```
$ ssh-keygen
```
5. Copy and paste the contents of the `id_rsa.pub` file (NOT your private key!!) into the provided field and give your SSH key a descriptive name.
6. Create your droplet! It might take a few minutes for everything to get set up.

### Initial Droplet Setup
Let's set up a normal user account.
1. At first, there's only one account on your droplet, `root`. Log in as the root user.
```
$ ssh root@your_server_ip
```
2. Add a new user. Replace `my_username` with a username of your choice.
```
# adduser my_username
```
3. Give your new user account sudo privileges. This allows your user account to run administrator commands without having to log in as root.
```
# usermod -aG sudo my_username
```
4. Set up a basic firewall to block all non-SSH connections.
```
# ufw allow OpenSSH
# ufw enable
# ufw status
```
You should see the following output:
```
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
OpenSSH (v6)               ALLOW       Anywhere (v6)
```
5. Copy your SSH keys to your user account.
```
# rsync --archive --chown=my_username:my_username ~/.ssh /home/my_username
```
6. Open up a new terminal session (don't log out of root yet!) and try to log into your user account.
```
$ ssh my_username@your_server_ip
```
7. If that works, you can safely exit your root account. For everyday use, you should use your user account, NOT root.

### Installing Apache
1. Update the local package index.
```
$ sudo apt update
```
2. Install `apache2`. Apache will start automatically upon installation.
```
$ sudo apt install apache2
```
3. Adjust your firewall to include connections for Apache.
```
$ sudo ufw allow 'Apache'
$ sudo ufw status
```
You should see the following output:
```
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere                  
Apache                     ALLOW       Anywhere                
OpenSSH (v6)               ALLOW       Anywhere (v6)             
Apache (v6)                ALLOW       Anywhere (v6)
```
4. Check your web server.
```
$ sudo systemctl status apache2
```
You should see the following output (or similar, based on your specs):
```
● apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2020-04-23 22:36:30 UTC; 20h ago
       Docs: https://httpd.apache.org/docs/2.4/
   Main PID: 29435 (apache2)
      Tasks: 55 (limit: 1137)
     Memory: 8.0M
     CGroup: /system.slice/apache2.service
             ├─29435 /usr/sbin/apache2 -k start
             ├─29437 /usr/sbin/apache2 -k start
             └─29438 /usr/sbin/apache2 -k start
```
5. Get your hostnames. You'll be able to access your web pages from those addresses.
```
$ hostname -I
```
6. View your web page by navigating to `http://your_server_ip`. You should see a default page that says "It works!" Note that HTTPS connections are not enabled by default (see [this article](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-20-04) for more information).

### Resources
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04

---

Accurate as of (last update): 2022-01-13

#### Contributors:  
Christopher Liu, pd1  
Lucas Lee, pd1  
Emma Buller, pd1  
