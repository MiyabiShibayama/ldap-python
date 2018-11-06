# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# ldapsearchmiyabi.py


from libldap import LDAP
from libldap import LDAP_SCOPE_SUB

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=hp'
BIND_PASS = 'secret123'


def main():
    print('call main')
    result = ldapsearchmiyabi()
    print(result)


def ldapsearchmiyabi():
    ld = LDAP(URI)
    ld.bind(BIND_DN, BIND_PASS)
    result = ld.search('uid=miyabi2,ou=Users,dc=example,dc=jp',
                       LDAP_SCOPE_SUB, '(&(uid=miyabi2)(ou=Users))')
    return result


print('global')


main()
