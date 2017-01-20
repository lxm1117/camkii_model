import numpy as np
total_ca=4222

ca_hz=np.transpose(np.loadtxt('mol_ca_2hz.txt'))
filename='cainput_2hz.txt'

caspk=ca_hz[1][1:]-ca_hz[1][0:-1]
fhz=open(filename,'w')

for i in range(0,len(ca_hz[0])-1):
	if caspk[i]>0 and ca_hz[1][i]<total_ca:
		line='cmd @ '+str(ca_hz[0][i])+' pointsource ca ' + str(int(caspk[i]))+' 1 0 0 998\n'
		fhz.write(line)
	if ca_hz[1][i]>total_ca:	
		break
	
	
fhz.close()
