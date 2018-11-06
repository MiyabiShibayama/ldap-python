#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# ldapadd.py


from libldap import LDAP


URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BIND_PASS = 'secret123'


def main():
    print('call main')
    kekka = addtestuser('ldap://ldap.example.jp',
                        'cn=master,dc=example,dc=jp', 'secret123',
                        10000, 10020)
    print(kekka)


def addtestuser(uri, bind_dn, bind_pass, min_uid, max_uid):
    ld = LDAP(URI)
    ld.bind(BIND_DN, BIND_PASS)
    for uid in range(min_uid, max_uid+1):
        entry_dn = 'uid=test' + str(uid) + ',ou=users,dc=example,dc=jp'
        entry = [('objectClass', ['person', 'posixAccount']),
                 ('uid', [str(uid)]),
                 ('uidNumber', [str(uid)]),
                 ('gidNumber', [str(uid)]),
                 ('homeDirectory', ['/home/test' + str(uid)]),
                 ('cn', ['test' + str(uid)]),
                 ('sn', ['test' + str(uid)]),
                 ('userPassword', ['secret123'])]
        result = ld.add(entry_dn, entry)
    return result


print('global')


main()
