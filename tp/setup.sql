create database if not exists monitoring;

use monitoring;

create table app_status (
  id int auto_increment primary key,
  timestamp datetime,
  app_name varchar(255),
  status varchar(50),
  response_time float
)
