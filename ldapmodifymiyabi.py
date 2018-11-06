# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set expandtab shiftwidth=4 :
# ldapmodifymiyabi

from libldap import LDAP
from libldap import LDAP_MOD_REPLACE

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'


def main():
    result = modifymiyabi()
    print(result)


def modifymiyabi():
    ld = LDAP(URI)
    ld.bind(BIND_DN, BIND_PASS)
    result = ld.modify(('uid=miyabi2,ou=Users,dc=example,dc=jp'), [
     ('userPassword', ['miyabi321'], LDAP_MOD_REPLACE)])
    ld.unbind()
    return result


main()
