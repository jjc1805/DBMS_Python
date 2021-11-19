from tkinter import *
import psycopg2

root = Tk()
root.title("Members")
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
def insert_member():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("INSERT INTO Members VALUES(%s, %s, %s, %s);",
	(member_id.get(), name.get(), instrument.get(), city.get()
	))
	
	conn.commit()
	conn.close()
	
	member_id.delete(0, END)
	name.delete(0, END)
	instrument.delete(0, END)
	city.delete(0, END)
	
		
	
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM Members;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record)+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=6, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()


member_id = Entry(root, width=30)
member_id.grid(row=0, column=1, padx=20)
name = Entry(root, width=30)
name.grid(row=1, column=1)
instrument = Entry(root, width=30)
instrument.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)

member_id_label = Label(root, text="Member ID")
member_id_label.grid(row=0, column=0)
name_label = Label(root, text="Member Name")
name_label.grid(row=1, column=0)
instrument_label = Label(root, text="Instrument")
instrument_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)


insert_btn = Button(root, text="Insert into table", command=insert_member)
insert_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()
cur.close()
conn.close()



root.mainloop()

