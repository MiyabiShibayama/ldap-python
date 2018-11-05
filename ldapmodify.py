#ldapmodify.py

from libldap import LDAP
from libldap import LDAP_MOD_ADD
from libldap import LDAP_MOD_REPLACE

URI = 'ldap://ldap.example.jp'
BIND_DN = 'cn=master,dc=example,dc=jp'
BASE_DN ='dc=example,dc=jp'
BIND_PASS ='secret123'

def main():
    print ('call main')
    kekka = ldapmodify('ldap://ldap.exzmple.jp','cn=master,dc=example','dc=xample,dc=jp','secret123')
    print('modify')

def ldapmodify(uri,bind_dn,base_dn,bind_pass):
    ld = LDAP('ldap://ldap.exmaple.jp')
    with LDAP(uri) as ld:
        ld.bind(bind_dn,bind_pass)
        for cn in range(min_cn,max_cn+1):
            entry_dn = 'cn=sampleA' + str(cn) + 'ou=sampleB' + str(ou) + 'dc=example,dc=jp'
        for ou in range(min_ou,max_ou+1):
            entry_dn = 'cn=sampleA' + str(cn) + 'ou=sampleB' + str(ou) + 'dc=example,dc=jp'
        result =  ld.modify('cn=sampleA,ou=sampleB,dc=example,dc=jp',['entry_dn',(['user1'], LDAP_MOD_ADD), ('description', ['Test Group One'], LDAP_MOD_REPLACE)])
   
    return result
    
print('global')

main()
