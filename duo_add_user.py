#!/usr/bin/python
import pprint
import sys
import duo_client

argv_iter = iter(sys.argv[1:])
def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)

# Configuration and information about objects to create.
admin_api = duo_client.Admin(
    ikey=get_next_arg('Admin API integration key ("DI..."): '),
    skey=get_next_arg('integration secret key: '),
    host=get_next_arg('API hostname ("api-....duosecurity.com"): '),
)

username = get_next_arg('user login name: ')
realname = get_next_arg('user full name: ')

# Create and return a new user object.
user = admin_api.add_user(
    username=username,
    realname=realname,
)
print('Created user:')
pprint.pprint(user)
