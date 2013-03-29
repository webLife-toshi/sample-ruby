#!/usr/bin/ruby

require 'sqlite3'

 begin

	db = SQLite3::Database.open ":testsql:"
	
	db.execute "CREATE TABLE IF NOT EXISTS Form(Id INTEGER PRIMARY KEY, Name TEXT not null, Email TEXT unique, Comment TEXT)"
	db.execute "INSERT INTO Form VALUES(1, 'Audi', 'example1@email.com','test test test test test test test test test test test test test' )"

 rescue SQLite3::Exception => e

	puts "Exception occured"
	puts e

 ensure
	db.close if db
 end

