#!/bin/bash
for i in {31..40}
do 
	nohup smoldyn-cplx vchnl_10hz.txt.8ch > test.tmp.10hz.8ch
	mv mol_ca_10hz.txt.8ch 10hz_8ch_trials/mol_ca_10hz.8ch.v$i
done
