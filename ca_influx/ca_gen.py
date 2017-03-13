# 1 fA=1e-15 C/s ~ 3.12 ions/ms
import numpy as np
#30 uM in 1*1*2 volume
#total_ca=36120
# 30 uM in 0.75**2*1.5
total_ca=0

tadjust=120	#delay input by 120ms
tstop=855	# 5hz 8ch
#tstop=465	# 10hz 8ch
#tstop=315.26 # for 16hz 16ch

#ca_hz=np.transpose(np.loadtxt('mol_ca_8hz.txt.16ch'))
#filename='cainput_8hz.txt'
ca_hz=np.transpose(np.loadtxt('mol_ca_trial1/mol_ca_5hz.txt.8ch'))
filename='cainput_5hz.txt.8ch.scaled'
depth=2000;

#ca_tot5hz_16ch=41533.0
#ca_tot10hz_16ch=48433.0
#ratio=ca_tot10hz_16ch/ca_tot5hz_16ch

ca_tot5hz_8ch=23672.0
ca_tot10hz_8ch=18272.0
ratio=ca_tot5hz_8ch/ca_tot10hz_8ch

caspk=ca_hz[1][1:]-ca_hz[1][0:-1]
fhz=open(filename,'w')

for i in range(0,len(ca_hz[0])-1):
	if caspk[i]>0 and ca_hz[0][i]<=tstop:
		total_ca+=int(caspk[i]/ratio)
		line='cmd @ '+str(tadjust+ca_hz[0][i])+' pointsource ca ' + str(int(caspk[i]/ratio))+' 1 0 0 ' + str(depth-0.5)+'\n'
		fhz.write(line)
	if ca_hz[0][i]>tstop:	
		break
	
	
fhz.close()
print "total_ca:",total_ca," ratio:",ratio

# 50 uM in 0.75**2*1.5
#total_ca=25397
# 50 uM in 1*1*2
#total_ca=60200


# for 8Hz tstop is about 570 ms to 575 ms
#total_ca=31501 #as tstop=500.00 for 10hz
#total_ca=31638 #as tstop=900.00 for 5hz


#tstop=580	#from 8hz.16ch
#total_ca=41810		# as tstop=315.26
