#!/usr/bin/env bash

# Store vagrant shared directory for reference
SHARED_DIRECTORY=/vagrant

# Store project directory for reference
PROJECT_DIRECTORY=$SHARED_DIRECTORY/acamar

echo 'Resynchronizing package indexes'
apt-get update > /dev/null

echo 'Installing python development packages'
apt-get install -y python-setuptools python-dev > /dev/null

echo 'Installing Django extensions dependencies'
apt-get install -y graphviz-dev graphviz pkg-config > /dev/null

echo 'Installing Django translation tools'
apt-get install -y gettext

echo 'Installing pip python package manager'
easy_install pip > /dev/null

echo 'Installing Git version control system'
apt-get install -y git > /dev/null

echo 'Installing full version of vim text editor'
apt-get install -y vim > /dev/null

echo 'Installing PostgreSQL database'
apt-get install -y postgresql libpq-dev > /dev/null

echo 'Creating vagrant PostgreSQL user'
sudo su - postgres -c 'createuser -s vagrant'

echo 'Creating vagrant database'
sudo su - postgres -c 'createdb vagrant'

echo 'Installing python project dependencies (requirements file)'
pip install -r /vagrant/requirements/development.txt > /dev/null

# The following commands fix flake8 bugs outside of a virtualenv
sudo pip install --upgrade setuptools > /dev/null

echo 'Running project migration files'
sudo su - vagrant -c "python $PROJECT_DIRECTORY/manage.py migrate" > /dev/null

echo 'Loading database fixture'
sudo su - vagrant -c "python $PROJECT_DIRECTORY/manage.py loaddata $SHARED_DIRECTORY/vagrant/db.json" > /dev/null

echo 'Prepending .bashrc_additions file to guest operating system .bashrc'
sudo su - vagrant -c 'sed -i "1i source ~/.bashrc_additions" ~/.bashrc'
