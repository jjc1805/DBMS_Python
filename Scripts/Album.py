from tkinter import *
import psycopg2

root = Tk()
root.title("Album")
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
def insert_album():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("INSERT INTO Album VALUES(%s, %s, %s, %s);",
	(album_id.get(), album_name.get(), date_released(), price.get()
	))
	
	conn.commit()
	conn.close()
	
	album_id.delete(0, END)
	album_name.delete(0, END)
	date_released.delete(0, END)
	price.delete(0, END)
	
	
		
	
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM Album;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record)+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=6, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()

#for Employee values

album_id = Entry(root, width=30)
album_id.grid(row=0, column=1, padx=20)
album_name = Entry(root, width=30)
album_name.grid(row=1, column=1)
date_released = Entry(root, width=30)
date_released.grid(row=2, column=1)
price = Entry(root, width=30)
price.grid(row=3, column=1)

album_id_label = Label(root, text="Manager ID")
album_id_label.grid(row=0, column=0)
album_name_label = Label(root, text="Manager Name")
album_name_label.grid(row=1, column=0)
date_released_label = Label(root, text="Manager ID")
date_released_label.grid(row=2, column=0)
price_label = Label(root, text="Manager ID")
price_label.grid(row=3, column=0)


insert_btn = Button(root, text="Insert into table", command=insert_album)
insert_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()
cur.close()
conn.close()



root.mainloop()

