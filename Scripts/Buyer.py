from tkinter import *
import psycopg2

root = Tk()
root.title("Buyer")
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
def insert_buyer():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("INSERT INTO Buyer VALUES(%s, %s);",
	(buyer_id.get(), buyer_name.get(), city.get(), ph_no.get()
	))
	
	conn.commit()
	conn.close()
	
	buyer_id.delete(0, END)
	buyer_name.delete(0, END)
	city.delete(0, END)
	ph_no.delete(0, END)
	
	
		
	
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM Buyer;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record)+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=6, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()

#for Employee values

buyer_id = Entry(root, width=30)
buyer_id.grid(row=0, column=1, padx=20)
buyer_name = Entry(root, width=30)
buyer_name.grid(row=1, column=1)
city = Entry(root, width=30)
city.grid(row=2, column=1)
ph_no = Entry(root, width=30)
ph_no.grid(row=3, column=1)

buyer_id_label = Label(root, text="Buyer ID")
buyer_id_label.grid(row=0, column=0)
buyer_name_label = Label(root, text="Buyer Name")
buyer_name_label.grid(row=1, column=0)
city_label = Label(root, text="City")
city_label.grid(row=2, column=0)
ph_no_label = Label(root, text="Phone Number")
ph_no_label.grid(row=3, column=0)


insert_btn = Button(root, text="Insert into table", command=insert_buyer)
insert_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()
cur.close()
conn.close()



root.mainloop()

