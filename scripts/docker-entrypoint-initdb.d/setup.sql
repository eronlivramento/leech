create schema geolocation;

drop table if exists geolocation.ceps_range;
create table geolocation.ceps_range (
	id serial PRIMARY KEY,
	state VARCHAR(2) NOT NULL,
	location VARCHAR ( 200 ) NOT NULL,
	range VARCHAR ( 50 ) NOT NULL
);