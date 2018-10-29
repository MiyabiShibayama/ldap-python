#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# ldapadd.py

from libldap import LDAP
from pprint import pprint

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=Master,dc=example,dc=jp'
BIND_PASS = 'secret123'

def addtestuser(uri, bind_dn, bind_pass, min_uid, max_uid):
    ldap = LDAP(uri)
    ldap.bind(bind_dn, bind_pass)
    for uid in range(min_uid, max_uid+1):
        entry_dn = 'uid=test' + str(uid) + ',ou=Users,dc=example,dc=jp'
        entry = [('objectClass', ['person', 'posixAccount']),
                 ('uid', [str(uid)]),
                 ('uidNumber', [str(uid)]),
                 ('gidNumber', [str(uid)]),
                 ('homeDirectory', ['/home/test' + str(uid)]),
                 ('cn', ['test' + str(uid)]),
                 ('sn', ['test' + str(uid)])]
        ldap.add(entry_dn, entry)

if __name__ == '__main__':
    addtestuser(URI, BIND_DN, BIND_PASS, 10, 20)

