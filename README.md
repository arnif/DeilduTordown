HOW TO:

Farðu í
chrome://settings/cookies

Leita eftir deildu
skrifar niður value á uid og pass, þetta er hægt að gera í hvaða tölvu sem er á meðan réttur notandi er skráður inn á deildu.net.
setur það í uid og pass value í tordown.py (efst)

Farðu svo á deildu.net og í RSS og fáðu RSS link, mæli með að hafa hakað í Þættir, Hi-Def og Heimildarefni. Feed type: Direct Download.

Í regex eru nokkur regular expression fyrir nokkra þætti. http://regexpal.com/ er hentug til að búa til regular expression.

PASSA að það eru engar tómar línur í regex skjalinu.

Til að keyra scriptuna:

	$ python tordown.py path/to/save/file 'link_to_rssfeed'

Svo í sér torrent clientinn þinn um að monitora path/to/save/file .

Viljir þú keyra scriptuna á t.d 15 min fresti setur hana í cronjob
	
	$ crontab -e

Setur svo þessa línu neðst

	*/15 * * * * sh ~/path/to/DeilduScript.sh
