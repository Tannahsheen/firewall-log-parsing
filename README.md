# firewall-log-parsing

two basic scripts for checking csv outputs from firewalls. 

One is specific-ip-csv-filter.py which pulls out all rows with a specific ip. Put in edit the script to change xxx.xxx.xxx.xxx with your input ip you want to searh for. edit YOURFILE.csv with your firewall csv logs. 
The second is bad-ip-check.py which is a script to take a specified known bad ip list. it will prompt you for the bad ip list, and the input csv. then output a new csv with all of the known bad ips showing up in rows. 
