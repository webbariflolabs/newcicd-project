#!/bin/bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

# Configure Nginx
sudo cp  cp /home/ubuntu/project/nginx/nginx.conf /etc/nginx/sites-available/barifloapp
sudo ln -sf /etc/nginx/sites-available/barifloapp /etc/nginx/sites-enabled/barifloapp

# Configure Supervisor
sudo cp /home/ubuntu/project/supervisor/supervisor.conf /etc/supervisor/conf.d/bariflo.conf

# Update Supervisor configuration
sudo supervisorctl reread
sudo supervisorctl update

# Restart Nginx and Supervisor services
sudo service nginx restart
sudo service supervisor restart

exit 0
