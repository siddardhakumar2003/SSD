delimiter //
drop procedure if exists GetWatchHistoryBySubscriber;
create procedure GetWatchHistoryBySubscriber(IN sub_n int)
begin 
	declare watch int;
    insert into temp select  n.subscriberName, s.title,s.genre, w.watchtime from (subscribers n left join watchhistory w on w.subscriberid = n.subscriberid) left join shows s on s.showid = w.showid where n.subscriberId=sub_n;	
end;
//

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