#!/bin/bash

success_status_code=0
failure_status_code=1
coverage_under_expected_status_code=2

echo 'Deleting .pyc files'
find acamar/ -name '*.pyc' -exec rm {} \;

echo 'Running source code analyzers'
flake8 acamar/

if [ $? -eq $success_status_code ]
    then
        echo 'No source code problems found'
    else
        echo 'Source code problems found, please fix them to continue'
        exit $failure_status_code
fi

echo 'Running tests with measuring coverage'
coverage run acamar/manage.py test acamar/

if [ $? -eq $success_status_code ]
    then
        echo 'The tests ran successfully'
    else
        echo 'The tests failed, please fix them to continue'
        exit $failure_status_code
fi

echo 'Reporting coverage'
coverage report --fail-under=95

if [ $? -eq $coverage_under_expected_status_code ]
    then
        echo 'The average coverage expected was not fulfilled, please increase it at least to 95% to continue'
        exit $failure_status_code
    else
        echo 'The average coverage expected was fulfilled'
fi

echo 'All tests ran successfully, now you can make a commit'
exit $success_status_code
