# 1 fA=1e-15 C/s ~ 3.12 ions/ms
import numpy as np
#30 uM in 1*1*2 volume
#total_ca=36120
# 30 uM in 0.75**2*1.5
#total_ca=15238



#tstop=575	#8hz
tstop=465	#10hz
#tstop=855	#5hz

ca_hz=np.transpose(np.loadtxt('mol_ca_trial1/mol_ca_10hz.txt.8ch'))
caspk=ca_hz[1][1:]-ca_hz[1][0:-1]
total_ca=0

for i in range(0,len(ca_hz[0])-1):
	if caspk[i]>0 and ca_hz[0][i]<=tstop:
		total_ca+=caspk[i]
	if ca_hz[0][i]>tstop:	
		break
print total_ca	


# 10hz: tstop=465 total_ca=48433
# 5hz: tstop=865  total_ca=41533
# 8hz: tstop=575  total_ca=45861
# 16hz:tstop=315.26	total_ca=41810	
# 10hz 8ch: tstop=465, total_ca=18272
# 5hz 8ch: tstop=855, total_ca=23672
