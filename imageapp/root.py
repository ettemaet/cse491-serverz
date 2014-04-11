import quixote
from quixote.directory import Directory, export, subdir

from . import html, image

class RootDirectory(Directory):
    _q_exports = []

    @export(name='')                    # this makes it public.
    def index(self):
        return html.render('index.html')

    @export(name='upload')
    def upload(self):
        return html.render('upload.html')

    @export(name='listimages')
    def listimages(self):
        imagevars= {"images" : image.images}
        return html.render('listimages.html', imagevars)

    @export(name='upload_receive')
    def upload_receive(self):
        request = quixote.get_request()
        print request.form.keys()

        the_file = request.form['file']
        filetype = the_file.orig_filename.split('.')[1]
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

        image.add_image(data, filetype)

        return quixote.redirect('./')

    @export(name='image')
    def image(self):
        return html.render('image.html')

    @export(name='image_raw')
    def image_raw(self):
        response = quixote.get_response()
        img = image.get_latest_image()
        response.set_content_type('image/%s' % img[1])
        return img[0]

    @export(name='get_image')
    def get_image(self):
        request = quixote.get_request()

        the_int = int(request.form['special'])
        img = image.get_image(the_int)
        return img[0]
