#! /usr/bin/env bash 
BN=$(basename $1 .txt)

echo ${BN}
mkdir "${BN}"

./lexique.sh       $1 > "${BN}/${BN}.lexique.txt"
python2 collocations.py  $1 > "${BN}/${BN}.collocations.json"
./index.sh         $1 > "${BN}/${BN}.index.txt"
python2 proper.py        $1 > "${BN}/${BN}.proper.txt"
python2 unusual.py       $1 > "${BN}/${BN}.unusual.txt"
