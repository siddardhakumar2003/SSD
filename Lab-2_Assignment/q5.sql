delimiter //

drop procedure if exists SendWatchTimeReportAllSubscribers;
create procedure  SendWatchTimeReportAllSubscribers()
begin
	declare id int;
    declare end1 int default false;
    declare sub_id cursor for select subscriberid from subscribers;
    declare continue handler for not found set end1=true;
	create table if not exists temp(
    subscriberName varchar(100),
    title varchar(100),
    genre varchar(100),
    watchtime int
    );
	open sub_id;
    l:loop
		fetch sub_id into id;
        if end1 then leave l;
        end if;
        call GetWatchHistoryBySubscriber(id);
	end loop;
    close sub_id;
    select * from temp;
    drop table temp;
end;
//