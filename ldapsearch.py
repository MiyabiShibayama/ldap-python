#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :

# ldapsearch.py

from libldap import LDAP
from libldap import LDAP_SCOPE_SUB
from pprint import pprint

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'


def ldapsearch_uid(uri, bind_dn, bind_pass, base_dn):
    ldap = LDAP(uri)
    ldap.bind(bind_dn, bind_pass)
    ldap.unbind()
    result = ldap.search(base_dn, LDAP_SCOPE_SUB, 'cn=miyabi', ['cn'])
    return result


def ldapsearch_gid(uri, bind_dn, bind_pass, base_dn):
    ldap = LDAP(uri)
    ldap.bind(bind_dn, bind_pass)
    ldap.unbind()
    result = ldap.search(base_dn, LDAP_SCOPE_SUB, '(uidNumber=*)', ['gidNumber'])
    return result


if __name__ == '__main__':
    result = ldapsearch_uid(uri,bind_dn,bind_pass,base_dn)
    pprint(result)
    #result = ldapsearch_gid(URI, BIND_DN, BIND_PASS, BASE_DN)
    #pprint(result)

