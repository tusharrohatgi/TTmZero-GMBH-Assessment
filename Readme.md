Requirements for Python 3.7 :

pytest
allure_pytest
requests
allure-python-commons

Executing test : pytest http_test.py

Git location : https://github.com/tusharrohatgi/Assignment-TTMZero

Generating and Getting Allure report
pytest --alluredir=./report http_test.py
allure serve ./report/

