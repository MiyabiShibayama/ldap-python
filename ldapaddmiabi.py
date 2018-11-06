# !/usr/bin/env python
# -*-coding: utf-8-*-

# miyabi2アカウントをldapaddで追加する

from libldap import LDAP


URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'


def main():
    print("call main")
    result = ldapaddmiyabi()
    print(result)


def ldapaddmiyabi():
    print("call ldapaddmiyabi")
    ld = LDAP(URI)
    ld.bind(BIND_DN, BIND_PASS)
    result = ld.add('uid=miyabi2,ou=Users,dc=example, dc=jp', [
     ('objectClass', ['top', 'person', 'inetOrgPerson', 'posixAccount']),
     ('uid', ['miyabi2']),
     ('cn', ['miyabi2']),
     ('sn', ['shibayama']),
     ('givenName', ['miyabi2']),
     ('uidNumber', ['1001']),
     ('gidNumber', ['1001']),
     ('homeDirectory', ['/home/miyabi2']),
     ('description', ['Test6']),
     ('loginShell', ['/bin/bash']),
     ('userPassword', ['miyabi123'])
     ])
    return result


main()
