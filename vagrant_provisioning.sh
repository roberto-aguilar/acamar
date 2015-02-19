#!/usr/bin/env bash

# Retrieve new lists of packages
apt-get update

# Install python development packages
apt-get install -y python-setuptools

# Install pip python package manager
easy_install pip

# Install virtualenv python environment manager
pip install virtualenv

# Install Git version control system
apt-get install -y git

# Install full version of vim text editor
apt-get install -y vim

# Install PostgreSQL database
apt-get install -y postgresql

# Store the vagrant shared directory location and move to it
SHARED_DIRECTORY=/vagrant
cd $SHARED_DIRECTORY

# Create a virtualenv
virtualenv env

# Change current user to vagrant
sudo -i -u vagrant

# Update .bashrc to source virtualenv on each login of the vagrant user
echo "source $SHARED_DIRECTORY/env/bin/activate" >> ~/.bashrc
