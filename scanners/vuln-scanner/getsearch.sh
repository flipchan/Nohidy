echo 'downloading cve and simular'

wget 'https://github.com/offensive-security/exploit-database/raw/master/files.csv'

wget 'http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml'

wget 'http://cve.mitre.org/data/downloads/allitems-cvrf.xml'

wget 'http://oval.mitre.org/rep-data/5.3/org.mitre.oval/oval.xml'

echo 'done'
