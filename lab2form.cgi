#!/usr/bin/ruby
print "Content-type: text/html\n\n"

#ライブラリ読み込み
require "cgi"
cgi = CGI.new

#入力データが空でなければ格納
if cgi["textdata"] != "" then
	strdata = '<p>' + cgi["textdata"] + '</p>'
else
	strdata = '<p>未入力です</p>'
end

print <<EOM
<html>
<head>
	<meta http-equiv="Content-type" content="text/html; charset=euc-jp">
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
