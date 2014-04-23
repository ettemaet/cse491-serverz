# image handling API
import sqlite3

def add_image(data, filetype, imgName, imgDesc):
    print "in add image"

    db = sqlite3.connect('images.sqlite')
    c = db.cursor()

    c.execute('SELECT i FROM image_store ORDER BY i DESC LIMIT 1')
    row = c.fetchone()

    if row == None:
        index = 0
    else:
        index = row[0]+1

    # configure to allow binary insertions
    db.text_factory = bytes

    # insert!
    vars = (index, data, filetype, imgName, imgDesc)
    c.execute('INSERT INTO image_store (i, image, filetype, imgName, imgDesc) VALUES(?,?,?,?,?)', vars)
    db.commit()

    db.close()

#i    images[image_num] = [data, filetype]
    print "current number of images: "
    print index + 1
    return index

def get_image(num):
    db = sqlite3.connect('images.sqlite')
    db.text_factory = bytes

    c = db.cursor()
    c.execute('SELECT i, image, filetype FROM image_store WHERE i=? LIMIT 1', (num,))
    i, image, filetype = c.fetchone()
    result = [image, filetype]
    db.close()

    return result

def get_latest_image():
    print "in get_latest_image"
    # connect to database
    db = sqlite3.connect('images.sqlite')

    # configure to retrieve bytes, not text
    db.text_factory = bytes

    # get a query handle (or "cursor")
    c = db.cursor()

    # select all of the images
    c.execute('SELECT i, image, filetype FROM image_store ORDER BY i DESC LIMIT 1')

    # grab the first result (this will fail if no results!)
    i, image, filetype = c.fetchone()
    result = [i, image, filetype]

    return result

def get_all_images():
    data = {}
    data["dict"] = {}
    db = sqlite3.connect('images.sqlite')
    c = db.cursor()
    db.text_factory = bytes

    c.execute('SELECT i, imgName, imgDesc FROM image_store ORDER BY i ASC')

    for row in c:
        index = str(row[0])
        name  = row[1]
        desc  = row[2]

        data["dict"][index] = [index, name, desc]
        print "image: ", row[0], name, desc
    db.close()
    return data

def get_image_info(num):
    db = sqlite3.connect('images.sqlite')
    c  = db.cursor()
    db.text_factory = bytes

    c.execute('SELECT imgName, imgDesc FROM image_store WHERE i=?', (num, ))

    imgName, imgDesc = c.fetchone()
    result = [imgName, imgDesc]

    return result

def get_latest_img_index():
    db = sqlite3.connect('images.sqlite')
    c = db.cursor()

    c.execute('SELECT i FROM image_store ORDER BY i DESC LIMIT 1')
    row = c.fetchone()
    return row[0]

