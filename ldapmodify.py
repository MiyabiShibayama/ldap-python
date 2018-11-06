# ldapmodify.py


from libldap import LDAP
from libldap import LDAP_MOD_ADD
from libldap import LDAP_MOD_REPLACE


URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN = 'dc=example,dc=jp'
BIND_PASS = 'secret123'


def main():
    print('call main')
    kekka = ldapmodify()
    print(kekka)


def ldapmodify():
    ld = LDAP(URI)
    with LDAP(URI) as ld:
        ld.bind(BIND_DN, BIND_PASS)
        entry_dn = ('cn=sampleA' + str('cn') + 'ou=sampleB' +
                    str('ou') + ',dc=example,dc=jp')
        entry = ('cn=sampleA,ou=sampleB,dc=example,dc=jp', [
                ('entry_dn', (['user1'], LDAP_MOD_ADD),
                 ('description', ['Test Group One'], LDAP_MOD_REPLACE),
                 ('uid', [str('ou')]),
                 ('uidNumber', [str('ou')]),
                 ('gidNumber', [str('ou')]),
                 ('homeDirectory', ['/home/test' + str('ou')]),
                 ('cn', ['test' + str('ou')]),
                 ('sn', ['test' + str('ou')]),
                 ('userPassword', ['secret123'])
                 )])
        result = (entry_dn, entry)
        return result


print('global')


main()
