BN=$(basename $1 .pdf)

pdfimages -j $1 $BN

for PBM in *.pbm
do 
    IMG=$(basename $PBM .pbm)
    convert $PBM ${IMG}.jpg
    rm $PBM
    tesseract -l eng ${IMG}.jpg $IMG
    #cat *.txt > ${BN}-all.txt
done
