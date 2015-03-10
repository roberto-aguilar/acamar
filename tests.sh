#!/bin/bash

success=0
failure=1
coverage_under_expected=2

echo 'Deleting .pyc files'
find acamar/ -name '*.pyc' -exec rm {} \;

echo 'Running source code analyzers'
flake8 acamar/

if [ $? -eq $success ]
    then
        echo 'No source code problems found'
    else
        echo 'Source code problems found, please fix them to continue'
        exit $failure
fi

echo 'Running tests with measuring coverage'
coverage run acamar/manage.py test acamar/

if [ $? -eq $success ]
    then
        echo 'The tests ran successfully'
    else
        echo 'The tests failed, please fix them to continue'
        exit $failure
fi

echo 'Reporting coverage'
coverage report --fail-under=95

if [ $? -eq $coverage_under_expected ]
    then
        echo 'The average coverage expected was not fulfilled, please increase it at least to 95% to continue'
        exit $failure
    else
        echo 'The average coverage expected was fulfilled'
fi

exit $success
