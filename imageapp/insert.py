# insert an image into the database.

import sqlite3

# connect to the already existing database
db = sqlite3.connect('images.sqlite')

db.execute('DROP TABLE IF EXISTS image_store')
db.commit()
db.execute('CREATE TABLE image_store (i INTEGER PRIMARY KEY, image BLOB, filetype TEXT)')
#db.execute('CREATE TABLE image_store (i INTEGER PRIMARY KEY, image BLOB, type TEXT)')
db.commit()
# configure to allow binary insertions
db.text_factory = bytes

# grab whatever it is you want to put in the database
r = open('dice.png', 'rb').read()

print '....inserting.....'
# insert!
db.execute('INSERT INTO image_store (image) VALUES (?)', (r,))
#db.execute('INSERT INTO image_store(image, type) VALUES(r, "png")')
db.commit()
#db.execute('UPDATE image_store SET filetype="png" WHERE i=1')
#db.commit()
