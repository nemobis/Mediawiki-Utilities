"""
Prints the rev_id, characters and hash of all revisions to Willy_on_Wheels.
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd()))

import getpass
import hashlib
from mw import api

api_session = api.Session("https://en.wikipedia.org/w/api.php")

print("(EN) Wikipedia credentials...")
username = input("Username: ")
password = getpass.getpass("Password: ")
api_session.login(username, password)

revisions = api_session.deleted_revs.query(
    properties={'revid', 'content'},
    titles={'Willy on Wheels'},
    direction="newer"
)

for rev in revisions:
    print(
        "{0} ({1} chars): {2}".format(
            rev['revid'],
            len(rev.get('*', "")),
            hashlib.sha1(bytes(rev.get('*', ""), 'utf8')).hexdigest()
        )
    )
