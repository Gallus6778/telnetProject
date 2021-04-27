import telnetlib2 as telnet

t = telnet.telnet()
ip='10.124.206.68'


# ----------------------------------------------------------------------------
# from telnetlib import Telnet
# with Telnet(ip, 23) as tn:
#     tn.interact()
# ----------------------------------------------------------------------------

# help(t)
# print(type(t.login(ip, username='ANICET', password='toor',p=23,timeout=5)))
# try:

t.login(ip, username='CHATBO', password='1234567890',p=23,timeout=5)
# t.telnet()
print('connexion etablie ...')

        # print("Connexion etablie")
    # else:
        # print("Echec de connexion")
# except:
#     print("une exception est produite")

# output1=t.execute('echo ala_is_king')
# print(output1)
# output2=t.execute('cd / && ls')
# print(output2)
# t.close()
