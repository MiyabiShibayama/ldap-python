#!/usr/bin/env python
#-*-coding: utf-8-*-

# miyabi2アカウントをldapaddで追加する

from libldap import LDAP
from libldap import LDAP_SCOPE_SUB

URI = 'ldap://ldap.exmaple.jp'
BIND_DN = 'cn=master,dc=example'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'


def ldapaddmiyabi(uri,bind_dn,bind_pass,gidNumber,description):
    ld = LDAP(URI)
    ld.bind(BIND_DN,BIND_PASS)
    result = ld.add('cn=miyabi2,ou=Users,dc=example,dc=jp',
            [('objectClass',['top','posixAccount']),
             ('cn',['miyabi2']),
             ('gidNumber',['1001']),
             ('description',['Test6'])
               ])
    return result

print('追加されました')

