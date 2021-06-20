create table Usuario(id int, email varchar(255), username varchar(50));
alter table Usuario add edad int;
alter table Usuario drop column edad;
alter table Usuario modify column email varchar(50);


insert into Usuario (email, username) values ('fabiana@correo.com', 'Fabiana');
delete from Usuario where username = 'Fabiana' limit 1;

alter table Usuario add primary key (id);
alter table Usuario modify column id int AUTO_INCREMENT;

insert into Usuario (email, username) values ('esteban@correo.com', 'Esteban');

update Usuario set edad = 31 where id = 1;

insert into Usuario (email, username, edad) values ('lalala@correo.com', 'Lala', 13);
delete from Usuario where id = 3 ;