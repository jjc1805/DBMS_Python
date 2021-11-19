from tkinter import *
import psycopg2

root = Tk()
root.title("Employee")
root.geometry("400x400")

top1 = Toplevel()
top1.title("Query1")
top1.geometry("400x400")
top2 = Toplevel()
top2.title("Query2")
top2.geometry("400x400")
top3 = Toplevel()
top3.title("Query3")
top3.geometry("400x400")
top4 = Toplevel()
top4.title("Query4")
top4.geometry("400x400")
top5 = Toplevel()
top5.title("Query5")
top5.geometry("400x400")

#Database connection:
try:
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	print("Connected")
except (Exception, psycopg2.DatabaseError) as error:
	print(error)
	print("Unable to connect to database")




#insert function
def insert_employee():
	 
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	
	c.execute("INSERT INTO Employee VALUES(%s, %s, %s);",
	(emp_id.get(), name.get(), role.get()
	))
	
	conn.commit()
	conn.close()
	
	emp_id.delete(0, END)
	name.delete(0, END)
	role.delete(0, END)
	
		
#Query function to view the records on the GUI
def query():
	conn = psycopg2.connect(host="localhost", database="music_label_database", user="postgres", password="abcde")
	
	c = conn.cursor()
	
	c.execute("SELECT * FROM Employee;")
	records = c.fetchall()
	
	print_records = ''
	for record in records:
		print_records += str(record[0]) +" "+ str(record[1]) +"\t" +str(record[2])+ "\n"
	
	query_label = Label(root, text=print_records)
	query_label.grid(row=6, column=0, columnspan=2)
	
	
	conn.commit()
	conn.close()


cur = conn.cursor()

emp_id = Entry(root, width=30)
emp_id.grid(row=0, column=1, padx=20)
name = Entry(root, width=30)
name.grid(row=1, column=1)
role = Entry(root, width=30)
role.grid(row=2, column=1)

emp_id_label = Label(root, text="Employee ID")
emp_id_label.grid(row=0, column=0)
name_label = Label(root, text="Name")
name_label.grid(row=1, column=0)
role_label = Label(root, text="Role")
role_label.grid(row=2, column=0)

insert_btn = Button(root, text="Insert into table", command=insert_employee)
insert_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
	
show_btn = Button(root, text="Display records", command=query)
show_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#query commands execution:
#1.
cur.execute('''SELECT * FROM EMPLOYEE ORDER BY Employee.emp_id ASC;''')
One = cur.fetchall()
rec1=''
for i in One:
	rec1 += str(i[0])+"\t"+str(i[1])+"\t"+str(i[2]) + "\n"


text1 = Label(top1, text = "Query 1: Select all Employees in ascending order of the employee id.")
text1.grid(row=0, column=1, padx=20)
One_label = Label(top1, text=rec1)
One_label.grid(row=2, column=0, columnspan=2)

#2.
cur.execute('''SELECT contract from Artist where (contract).start_date = '2020-10-02';''')
Two = cur.fetchall()
rec2=''
for i in Two:
	rec2 += str(i[0]) + "\n"


text2 = Label(top2, text = "Query 2: Select contracts from artists whose start date is '2020-10-02'")
text2.grid(row=0, column=1, padx=20)
Two_label = Label(top2, text=rec2)
Two_label.grid(row=2, column=0, columnspan=2)

#3
cur.execute('''delete from song where song_id = 's1';
select * from song;''')
Three = cur.fetchall()
rec3=''
for i in Three:
	rec3 += str(i[0])+ "\t" + str(i[1]) +"\t" +str(i[2]) + "\n"


text3 = Label(top3, text = "Query 3: Delete all items with song_id = 's1' from the song table.")
text3.grid(row=0, column=1, padx=20)
Three_label = Label(top3, text=rec3)
Three_label.grid(row=2, column=0, columnspan=2)

#4
cur.execute('''(SELECT emp_id, name FROM EMPLOYEE) INTERSECT (SELECT artist_id, artist_name FROM artist);''')
Four = cur.fetchall()
rec4=''
for i in Four:
	rec4 += str(i[0]) + "\t" + str(i[1]) + "\n"


text4 = Label(top4, text = "Query 4: Get records with common id and name between the employee and artist tables.")
text4.grid(row=0, column=1, padx=20)
Four_label = Label(top4, text=rec4)
Four_label.grid(row=2, column=0, columnspan=2)

#5
cur.execute('''SELECT MAX(price) AS highest, MIN(price) AS lowest, (MAX(price) - MIN(price)) AS difference FROM Album;''')
Five = cur.fetchall()
rec5=''
for i in Five:
	rec5 += str(i[0])+ "\t" + str(i[1]) + "\t" + str(i[2]) + "\n"


text5 = Label(top5, text = "Query 5: Give the highest, lowest and difference between prices from Album.")
text5.grid(row=0, column=1, padx=20)
Five_label = Label(top5, text=rec5)
Five_label.grid(row=2, column=0, columnspan=2)



conn.commit()
cur.close()
conn.close()



root.mainloop()

