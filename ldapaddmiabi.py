#!/usr/bin/env python
#-*-coding: utf-8-*-

# miyabi2アカウントをldapaddで追加する

from libldap import LDAP
from libldap import LDAP_SCOPE_SUB

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'

def main():
    print('call main')
    miyabiadd = ldapaddmiyabi()
    print('追加されました')

def ldapaddmiyabi():
    ld = LDAP(URI)
    ld.bind(BIND_DN,BIND_PASS)
    result = ld.add('cn=miyabi2,ou=Users,dc=example,dc=jp',
            [('objectClass',['top','person','inetOrgPerson','posixAccount']),
             ('uid',['miyabi']),
             ('cn',['miyabi2']),
             ('sn',['shibayama']),
             ('givenName',['miyabi']),
             ('uidNumber',['1001']),
             ('gidNumber',['1001']),
             ('homeDirectory',['/home/miyabi']),
             ('description',['Test6']),
             ('loginShell',['/bin/bash']),
             ('userPassword',['miyabi123'])
               ])
    return result

print('add')

main()

