BN="$(basename $1 .txt)"

mkdir "$BN"
./lexique.sh       $1 > ${BN}/${BN}.lexique.txt
python collocations.py  $1 > ${BN}/${BN}.collocations.json
./index.sh         $1 > ${BN}/${BN}.index.txt
python proper.py        $1 > ${BN}/${BN}.proper.txt
python unusual.py       $1 > ${BN}/${BN}.unusual.txt
