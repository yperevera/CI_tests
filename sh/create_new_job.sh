#!/bin/bash

echo '#### Create Virtual Environment ####'
VIRTUAL_ENV_NAME='virtual-environment'
virtualenv $VIRTUAL_ENV_NAME


echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/Scripts/activate


echo '#### Install requirements ####'
pip install -r ./requirements.txt


echo '#### Run tests ####'
py.test --alluredir=../allure-results ./test_main_page.py  

 
echo '### deactivate virtual environment ###'
deactivate