#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

#まだ途中

# ldapdeletemiyabi.py

from libldap import LDAP

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'

def main():
    result = delmiyabi2()
    print = ('result')

def delmiyabi2():
    ld = LDAP(URI)
    ld.bind(BIND_DN,BIND_PASS)
    result = ld.delete('uid=miyabi2,ou=Users,dc=example,dc=jp',
            [('objectClass',['top','person','inetOrgPerson','posixAccount']),
             ('uid',['miyabi2']),
             ('cn',['miyabi2']),
             ('sn',['shibayama']),
             ('givenName',['miyabi2']),
             ('uidNumber',['1001']),
             ('gidNumber',['1001']),
             ('homeDirectry',['/home/miyabi2']),
             ('description',['Test6']),
             ('loginShell',['/bin/bash']),
             ('userPassword',['miyabi123'])
               ])
    return result

main()

