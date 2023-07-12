#!/bin/bash

# Install system dependencies
sudo apt-get update
sudo apt-get install -y nginx supervisor

# Stop Nginx and Supervisor services if they are running
sudo service nginx stop
sudo service supervisor stop

# Remove default Nginx configuration
sudo rm -f /etc/nginx/sites-enabled/default

# Remove default Supervisor configuration
sudo rm -f /etc/supervisor/conf.d/supervisord.conf

# Create necessary directories
sudo mkdir -p /var/log/supervisor

# Ensure necessary permissions
sudo chown -R ubuntu:ubuntu /var/log/supervisor

# Clean up any previous application files
sudo rm -rf /var/www/project/*

# Continue with other installation steps as needed
# For example, cloning your application code from a Git repository,
# installing Python packages with pip, etc.

exit 0
