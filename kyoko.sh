# fetch menu
wget -q -O deli.pdf "http://www.cardenas.co.jp/shop/deli_weekly%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC.pdf"

# convert pdf to png
convert -density 300 deli.pdf -quality 90 src.png

# trim for each day
convert -crop 1960x550+400+600  src.png dest1.png
convert -crop 1960x550+400+1150 src.png dest2.png
convert -crop 1960x550+400+1700 src.png dest3.png
convert -crop 1960x550+400+2250 src.png dest4.png
convert -crop 1960x550+400+2800 src.png dest5.png

# run
python kyoko.py
