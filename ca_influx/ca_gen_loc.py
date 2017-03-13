import numpy as np
total_ca=8500

ca_hz=np.transpose(np.loadtxt('mol_ca_3hz.txt'))
filename='cainput_3hz.txt'
chnl_file='3hz_chnlact.txt'

fhz=open(filename,'w')

ca_acc=0
chnl=open(chnl_file,'r')

locx=[0,-50,-50,50, 50,-100,-100,100, 100]
locy=[0,-50, 50,50,-50,-100, 100,100,-100]
for line in chnl:
	time=float(line.split(' ')[0].split('=')[1])
	chnl_no=int(line.split(' ')[2].split('=')[1])
	ca_acc+=1
	if  ca_acc<total_ca:
		#print time, chnl_no
		outputline='cmd @ ' + str(time) + ' pointsource ca 1 1 '+str(locx[chnl_no-1])+' ' + str(locy[chnl_no-1])+' 998\n'
		fhz.write(outputline)	
	else: break
chnl.close()


'''
caspk=ca_hz[1][1:]-ca_hz[1][0:-1]
for i in range(0,len(ca_hz[0])-1):
	if caspk[i]>0 and ca_hz[1][i]<total_ca:
		line='cmd @ '+str(ca_hz[0][i])+' pointsource ca ' + str(int(caspk[i]))+' 1 0 0 998\n'
		fhz.write(line)
	if ca_hz[1][i]>total_ca:	
		break
'''	
	
fhz.close()
