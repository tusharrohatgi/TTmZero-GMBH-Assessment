"""
Description :

This is an end-point for GET request which takes arguments as Request parameters.
This end-point has headers with it and tells me the origin and URL as well.


"""

import requests



def get_response(params):
    for key , value in params.items():
        response = requests.get("https://httpbin.org/get?" + str(key) + "="+ str(value))
    return str(response.content)

def test1():
    params = {"args1":[1,2,3]}
    for key , value in params.items():
        assert str(value) in get_response(params)
        assert str(key) in get_response(params)


def test2():
    params = {"args2": "Value in string"}
    for key, value in params.items():
        assert str(value) in get_response(params)
        assert str(key) in get_response(params)

def test3():
    params = {"a": 0000}
    for key, value in params.items():
        assert str(value) in get_response(params)
        assert str(key) in get_response(params)
