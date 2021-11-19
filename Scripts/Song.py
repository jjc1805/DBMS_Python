from tkinter import *
import psycopg2

root = Tk()
root.title("Song")
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
def insert_song():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("INSERT INTO Song VALUES(%s, %s, %s);",
	(song_id.get(), song_name.get(), album_name.get()
	))
	
	conn.commit()
	conn.close()
	
	song_id.delete(0, END)
	song_name.delete(0, END)
	album_name.delete(0, END)
	
	
		
	
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM Song;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record)+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=5, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()

#for Employee values

song_id = Entry(root, width=30)
song_id.grid(row=0, column=1, padx=20)
song_name = Entry(root, width=30)
song_name.grid(row=1, column=1)
album_name = Entry(root, width=30)
album_name.grid(row=2, column=1)

song_id_label = Label(root, text="Song ID")
song_id_label.grid(row=0, column=0)
song_name_label = Label(root, text="Song Name")
song_name_label.grid(row=1, column=0)
album_name_label = Label(root, text="Album Name")
album_name_label.grid(row=2, column=0)


insert_btn = Button(root, text="Insert into table", command=insert_song)
insert_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



conn.commit()
cur.close()
conn.close()



root.mainloop()

