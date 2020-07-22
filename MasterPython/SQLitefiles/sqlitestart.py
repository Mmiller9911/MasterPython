# SQLite3 is a very easy to use database engine. It is self-contained, serverless,
# zero-configuration and transactional. It is very fast and lightweight, and the entire database is stored in a single disk file.
# It is used in a lot of applications as internal data storage. The Python Standard Library includes a module called "sqlite3" intended for working with this database.
# This module is a SQL interface compliant with the DB-API 2.0 specification.
#
# Additionally it is worth installing the command line client (not included with sqlite) so that the sql itself can be checked without worrying about the python code also.
#
# https://www.sqlite.org/index.html
#
# sqlite-tools-win32-x86-3310100.zip
# (1.74 MiB)		A bundle of command-line tools for managing SQLite database files,
# including the command-line shell program, the sqldiff.exe program, and the sqlite3_analyzer.exe program.
# (sha1: 84de665d28cff0f8c512889cd356712e17310637)

# in sqlite you can put any type of data into any datatype column!
# in sqlite there is no alter table command so it is important to get things correct first time
# file ext doesn't matter
# do not need to specify auto_increment on primary keys as it is done automatically
# doesn't run on a server, intended to be used within a program
# doesn't have stored procedures

#  console commands
# .quit
# .help
# .tables
# .schema
# .dump
# sqlite3 test.db
# sqlite> .backup testbackup
# sqlite> .restore music-backup2
# . headers on - display column headers

# sqlite> create table contacts (name text, phone integer, email text);
# sqlite> insert into contacts (name, phone, email) values ('matt', 454545, 'matt@gmail.com')
# sqlite> insert into contacts values ('Harmony', 2103, 'bbhmf@gmail.com');
# sqlite> select * from albums order by name COLLATE NOCASE;
# sqlite> select * from albums order by artist, name COLLATE NOCASE;
# sqlite> select * from songs order by album,track;
# sqlite> select songs.track, songs.title, albums.name FROM songs JOIN albums ON songs.album = albums._id;
# sqlite> select songs.track, songs.title, albums.name FROM songs INNER JOIN albums ON songs.album = albums._id;
# sqlite> select albums.name, songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id ORDER BY albums.name, songs.track;
# sqlite> select artists.name, albums.name FROM artists INNER JOIN albums ON artists._id = albums.artist ORDER BY artists.name;
#
# sqlite> select artists.name, albums.name, songs.track, songs.title from songs
#    ...> inner join albums on songs.album = albums._id
#    ...> inner join artists on albums.artist = artists._id
#    ...> where albums.name = 'Doolittle'
#    ...> order by artists.name, albums.name, songs.track;
#
# sqlite> select artists.name, albums.name, songs.track, songs.title from songs
#    ...> inner join albums on songs.album = albums._id
#    ...> inner join artists on albums.artist = artists._id
#    ...> where songs.title LIKE 'doctor'
#    ...> ;
#
# sqlite> select artists.name, albums.name, songs.track, songs.title from songs
#    ...> inner join albums on songs.album = albums._id
#    ...> inner join artists on albums.artist = artists._id
#    ...> where songs.title LIKE '%doctor%';
#
# sqlite> create view artist_list AS
#    ...> select artists.name, albums.name, songs.track, songs.title from songs
#    ...> inner join albums on songs.album = albums._id
#    ...> inner join artists on albums.artist = artists._id
#    ...> order by artists.name, albums.name, songs.track;
#
# /* artist_list(name,"name:1",track,title) */;
# sqlite> select * from artist_list where title  = 'Sheik';
# ZZ Top|Tres Hombres|9|Sheik
#
# sqlite> select * from artist_list where track <> 71;
# sqlite> select count(*) from songs;
# sqlite> select songs.title from songs inner join albums on songs.album = albums._id where albums.name = 'Forbidden';
#
# sqlite> select songs.track, songs.title from songs inner join albums on songs.album = albums._id where albums.name = 'Forbidden' order by songs.track;
#
#
# select albums.name, COUNT(albums.name) AS num_albums FROM albums GROUP BY albums.name HAVING num_albums >1
#
# SELECT artist._id, artists.name, albums.name FROM artists
# 	INNER JOIN ON albums.artist = artists._id
# WHERE albums.name IN
# 	(SELECT albums.name FROM albums GROUP BY albums.name HAVING COUNT(albums.name) > 1)
# ORDER BY albums.name, artists.name

#  ============================================================================================================================================

# import sqlite3
#
# db = sqlite3.connect('contacts.sqlite')  # create or if not open db
# db.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)')
# db.execute('INSERT INTO contacts (name, phone, email) values ("matt", 0779196776, "matt@email.com")')
# db.execute('INSERT INTO contacts values ("harmony", 0779195543, "harmony@email.com")')
#
# cursor = db.cursor() # cursor is a generator which produces an iterable result
#
# cursor.execute('SELECT * FROM contacts')
# # print(cursor.fetchall())
#
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
#
# for name, phone, emails in cursor:   # unpack the tuple returned
#     print(name)
#     print(phone)
#     print(emails)
#     print('----' * 10)
#
# cursor.close()
# db.commit()
# db.close()

#  ============================================================================================================================================

# import sqlite3
#
# db = sqlite3.connect('contacts.sqlite')  # create or if not open db
#
# update_sql = "UPDATE contacts SET email = 'email@emails.com' where contacts.phone = 77669196776"
# update_cursor = db.cursor()
# update_cursor.execute(update_sql)
# print('{0} rows updated'.format(update_cursor.rowcount))
# update_cursor.connection.commit() # commit using the cursor connection instead
# print('are connections the same? {}'.format(db==update_cursor.connection))
#
# # for row in db.execute('SELECT * from contacts'):
# #     print(row)
#
# for name, phone, email in db.execute('SELECT * from contacts'):
#     print(name)
#     print(phone)
#     print(email)
#     print('--' * 10)
#
# db.close()

#  ============================================================================================================================================
#  SQLite with python - 3 (SQL injection attacks)
#  ============================================================================================================================================

# using the execute command instead of executescript will prevent more than one command from running
# using placeholders (?) and parameter subsitution help python sanitize the input
# never build a SQL string when the parameters sent may come from outside the code ie. provided by a user string or passed into the system using a function
# to use placeholders all that is required is a ? in the sql query and a tuple in the execute command with the required parameters


# import sqlite3
#
# db = sqlite3.connect('contacts.sqlite')  # create or if not open db
#
# new_email = 'bob@emails.com'
# new_phone = input('Please enter a phone number - ')
#
# # update_sql = "UPDATE contacts SET email = '{}' where phone = {}".format(new_email, new_phone)
# # update_sql = "UPDATE contacts SET phone = {} where email = '{}'".format(new_phone, new_email)
# update_sql = "UPDATE contacts SET email = ? where phone = ?"
# print(update_sql)
#
# update_cursor = db.cursor()
# update_cursor.execute(update_sql, (new_email, new_phone))
#
# print('{0} rows updated'.format(update_cursor.rowcount))
# update_cursor.connection.commit() # commit using the cursor connection instead
# print('are connections the same? {}'.format(db==update_cursor.connection))
#
# # for row in db.execute('SELECT * from contacts'):
# #     print(row)
#
# for name, phone, email in db.execute('SELECT * from contacts'):
#     print(name)
#     print(phone)
#     print(email)
#     print('--' * 10)
#
# db.close()

#  ============================================================================================================================================
#  execute with single value tuple
#  ============================================================================================================================================

import sqlite3

conn = sqlite3.connect('contacts.sqlite')

name = input('Please enter your name - ')
# select_sql = 'select * from contacts where contacts.name = ?'
select_sql = 'select * from contacts where contacts.name LIKE ?' # makes it none case sensitive

for row in conn.execute(select_sql, (name,)):
    print(row)

conn.close()

#  ============================================================================================================================================