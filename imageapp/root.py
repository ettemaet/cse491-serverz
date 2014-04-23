import quixote
from quixote.directory import Directory, export, subdir

from . import html, image

class RootDirectory(Directory):
    _q_exports = []

    @export(name='')                    # this makes it public.
    def index(self):
        index = image.get_latest_img_index()
        data = {'index' : index}
        return html.render('index.html', data)

    @export(name='upload')
    def upload(self):
        return html.render('upload.html')

    @export(name='listimages')
    def listimages(self):
        data = image.get_all_images()
        print "...................stuff being sent: "
        print data
        return html.render('listimages.html', data)

    @export(name='upload_receive')
    def upload_receive(self):
        request = quixote.get_request()

        the_file = request.form['file']
        filetype = the_file.orig_filename.split('.')[1]
        imgName  = request.form['imgName']
        imgDesc  = request.form['imgDesc']
        print "Image Name: ", imgName
        print "Image Desc: ", imgDesc
        if (filetype == 'tif' or filetype == 'tiff'):
            filetype = 'tiff'
        elif filetype == 'jpeg' or filetype == 'jpg':
            filetype = 'jpg'
#        else:
#            return
        print 'File Type: ' + filetype
        print dir(the_file)
        print 'File Name: ', the_file.base_filename
        data = the_file.read(int(1e9))

        image.add_image(data, filetype, imgName, imgDesc)

        return quixote.redirect('./')

    # Not in use any more.
    @export(name='image')
    def image(self):
        img = image.get_latest_image()
        index = img[0]
        print "index!!!!!!!!!!: ", index
        name, desc = image.get_image_info(index)
        info = [index, name, desc]
        data = {'pic' : info}
        return html.render('image.html', data)

    @export(name='image_raw')
    def image_raw(self):
        response = quixote.get_response()
        img = image.get_latest_image()
        response.set_content_type('image/%s' % img[2])
        return img[1]


    @export(name='get_image')
    def get_image(self):
        request = quixote.get_request()

        the_int = int(request.form['special'])
        img = image.get_image(the_int)
        return img[0]

    @export(name='viewPic')
    def viewPic(self):
        request = quixote.get_request()
        the_int = image.get_latest_img_index()
        name, desc = image.get_image_info(the_int)
        info = [the_int, name, desc]

        data = {'pic' : info}

        return html.render('viewPic.html', data)

