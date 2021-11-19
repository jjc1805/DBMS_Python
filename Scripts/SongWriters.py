from tkinter import *
import psycopg2

root = Tk()
root.title("SongWriters")
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
def insert_song_writers():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("INSERT INTO SongWriters VALUES(%s, %s, %s, ROW(%s, %s));",
	(writer_id.get(), name.get(), city.get(), start_date.get(), end_date.get() 
	))
	
	conn.commit()
	conn.close()
	
	writer_id.delete(0, END)
	name.delete(0, END)
	city.delete(0, END)
	start_date.delete(0, END)
	end_date.delete(0, END)
	
	
		
	
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM SongWriters;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record)+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=7, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()

#for Employee values

writer_id = Entry(root, width=30)
writer_id.grid(row=0, column=1, padx=20)
name = Entry(root, width=30)
name.grid(row=1, column=1)
city = Entry(root, width=30)
city.grid(row=2, column=1)
start_date = Entry(root, width=30)
start_date.grid(row=3, column=1)
end_date = Entry(root, width=30)
end_date.grid(row=4, column=1)


writer_id_label = Label(root, text="Writer ID")
writer_id_label.grid(row=0, column=0)
name_label = Label(root, text="Writer Name")
name_label.grid(row=1, column=0)
city_label = Label(root, text="City")
city_label.grid(row=2, column=0)
start_date_label = Label(root, text="Start Date")
start_date_label.grid(row=3, column=0)
end_date_label = Label(root, text="End Date")
end_date_label.grid(row=4, column=0)


insert_btn = Button(root, text="Insert into table", command=insert_song_writers)
insert_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()
cur.close()
conn.close()



root.mainloop()

