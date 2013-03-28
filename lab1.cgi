#!/usr/bin/ruby

require 'sqlite3'

begin
	db = SQLite3::Database.open "test.db"
	db.execute "CREATE TABLE IF NOT EXISTS Cars(Id INTEGER PRIMARY KEY,Name TEXT, Price INT)"
	db.execute "INSERT INTO Cars VALUES(1,'Audi',52642)"
	db.execute "INSERT INTO Cars VALUES(2,'Mercedes',57127)"
	db.execute "INSERT INTO Cars VALUES(3,'Skoda', 9000)"
	db.execute "INSERT INTO Cars VALUES(4,'Volvo',29000)"

 rescue SQLite3::Exception => e

	puts "Exception occured"
	puts e

 ensure
	db.close if db

end


