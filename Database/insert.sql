\c music_label_database

--write Employee here
insert into Employee values('mn_1', 'Robert', 'Manager');
insert into Employee values('mn_2','Jenny','Manager');
insert into Employee values('mn_3','Randy','Manager');

insert into Employee values('ar_1','Why Dont We','Artist');
insert into Employee values('ar_2','Sonic Silk','Artist');
insert into Employee values('ar_3','Jeremy Zucker','Artist');

insert into Employee values('mm1','Corbyn','Member');
insert into Employee values('mm2','Jonah','Member');
insert into Employee values('mm3','Bruno Mars','Member');

insert into Employee values('sw1','Jacob','Songwriter');
insert into Employee values('sw2','Mary','Songwriter');
insert into Employee values('sw3','Jose','Songwriter');


insert into Manager values('mn_1', 'Robert');
insert into Manager values('mn_2','Jenny');
insert into Manager values('mn_3','Randy');

insert into Artist values('ar_1', 'Why Don’t We', 'Pop',ROW('2020-10-02','2024-10-02'));
insert into Artist values('ar_2','Sonic Silk','Indie',ROW('2019-12-07','2023-12-07'));
insert into Artist values('ar_3','Jeremy Zucker','Pop',ROW('2017-09-22','2021-09-22'));

insert into Members values('mm1', 'Corbyn', 'Guitar', 'Ohio');
insert into Members values('mm2','Jonah', 'Piano', 'New York');
insert into Members values('mm3','Bruno Mars', 'Drums', 'New York');

insert into Songwriters values('sw1','Jacob','LA',ROW('021-06-29','2025-06-29'));
insert into Songwriters values('sw2','Mary','Florida',ROW('2019-03-01','2023-03-01'));
insert into Songwriters values('sw3','Jose','Minnesota',ROW('2018-01-20','2022-01-20'));

insert into Studio values('sid', 'Oceans Production','NewYork',1000.0);

insert into Album values('al1','The Good Times', '2021-01-13',250);
insert into Album values('al2','Unorthodox','2019-10-02', 300);
insert into Album values('al3','Chickens','2021-10-21', 250);

insert into Song values('s1','Love Back','The Good Times');
insert into Song values('s2','It will rain','Unorthodox');
insert into Song values('s3','No One Compares to You','Good Friends');

insert into Buyer values('b1', 'Jason', 'Bangalore','136019827');
insert into Buyer values('b2','Dhruv','Kochi','1092748201');
insert into Buyer values('b3','Gauri','Panjim','183926902');
