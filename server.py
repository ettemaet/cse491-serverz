#!/usr/bin/env python
import random
import socket
import time
import urlparse

def handle_connection(conn):
    info = conn.recv(1000)
    # req is either POST or GET
    req = info.split('\r\n')[0].split(' ')[0]

    # reqType is the path extracted
    reqType = info.split('\r\n')[0].split(' ')[1]
    urlInfo = urlparse.urlparse(reqType)
    reqType = urlInfo.path
#    conn.send(reqType)

  #  conn.send(info)
    if req == 'GET':
        if reqType == '/':
            handle_slash(conn, urlInfo)
        elif reqType == '/content':
            handle_content(conn, urlInfo)
        elif reqType == '/file':
            handle_file(conn, urlInfo)
        elif reqType == '/image':
            handle_image(conn, urlInfo)
        elif reqType == '/form':
            handle_form(conn, urlInfo)
        elif reqType == '/submit':
            handle_submit(conn, urlInfo)
#        else:
#            handle_error()
    elif req == 'POST':
        handle_post(conn, info)
 #   conn.send(reqType)
    conn.close()

def handle_slash(conn, urlInfo):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n' + \
              '<h1>Hello, world.</h1>' + \
              'This is ettemaet\'s Web server.'
    conn.send(content)
    links = '\n<a href="/content">Content</a>\n' + \
            '<a href="/file">Files</a>\n' + \
            '<a href="/image">Images</a>\n'
    conn.send(links)

def handle_content(conn, urlInfo):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    info = '<h2>content</h2>'
    conn.send(info)

def handle_file(conn, urlInfo):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    info = '<h2>files</h2>'
    conn.send(info)

def handle_image(conn, urlInfo):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    info = '<h2>images</h2>'
    conn.send(info)

def handle_form(conn, urlInfo):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    getForm = "<form action='/submit' method='GET'>" + \
           "First Name:<input type='text' name='firstname'>" + \
           "Last Name:<input type='text' name='lastname'>" + \
           "<input type='submit' value='Submit Get'>" + \
           "</form>"
    conn.send(getForm)
    postForm = "<form action='/post' method='POST'>" + \
           "First Name:<input type='text' name='firstname'>" + \
           "Last Name:<input type='text' name='lastname'>" + \
           "<input type='submit' value='Submit Post'>" + \
           "</form>"
    conn.send(postForm)

def handle_submit(conn, urlInfo):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    query = urlInfo.query
    data = urlparse.parse_qs(query)

    conn.send('Hello Mr. ')
    conn.send(data['firstname'][0])
    conn.send(' ')
    conn.send(data['lastname'][0])
    conn.send('.')


def handle_post(conn, info):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
             '\r\n'
    conn.send(content)

    hello = '<h3>hello world, submitted via post</h3>'
    conn.send(hello)
    query = info.splitlines()[-1]
    data = urlparse.parse_qs(query)

    conn.send('Hello Mr. ')
    conn.send(data['firstname'][0])
    conn.send(' ')
    conn.send(data['lastname'][0])
    conn.send('.')


def main():

    s = socket.socket()         # Create a socket object
    host = socket.getfqdn() # Get local machine name
    port = random.randint(8000, 9999)
    s.bind((host, port))        # Bind to the port

    print 'Starting server on', host, port
    print 'The Web server URL for this would be http://%s:%d/' % (host, port)

    s.listen(5)                 # Now wait for client connection.

    print 'Entering infinite loop; hit CTRL-C to exit'
    while True:
        # Establish connection with client.
        c, (client_host, client_port) = s.accept()
        print 'Got connection from', client_host, client_port
        handle_connection(c)

if __name__ == "__main__":
    main()
