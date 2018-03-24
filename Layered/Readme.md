
Layered Architecture
-----------------------------------------------------------

Database

Test file is main.py

The project is a database that uses a layered architecture to retrieve 
data. There are three layers - 

	1. File Layer - deals with the loading and saving of text files to and from memory.
	2. Encryption Layer - deals with the encryption and decryption of the database data. Communicates with File Layer.
	3. Database Layer - creates and presents tables in a code friendly format for use. Communicates with Encryption Layer.

The FileLayer saves the data into the data folder.

Commands

	=>showTables 

		shows the tables in the database

	=>selectTable (table name)

		selects a table for editing

		usage: selectTable goo

	=>addTable (table name)

		adds a table to the database

		usage: addTable newtable

	=>printTable

		displays the currently selected table

	=>addColumn (column name)

		adds a column to the current table

		usage: addColumn newcolumn

	=>addRow (row data)

		adds a row to the current table

		usage: addRow data1 data2 data3

	=>setValue (condition, column name, data)

		sets a value in the current table

		usage: setValue column1=>data1  column3 data3