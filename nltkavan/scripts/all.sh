BN="$(basename $1 .txt)"

mkdir ../results/"$BN"
./lexique.sh       $1 > ../results/${BN}/${BN}.lexique.txt
python2 collocations.py  $1 > ../results/${BN}/${BN}.collocations.json
./index.sh         $1 > ../results/${BN}/${BN}.index.txt
python2 proper.py        $1 > ../results/${BN}/${BN}.proper.txt
python2 unusual.py       $1 > ../results/${BN}/${BN}.unusual.txt
