#!/bin/bash
for i in {31..40}
do 
	nohup smoldyn-cplx vchnl.txt > test.tmp
	mv mol_ca_10hz.txt.16ch 10hz_16ch_trials/mol_ca_10hz.16ch.v$i
done
