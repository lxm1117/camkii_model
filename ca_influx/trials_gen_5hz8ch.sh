#!/bin/bash
for i in {31..40}
do 
	nohup smoldyn-cplx vchnl_5hz.txt.8ch > test.tmp.5hz
	mv mol_ca_5hz.txt.8ch 5hz_8ch_trials/mol_ca_5hz.8ch.v$i
done
