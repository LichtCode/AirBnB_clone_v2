#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
# 1. Install Nginx if it not already installed
# 2. Create the folder /data/ if it doesn’t already exist
# 3. Create the folder /data/web_static/ if it doesn’t already exist
# 4. Create the folder /data/web_static/releases/ if it doesn’t already exist
# 5. Create the folder /data/web_static/shared/ if it doesn’t already exist
# 6. Create the folder /data/web_static/releases/test/ if it doesn’t already exist
# 7. Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
# 8. Create a symbolic link /data/web_static/current linked to the
# /data/web_static/releases/test/ folder. If the symbolic link already exists,
# it should be deleted and recreated every time the script is ran.
# Give ownership of the /data/ folder to the ubuntu user AND group
# (you can assume this user and group exist).
# This should be recursive; everything inside
# should be created/owned by this user/group.
# 9. Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
# Don’t forget to restart Nginx after updating the configuration:
# Use alias inside your Nginx configuration

# 0. update the machine
sudo apt-get update

# 1. install nginx if it not installed
sudo apt-get -y install nginx
#  sudo ufw allow 'Nginx HTTP'

# 2 - 6. create requiured directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# 7. create a random html page

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"| sudo tee /data/web_static/releases/test/index.html

# 8. creating a symbolic lnk
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# granting ownership to userand group


sudo chown -R ubuntu:ubuntu /data/

# backup nginx default

#. serving the content on the serverwith nginx

sudo sed -i '/listen 80 default_server/a \\n\tlocation /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# test nginx
sudo nginx -t

#  restart nginx
sudo service nginx restart
