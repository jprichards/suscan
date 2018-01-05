# SUscan
```
usage: suscan.py [-h] [-s] [-e]

Find & Extract Build Numbers from Apple sucatalogs

Full Run: python suscan.py -se

optional arguments:
  -h, --help  show this help message and exit
  -s          Save urls for dist files with auxinfo key to local json
  -e          Extract Build Number from files in local json
  ```

Example Run:
```
15:59 jrichards @ suscan $  python suscan.py -se
Downloading https://swscan.apple.com/content/catalogs/others/index-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 525 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 721 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 985 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1315 English dist files ***
Downloading https://swscan.apple.com/content/catalogs/others/index-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1318 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1460 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-lion-snowleopard-leopard.merged-1.sucatalog
*** Found 1640 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-leopard-snowleopard.merged-1.sucatalog
*** Found 1646 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/others/index-leopard.merged-1.sucatalog
*** Found 1646 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/index-1.sucatalog
*** Found 1646 English dist files ***
Downloading http://swscan.apple.com/content/catalogs/index.sucatalog
*** Found 1646 English dist files ***
Searching for auxinfo key in each dist file...
*** Found auxinfo for 091-52052 ***
*** Found auxinfo for 091-33271 ***
Writing matches to auxinfo.json file...
Complete
Reading from auxinfo.json file...
Extracting Build Info from each match...
[{'10.13.2': '17C2120'}, {'10.13.2': '17C88'}]
```
