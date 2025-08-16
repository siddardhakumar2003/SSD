Assignment Software Systems Development


Question 1:
    We were asked to print all subscribers using cursor.
    - Defined a cursor to point all rows from subscribers table and insert the row in temporary table sub_name.
    - Printed all row in sub_name table.
    - Drop the table for any name clashes.
    I used this temporary table to show all names otherwise only last row was printed previously.
    To execute Script run the following commands after opening mysql:
    - use mysql (Database)
    - mysql -u [username] -p[password] [database_name] < q1.sql
    - call ListAllSubscribers();

Question 2:
    We were asked to print all shows watched by subscriber with particular id with their watch time.
    - Query a select statement with where clause of subscriber id = given id from table shows and watchistory join
    To execute Script run the following commands after opening mysql:
    - use mysql (Database)
    - mysql -u [username] -p[password] [database_name] < q2.sql
    - call GetWatchHistoryBySubscriber(<sub_id>); [give id instead of sub_id]

Question 3:
    We were asked to insert given subscriber name into subscribers table.
    - Cursor exist pointing to select statement for count(subscriberName) with where clause of subscriber name = given name from table subscribers.
    - If output was zero then insert statement executed esle output already exists.
    - For primary key i used cursor to find max key then for inserting max+1 was added in primary key. 
    To execute Script run the following commands after opening mysql:
    - use mysql (Database)
    - mysql -u [username] -p[password] [database_name] < q3.sql
    - AddSubscriberIfNotExists(<subName>); [Write name instead of subname]

Question 4:
    We were asked to print watch time report of all subscriber who are subscribed only.
    - cursor sub_id to get all subscriber from watchhistory table so that we get only subscriber who are subscribed.
    - to print all is created a table temp to store all information 
    - called a procedure which insert all row of watchhistorytable into temp for given subscriber id.
    - drop table temp for future purpose.
    To execute Script run the following commands after opening mysql:
    - use mysql (Database)
    - mysql -u [username] -p[password] [database_name] < q4.sql
    - call SendWatchTimeReport();

Question 5:
    We were asked to print watch time report of all subscribers.
    - cursor sub_id to get all subscriber from subscribers table so that we get all subscribers.
    - to print all is created a table temp to store all information 
    - called a procedure which insert all row of watchhistorytable into temp for given subscriber id.
    - drop table temp for future purpose.
    To execute Script run the following commands after opening mysql:
    - use mysql (Database)
    - mysql -u [username] -p[password] [database_name] < q5.sql
    - call SendWatchTimeReportAllSubscribers();