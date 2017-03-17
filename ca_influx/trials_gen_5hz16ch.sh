#!/bin/bash
for i in {31..40}
do 
	nohup smoldyn-cplx vchnl_5hz.txt > test.tmp.5hz.16ch
	mv mol_ca_5hz.txt.16ch 5hz_16ch_trials/mol_ca_5hz.16ch.v$i
done
