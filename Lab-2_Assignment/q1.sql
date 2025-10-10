DELIMITER //
DROP PROCEDURE IF EXISTS ListAllSubscribers;

create procedure ListAllSubscribers()
begin 
declare end1 int default false;
declare sub_name varchar(100);
declare name cursor for select SubscriberName from subscribers;
declare continue handler for not found set end1=true;
create table if not exists s_name (n varchar(100));
open name;
iterator: LOOP
	fetch name into sub_name;
	if end1 then 
		leave iterator;
    end if;
		 insert into s_name values(sub_name);
 end loop;
 select n as names from s_name;
 drop table s_name;
 close name;
 end//
 
 