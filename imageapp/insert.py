# insert an image into the database.

import sqlite3

# connect to the already existing database
db = sqlite3.connect('images.sqlite')

db.execute('DROP TABLE image_store')
db.commit()
db.execute('CREATE TABLE image_store (i INTEGER PRIMARY KEY, image BLOB, filetype TEXT, imgName TEXT, imgDesc TEXT)')
db.commit()
# configure to allow binary insertions
db.text_factory = bytes

# grab whatever it is you want to put in the database
#r = open('dice.png', 'rb').read()
#vars = (r, "png")

print '....inserting.....'
# insert!
#db.execute('INSERT INTO image_store (image) VALUES (?)', (r,))
#db.execute('INSERT INTO image_store(image, filetype) VALUES(?,?)', vars)
#db.commit()
#db.execute('UPDATE image_store SET filetype="png" WHERE i=1')
#db.commit()
