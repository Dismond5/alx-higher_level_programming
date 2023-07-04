#!/usr/bin/python3
"""
script that takes in a URL and email, sents a POST request to
the passed URL with emain as a parameter."""

import sys
import requests

if __name__ = "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {
            "email": email
            }
    reponse = request.post(url, data=payload)
    print(response.tct)
