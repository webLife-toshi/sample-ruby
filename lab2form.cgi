#!/usr/bin/ruby
#encoding:utf-8
require 'sqlite3'
require "cgi"
cgi = CGI.new

print "Content-type: text/html\n\n"

 begin

        db = SQLite3::Database.open ":testsql:"
	
    db.results_as_hash = true
        
    ary = db.execute "SELECT * FROM Form"    
        
    ary.each do |row|
        printf "%s %s %s\n", row['Id'], row['Name'], row['Email']
    end	
       

 rescue SQLite3::Exception => e

        puts "Exception occured"
        puts e

 ensure
        db.close if db
 end

#ライブラリ読み込み


#入力データが空でなければ格納
if cgi["textdata"] != "" then
	strdata = '<p>' + cgi["textdata"] + '</p>'
else
	strdata = '<p>未入力です</p>'
end

print <<EOM
<html>
<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8">
</head>
<body>
<h1>Rubyでフォームのデータを受け取る</h1>
<form action="lab2form.cgi" method="post">
	<input type="text" name="textdata" value="">
	<input type="submit" value="入力文字を表示">
</form>

	#{strdata}

</body>
</html>
EOM
