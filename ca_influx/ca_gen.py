# 1 fA=1e-15 C/s ~ 3.12 ions/ms
import numpy as np
#30 uM in 1*1*2 volume
#total_ca=36120
# 30 uM in 0.75**2*1.5
total_ca=0

frequency='5hz'
channel='72ch'
#depth=5000	
depth=2000

#tadjust=120	#delay input by 120ms
tadjust=10
if frequency=='5hz':
	tstop=855	# 5hz 8ch
elif frequency=='10hz':
	tstop=465	# 10hz 8ch

#ca_hz=np.transpose(np.loadtxt('5hz_16ch_trials/mol_ca_5hz.16ch.v4'))
#filename='cainput_10hz8ch.txt.3'

ca_hz=np.transpose(np.loadtxt('mol_ca_'+frequency+'.'+channel))
filename='cainput_'+frequency+channel+'.txt'

caspk=ca_hz[1][1:]-ca_hz[1][0:-1]
fhz=open(filename,'w')

for i in range(0,len(ca_hz[0])-1):
	if caspk[i]>0 and ca_hz[0][i]<=tstop:
		total_ca+=int(caspk[i])
		line='cmd @ '+str(tadjust+ca_hz[0][i])+' pointsource ca ' + str(int(caspk[i]))+' 1 0 0 ' + str(depth-0.5)+'\n'
		fhz.write(line)
	if ca_hz[0][i]>=tstop:	
		break
	
	
fhz.close()
print "total_ca:",total_ca

