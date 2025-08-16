delimiter //
drop procedure if exists GetWatchHistoryBySubscriber;
create procedure GetWatchHistoryBySubscriber(IN sub_id INT)
begin
	select s.showid,s.title,w.watchtime from shows s natural join watchhistory w;
end //