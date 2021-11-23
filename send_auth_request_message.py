#!/usr/bin/env python
import csv
import sys
import duo_client

argv_iter = iter(sys.argv[1:])
def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)

# Configuration and information about objects to create.
admin_api = duo_client.Auth(
    ikey=get_next_arg('Auth API integration key ("DI..."): '),
    skey=get_next_arg('integration secret key: '),
    host=get_next_arg('API hostname ("api-....duosecurity.com"): '),   
)

username=get_next_arg('username : '),   

# Retrieve user info from API:
response = admin_api.auth(username=username,factor="push",device="auto", pushinfo="from=Incident%20Response%20Team&domain=example.com" )
print(response)