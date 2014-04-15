$BN="$(basename $1 .txt)"

./lexique.sh       $1 > ${BN}/${BN}.lexique.txt
./collocations.py  $1 > ${BN}/${BN}.collocations.json
./index.sh         $1 > ${BN}/${BN}.index.txt
./proper.py        $1 > ${BN}/${BN}.proper.txt
./unusual.py       $1 > ${BN}/${BN}.unusual.txt
