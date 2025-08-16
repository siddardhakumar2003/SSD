delimiter //
drop procedure if exists AddSubscriberIfNotExists;
create procedure AddSubscriberIfNotExists(IN subName VARCHAR(100))
begin
	declare subId int;
    declare max1 int;
	declare  sub cursor for select max(subscriberid) from subscribers;
    declare exist cursor for select count(subscriberName) from subscribers where subscriberName=subName;
    open exist;
    open sub;
    fetch exist into max1;
    fetch sub into subId;
    if max1=0 then insert into subscribers(SubscriberID,SubscriberName) values(subId+1,subName);
    else select concat(subname," Already Exists") as output;
    end if; 
    close sub;
    close exist;
end//