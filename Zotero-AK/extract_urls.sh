while read p; do
    url=`echo "${p}" | cut -f 1`
    fn=screenshots/`echo "${p}" | cut -f 2`.png
    webtocon ${url} "${fn}" 1280 1024
done < sources.list
