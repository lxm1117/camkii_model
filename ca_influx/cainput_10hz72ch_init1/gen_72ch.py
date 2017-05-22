import numpy as np
import pdb
mol_ca1=np.transpose(np.loadtxt('../10hz_16ch_trials/mol_ca_10hz.16ch.v16'))
mol_ca2=np.transpose(np.loadtxt('../10hz_16ch_trials/mol_ca_10hz.16ch.v14'))
mol_ca3=np.transpose(np.loadtxt('../10hz_16ch_trials/mol_ca_10hz.16ch.v34'))
mol_ca4=np.transpose(np.loadtxt('../10hz_16ch_trials/mol_ca_10hz.16ch.v6'))
mol_ca5=np.transpose(np.loadtxt('../10hz_16ch_trials/mol_ca_10hz.16ch.v40'))

mol_ca=np.zeros(shape=(2,len(mol_ca1[0])))
mol_ca[0]=mol_ca1[0]
mol_ca[1]=mol_ca1[1]+mol_ca2[1]+mol_ca3[1]+mol_ca4[1]+mol_ca5[1]	
#pdb.set_trace()
fw=open('mol_ca_10hz.72ch','w')

for i in range(0,len(mol_ca[0])):
	fw.write(str(int(mol_ca[0][i]))+' '+str(int(mol_ca[1][i]))+'\n')

fw.close()	
