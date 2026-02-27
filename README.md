# yangco-sqlite3-to-csv
Retrieve records from sqlite3 database then put data in a csv file

## File directory overview
<img width="433" height="530" alt="image" src="https://github.com/user-attachments/assets/5a23d5c8-32ec-4c7c-88e5-3ef6a29b8a00" />

## setting up the database (using sqlite3 via cmd)
1. navigate to Documents > GitHub > yangco-sqlite3-to-csv > db
2. execute command ```sqlite3 yangcodb```
3. execute command ```.read 01_ddl_script.sql```
4. execute command ```.read 02_insert_script.sql```

Execute command ```rollback_script.sql``` to drop the tables

## Executing the program (via cmd)
1. navigate back to Documents > GitHub > yangco-sqlite3-to-csv
2. Execute command ```pip install pandas``` for download pandas library
3. Execute ```python python_only.py``` for getting the results without using pandas. Output file sample screenshot:
<img width="508" height="54" alt="image" src="https://github.com/user-attachments/assets/634fa48a-4642-4093-80ea-d3e6b374f20d" /> 

4. Execute ```python python_pandas.py``` for getting the results using pandas. Output file sample screenshot:
<img width="533" height="63" alt="image" src="https://github.com/user-attachments/assets/7fdcf59d-3662-4225-a806-3ed85f47af2a" />



   
