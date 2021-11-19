drop database music_label_database ;
create database music_label_database ;

\c music_label_database

create table Employee
(
	emp_id char(9),
	name varchar(20) not null,
	role varchar(15),
	primary key(emp_id)
);

create table Manager 
(	
	manager_id char(9),
	manager_name varchar(20) not null,
	primary key(manager_id),
	foreign key(manager_id) references Employee(emp_id)
);

create type contract_data as
(	
	start_date Date,
	end_date Date
);

create table Artist
(	Artist_id char(9),
	Artist_name varchar(20) not null,
	genre varchar(10),
	contract contract_data,
	primary key (Artist_id),
	foreign key(Artist_id) references Employee(emp_id)
	
);

create table Members
(	
	member_id char(9),
	name varchar(20) not null,
	instrument varchar(15),
	city varchar(15),
	primary key (member_id),
	foreign key(member_id) references Employee(emp_id)
);



create table SongWriters
(	
	writer_id char(9),
	name varchar(20) not null,
	city varchar(15),
	contract contract_data,
	primary key (writer_id),
	foreign key(writer_id) references Employee(emp_id)
);

create table Studio
(
	studio_id char(9),
	studio_name varchar(20) not null,
	city varchar(15),
	hourly_cost Decimal,
	primary key (studio_id)
);

create table Album
(	
	album_id char(9),
	album_name varchar(15),
	date_released Date,
	price Decimal,
	primary key (album_id, album_name)
);

create table Song
(
	song_id char(9),
	song_name varchar(30) not null,
	album_name varchar(15) not null,
	primary key (song_id)
);


create table Buyer
(
	buyer_id char(9),
	buyer_name varchar(20) not null,
	city varchar(15),
	ph_no int not null,
	primary key (buyer_id)
);


