from telnetlib import Telnet
with Telnet('10.124.206.68', 23) as tn:
    tn.interact()