# ldapadd2.py


from libldap import LDAP


URI = 'ldap://ldap.example.jp'
BASE_DN = 'dc=example,dc=jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BIND_PASS = 'secret123'

ld = LDAP(URI)
ld.bind(BIND_DN, BIND_PASS)
result = ld.add('cn=group2,ou=Groups,dc=example,dc=jp', [
  ('objectClass', ['top', 'posixGroup']),
  ('cn', ['group2']),
  ('gidNumber', ['3000']),
  ('description', ['Test Group 3'])
  ])


print(result)
