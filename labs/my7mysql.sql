CREATE DATABASE wsaa;
show databases;
use wsaa;
show tables;
create table student (id int NOT NULL AUTO_INCREMENT, name varchar(250), primary key(id));
describe student;
select * from student;
insert into student (name) values ("mary");
select * from student;

update student set name="maryanne" where id=2;
select * from student;
delete from student where id=3;
select * from student;