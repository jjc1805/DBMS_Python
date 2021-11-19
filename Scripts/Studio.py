from tkinter import *
import psycopg2

root = Tk()
root.title("Studio")
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
def insert_studio():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("INSERT INTO Studio VALUES(%s, %s, %s, %s);",
	(studio_id.get(), studio_name.get(), city.get(), hourly_cost.get()
	))
	
	conn.commit()
	conn.close()
	
	studio_id.delete(0, END)
	studio_name.delete(0, END)
	city.delete(0, END)
	hourly_cost.delete(0, END)
	
	
		
	
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM Studio;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record)+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=6, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()

#for Employee values

studio_id = Entry(root, width=30)
studio_id.grid(row=0, column=1, padx=20)
studio_name = Entry(root, width=30)
studio_name.grid(row=1, column=1)
city = Entry(root, width=30)
city.grid(row=2, column=1)
hourly_cost = Entry(root, width=30)
hourly_cost.grid(row=3, column=1)

studio_id_label = Label(root, text="Studio ID")
studio_id_label.grid(row=0, column=0)
studio_name_label = Label(root, text="Studio Name")
studio_name_label.grid(row=1, column=0)
city_label = Label(root, text="City")
city_label.grid(row=2, column=0)
hourly_cost_label = Label(root, text="Hourly Cost")
hourly_cost_label.grid(row=3, column=0)



insert_btn = Button(root, text="Insert into table", command=insert_studio)
insert_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()
cur.close()
conn.close()



root.mainloop()

