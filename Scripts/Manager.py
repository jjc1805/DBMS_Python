from tkinter import *
import psycopg2

root = Tk()
root.title("Manager")
root.geometry("400x400")

#Database connection:
try:
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	print("Connected")
except (Exception, psycopg2.DatabaseError) as error:
	print(error)
	print("Unable to connect to database")

#Query statements:
cur = conn.cursor()

#insert function
def insert_manager():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("INSERT INTO Manager VALUES(%s, %s);",
	(manager_id.get(), manager_name.get()
	))
	
	conn.commit()
	conn.close()
	
	manager_id.delete(0, END)
	manager_name.delete(0, END)
	
	
		
	
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM Manager;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record)+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=6, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()

#for Employee values

manager_id = Entry(root, width=30)
manager_id.grid(row=0, column=1, padx=20)
manager_name = Entry(root, width=30)
manager_name.grid(row=1, column=1)

manager_id_label = Label(root, text="Manager ID")
manager_id_label.grid(row=0, column=0)
manager_name_label = Label(root, text="Manager Name")
manager_name_label.grid(row=1, column=0)


insert_btn = Button(root, text="Insert into table", command=insert_manager)
insert_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()
cur.close()
conn.close()



root.mainloop()

