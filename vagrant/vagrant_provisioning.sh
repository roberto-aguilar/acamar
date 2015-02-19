#!/usr/bin/env bash

# Retrieve new lists of packages
apt-get update

# Install python development packages
apt-get install -y python-setuptools python-dev

# Install pip python package manager
easy_install pip

# Install virtualenv python environment manager
pip install virtualenv

# Install Git version control system
apt-get install -y git

# Install full version of vim text editor
apt-get install -y vim

# Install PostgreSQL database
apt-get install -y postgresql libpq-dev

# Create vagrant PostgreSQL user
sudo su - postgres -c 'createuser -s vagrant'

# Create vagrant database
sudo su - postgres -c 'createdb vagrant'

# Create a virtualenv
virtualenv /vagrant/env

# Update vagrant .bashrc to enable color in promptv
sudo su - vagrant -c 'sed -i "1i force_color_prompt=yes" ~/.bashrc'

# Update vagrant .bashrc to chanage current directory to shared directory
sudo su - vagrant -c 'echo "cd /vagrant" >> ~/.bashrc'

# Update vagrant .bashrc to source virtualenv on each login of the vagrant user
sudo su - vagrant -c 'echo "source /vagrant/env/bin/activate" >> ~/.bashrc'
