#!/usr/bin/ruby

require 'sqlite3'

 begin

	db = SQLite3::Database.open ":testsql:"
	
	db.execute "INSERT INTO Form(Name,Email,Comment) VALUES('Tom', 'example2@email.com','hello, everyone. How is your feeling?' )"

	id = db.last_insert_row_id
	puts "The last id of the inserted row is #{id}"

 rescue SQLite3::Exception => e

	puts "Exception occured"
	puts e

 ensure
	db.close if db
 end

