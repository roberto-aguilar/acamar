#!/usr/bin/env bash

# Store vagrant shared directory
SHARED_DIRECTORY=/vagrant

# Retrieve new lists of packages
apt-get update

# Install python development packages
apt-get install -y python-setuptools python-dev

# Install django-extensions requirements
apt-get install -y graphviz-dev graphviz pkg-config

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

# Install python dependencies
pip install -r /vagrant/requirements/development.txt

# Run django migrations
sudo su - vagrant -c "python $SHARED_DIRECTORY/acamar/manage.py migrate"

# Load database fixture
sudo su - vagrant -c "python $SHARED_DIRECTORY/acamar/manage.py loaddata $SHARED_DIRECTORY/vagrant/db.json"

# Update vagrant .bashrc to enable color in promptv
sudo su - vagrant -c 'sed -i "1i force_color_prompt=yes" ~/.bashrc'

# Update vagrant .bashrc to chanage current directory to acamar project
sudo su - vagrant -c "echo 'cd $SHARED_DIRECTORY/acamar' >> ~/.bashrc"
