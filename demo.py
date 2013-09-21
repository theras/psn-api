from psn import Psn


psn = Psn()
jid = psn.jid('Luumina')
print psn.profile(jid[0])