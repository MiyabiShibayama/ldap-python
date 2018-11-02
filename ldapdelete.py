#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# ldapdelete.py

from libldap import LDAP
from libldap import LDAP_SCOPE_SUB
from pprint import pprint

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn =master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'

def main(uri,bind_dn,base_dn,bind_pass):
    print('call main')

def delitem(uri, bind_dn, base_dn, bind_pass):
    ldap = LDAP(uri)
    ldap.bind(bind_dn,bind_pass)
    result = ldap.search(base_dn,LDAP_SCOPE_SUB,
                         ['gidNumber'])
    print('gidNumber{}を消去しました'.format(uri,bind_dn,base_dn,bind_pass))

    return result

main('uri','bind_dn','base_dn','bind_pass')
