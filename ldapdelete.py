# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# ldapdelete.py

from libldap import LDAP


URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn =master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'


def main():
    print('call main')
    kekka = delitem('ldap://ldap.example.jp', 'cn=master,dc=example,dc=jp',
                    'dc=example,dc=jp', 'secretr123')
    if kekka == 0:
        print('成功')
    else:
        print('失敗')


def delitem(uri, bind_dn, base_dn, bind_pass):
    print('call delitem')
    ld = LDAP(URI)
    ld.bind(BIND_DN, BIND_PASS)
    result = ld.delitem(['gidNumber'])

    result = 1
    return result


print('global')


main()
