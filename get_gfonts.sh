grep "src" fonts.css | awk -F 'url\(|\)' '{print $2}' > files.txt
mkdir fonts
cd fonts
xargs -n 1 curl -O < ../files.txt
cd ../
sed -i 's/old-text/new-text/g' fonts.css
python3 replace.py
mv fonts.css fonts_old.css
mv fonts_repl.css fonts.css
