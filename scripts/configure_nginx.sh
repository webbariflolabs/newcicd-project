#!/bin/bash

set -e

# Remove default Nginx configuration
sudo rm -f /etc/nginx/sites-enabled/default

# Create a new Nginx configuration file
sudo cat >/etc/nginx/sites-available/myapp <<EOL
server {
    listen 80;
    server_name 18.176.61.100;

    location / {
        proxy_pass http://127.0.0.1:8000;
        include proxy_params;
        proxy_pass http://unix:/project/app.sock;
    }

    location /static/ {
        alias /home/ubuntu/project/static/;
    }
}
EOL

# Enable the new Nginx configuration
sudo ln -sf /etc/nginx/sites-available/barifloapp /etc/nginx/sites-enabled/barifloapp

# Test Nginx configuration
sudo nginx -t

# Restart Nginx service
sudo service nginx restart

exit 0
