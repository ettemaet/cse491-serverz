# image handling API
import sqlite3

images = {}

def add_image(data, filetype):
    print "in add image"
    if images:
        image_num = max(images.keys()) + 1
    else:
        image_num = 0

    db = sqlite3.connect('images.sqlite')

    # configure to allow binary insertions
    db.text_factory = bytes

    # insert!
    c = db.cursor()
    c.execute('INSERT INTO image_store (image) VALUES(?)', (data,))
    db.commit()

    c.execute('SELECT * FROM image_store')
    test = c.fetchall()
    for row in test:
        print row[0]

    db.close()

    images[image_num] = [data, filetype]
    return image_num

def get_image(num):
    return images[num]

def get_latest_image():
    print "in get_latest_image"
    # connect to database
    db = sqlite3.connect('images.sqlite')

    # configure to retrieve bytes, not text
    db.text_factory = bytes

    # get a query handle (or "cursor")
    c = db.cursor()

    # select all of the images
    c.execute('SELECT i, image FROM image_store ORDER BY i DESC LIMIT 1')

    # grab the first result (this will fail if no results!)
    i, image = c.fetchone()
    test = [image, 'png']
    """
    print 'i: '
    print i
    c.execute('SELECT * FROM image_store')
    test = c.fetchall()
    for row in test:
        print row
    print type(image)
#    open(i, 'w').write(image)
    """
    return test
    """
    image_num = max(images.keys())
    print type(images[image_num])
    print images[image_num]
    return images[image_num]
    """
