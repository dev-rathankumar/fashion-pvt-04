# fashionProject-private

```bash
sudo apt update && apt upgrade -y
```
```bash
sudo apt install python3-pip python3-dev ufw nginx
```
## create a user and give him sudo permission
```bash
adduser altocan
```
```bash
adduser altocan sudo
```
```bash
exit
```
## ssh into server as a user
```bash
ssh altocan@IPADDRESS
```
```bash
sudo ufw allow ssh
```
```bash
sudo ufw enable
```
```bash
sudo apt update
```
```bash
sudo apt install python3-pip python3-dev nginx
```
```bash
sudo pip3 install virtualenv
```
```bash
mkdir ~/fashiondir
```
```bash
cd ~/fashiondir
```
```bash
git clone https://github.com/dev-rathankumar/fashion-pvt-04.git .
```
```bash
virtualenv env
```
```bash
source env/bin/activate
```
## Install postgres
```bash
sudo apt-get install postgresql postgresql-contrib
```
```bash
sudo systemctl start postgresql.service
```
```bash
sudo systemctl enable postgresql.service
```
```bash
sudo systemctl status postgresql.service
```
## Configure postgres
```bash
sudo passwd postgres
```
```bash
sudo su - postgres
```
```bash
psql -d postgres -c "ALTER USER postgres WITH PASSWORD 'Linode@2021';"
```
```bash
psql postgres
```
```bash
CREATE DATABASE fashion_db;
```
```bash
exit
```
```bash
exit
```
## setup .env file
```bash
sudo nano .env  ### add the environment variables with postgres db name and password
```
```bash
sudo nano fashion_main/settings.py   ### add IP address in allowed host
```
```bash
pip install -r requirements.txt
```
```bash
deactivate
```
```bash
source env/bin/activate
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
## allow port 8000
```bash
sudo ufw enable
```
```bash
sudo ufw allow 8000
```
```bash
sudo ufw status
```
## run the server
```bash
python manage.py runserver 0.0.0.0:8000
```
```bash
Press CTRL + C
```
```bash
sudo apt install gunicorn
```
```bash
gunicorn --bind 0.0.0.0:8000 fashion_main.wsgi
```
```bash
exit
```
## Configuring gunicorn

```python
sudo nano /etc/systemd/system/gunicorn.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

```python
sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=altocan
Group=www-data
WorkingDirectory=/home/altocan/fashiondir
ExecStart=/home/altocan/fashiondir/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          fashion_main.wsgi:application

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

## Configuring Nginx as a reverse proxy
```python
sudo nano /etc/nginx/sites-available/fashion_main

server {
    listen 80;
    server_name altocanp1.website;

    location ~ ^/\.well-known {
        root /home/altocan/fashiondir;
        allow all;
    }

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/altocan/fashiondir;
    }
    location /media/ {
        root /home/altocan/fashiondir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
```bash
sudo ln -s /etc/nginx/sites-available/fashion_main /etc/nginx/sites-enabled/
```
```bash
cd /etc/nginx/sites-enabled/
sudo rm default
```

```bash
sudo ufw allow 80
sudo ufw allow 'Nginx Full'
sudo ufw allow 586
sudo ufw deny 8000
```
```python
sudo nano fashiondir/fashion_main/settings.py
# Add the domain name into allowed host
sudo systemctl restart nginx
sudo systemctl restart gunicorn
```
