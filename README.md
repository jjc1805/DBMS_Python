# Database Management System using Ptinker and Psycopg2
This is the project on a Database Management System using Ptinker and Psycopg2 libraries.

# Initial Requirements:
1. Your system must have python installed preferably version 3 and above.
2. Install the psycopg2 library.
3. Install postgresSQL

# Creating the Database:
1. Under the Database folder, two files create.sql and insert.sql are included.
2. In postgres terminal run the 2 files using,

        psql -U postgres -f <file_path of create.sql>
   This will create the database. For this project I've used a Music Label Database.
        
        psql -U postgres -f <file_path of insert.sql>
   This command will populate the database with values.
   
# Creating the GUI and connecting using Psycopg2:
