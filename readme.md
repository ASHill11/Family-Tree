# Singing Cadets Family Tree Project

## Running the SQLite3 console
To open the SQLite3 console, make sure you have sqlite3 installed ([installation guide](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm) and [download page](https://www.sqlite.org/download.html)), then run the following command from the project directory:
```
sqlite3 sqlite3-db/pythonsqlite.db
```
To list all tables, run this command:
```
.tables
```
To safely quit the console, run this command:
```
.quit
```
To see the table info for the table `person`, run this command:
```
PRAGMA table_info('person');
```
To see all entries in the table `person' run this command:
```
SELECT * FROM person;
```