#!/bin/bash

success_status_code=0
failure_status_code=1
coverage_under_expected_status_code=2

red_color='\033[0;31m'
green_color='\033[0;32m'
no_color='\033[0m'

echo 'Deleting .pyc files...'
find acamar/ -name '*.pyc' -exec rm {} \;

echo 'Running source code analyzers...'
flake8 acamar/

if [ $? -eq $success_status_code ]
    then
        echo "${green_color}No source code problems found${no_color}"
    else
        echo "${red_color}Source code problems found, please fix them to continue${no_color}"
        exit $failure_status_code
fi

echo "Running tests with coverage's measuring"
coverage run acamar/manage.py test acamar/

if [ $? -eq $success_status_code ]
    then
        echo "${green_color}The tests ran successfully${no_color}"
    else
        echo "${red_color}The tests failed, please fix them to continue${no_color}"
        exit $failure_status_code
fi

echo 'Reporting coverage...'
coverage report --fail-under=95 -m

if [ $? -eq $coverage_under_expected_status_code ]
    then
        echo "${red_color}The coverage average expected was not fulfilled, please increase it at least to 95% to continue${no_color}"
        exit $failure_status_code
    else
        echo "${green_color}The coverage average expected was fulfilled${no_color}"
fi

echo "${green_color}All tests ran successfully, now you can make a commit${red_color}"
exit $success_status_code
