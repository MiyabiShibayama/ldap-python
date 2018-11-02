#ldapsearch1.py              

class ldapsearch1:
    from libldap import LDAP
    from libldap import LDAP_SCOPE_SUB
    from pprint import pprint

    URI = 'ldap://ldap.example.jp'
    BIND_DN  = 'cn=master,dc=example,dc=jp'
    BASE_DN ='dc=example,dc=jp'
    BIND_PASS ='secret123'

    def ldapsearch_ou(uri,bind_dn,base_dn,bind_pass):
        ld = LDAP(uri)
        with LDAP(uri) as ld:
            ld.bind(bind_dn,bind_pass)
            result = ld.search(base_dn,LDAP_SCOPE_CHILD,'(|(cn=miyabi)(dc=jp))')


print('search1')
