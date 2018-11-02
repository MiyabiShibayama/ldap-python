#ldapadd2.py

from libldap import LDAP
from pprint import pprint

URI='ldap://ldap.example.co.jp'
BASE_DN='dc=example,dc=jp'
BIND_DN='cn=master,dc=example,dc=jp'
BIND_PASS='secret123'

ld=LDAP('ldap://ldap.example.co.jp')
ld.bind('cn=master,dc=example,dc=jp,bind_pass=secret123')
ld.add('cn=group1,ou=Groups,dc=example,dc=jp'[
    ('objectClass',['top','posixGroup']),
    ('cn',[group1]),('gitNumber',[1000]),
    ('description',['Test Group 1'])
    ])

print('add2')
