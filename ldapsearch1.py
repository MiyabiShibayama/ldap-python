# ! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# ldapsearch1.py

from libldap import LDAP
from libldap import LDAP_SCOPE_SUB

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'


def main():
    print('main')
    search = ldapsearch_ou('ldap://ldap.example.jp', 'cn=master,dc=example',
                           'dc=example,dc=jp', 'secret123')
    print(search)


def ldapsearch_ou():
    ldap = LDAP(URI)
    ldap.bind(BIND_DN, BIND_PASS)
    result = ldap.search(BASE_DN, LDAP_SCOPE_SUB, '(|(cn=miyabi)(dc=jp))')
    return result


print('global')


main()
