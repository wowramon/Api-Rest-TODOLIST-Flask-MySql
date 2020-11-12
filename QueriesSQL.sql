Drop database DBTODO;
CREATE database IF NOT exists DBTODO;

use DBTODO;


/* Tables */
create table Users(
ID int Primary key auto_increment not null,
Email varchar(30) not null,
Password varchar(200) not null,
name varchar(20) not null,
Udate date not null
);

create table Projects(
ID int Primary key auto_increment not null,
NameP varchar(20) not null,
ID_User int
);

create table Task(
ID int primary key auto_increment not null,
Name_Task varchar(20) not null,
completed bool ,
ID_Project int
);

create table State(
ID int primary key auto_increment not null,
Urgent bool,
Normal bool,
late bool,
ID_TASK int
);

/*ENTITY RELATION*/
alter table Projects
  add constraint ID_User
  foreign key (ID_User)  /* Users to Projects*/
  references Users(ID)
  on delete CASCADE
  on update no action;

alter table Task
  add constraint ID_Project
  foreign key (ID_Project)
  references Projects(ID)
  on delete CASCADE
  on update no action;
  
  alter table State
    add constraint ID_TASK
    foreign key (ID_TASK)
    references Task(ID)
    on delete CASCADE
    on update no action;
