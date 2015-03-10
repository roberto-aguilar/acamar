#!/bin/bash

success_status_code=0
failure_status_code=1
coverage_under_expected_status_code=2

echo 'Deleting .pyc files...'
find acamar/ -name '*.pyc' -exec rm {} \;

echo 'Running source code analyzers...'
flake8 acamar/

if [ $? -eq $success_status_code ]
    then
        echo 'No source code problems found'
    else
        echo 'Source code problems found, please fix them to continue'
        exit $failure_status_code
fi

echo 'Pulling out all strings marked for translation...'
python acamar/manage.py makemessages -l es

echo 'Searching for fuzzy ids in translation files...'
fuzzy_ocurrences=$(find acamar/ -name 'django.po' -exec grep '#, fuzzy' {} \; | wc -l)

if [ $fuzzy_ocurrences -gt 0 ]
    then
        echo 'Translation files with fuzzy ids found, please fix then to continue'
        exit $failure_status_code
    else
        echo 'No fuzzy ids found in translation files'
fi

echo 'Searching for orphans ids in translation files...'
orphan_ids_ocurrences=$(find acamar/ -name 'django.po' -exec grep '#~' {} \; | wc -l)

if [ $orphan_ids_ocurrences -gt 0 ]
    then
        echo 'Translation files with orphan ids found, please fix them to continue'
        exit $failure_status_code
    else
        echo 'No orphan ids found in translation files'
        echo 'Compiling translation files...'
        python acamar/manage.py compilemessages
        echo 'The translation files compiled successfully, make sure to add them to the version control system stage'
fi

echo 'Running tests with measuring coverage...'
coverage run acamar/manage.py test acamar/

if [ $? -eq $success_status_code ]
    then
        echo 'The tests ran successfully'
    else
        echo 'The tests failed, please fix them to continue'
        exit $failure_status_code
fi

echo 'Reporting coverage...'
coverage report --fail-under=95

if [ $? -eq $coverage_under_expected_status_code ]
    then
        echo 'The coverage average expected was not fulfilled, please increase it at least to 95% to continue'
        exit $failure_status_code
    else
        echo 'The coverage average expected was fulfilled'
fi

echo 'All tests ran successfully, now you can make a commit'
exit $success_status_code
