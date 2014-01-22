#!/usr/bin/env python
import random
import socket
import time

def handle_connection(conn):
    info = conn.recv(1000)
    req = info.split('\r\n')[0].split(' ')[0]
    reqType = info.split('\r\n')[0].split(' ')[1]

#    conn.send(info)
    if req == 'GET':
        if reqType == '/':
            handle_slash(conn, reqType)
        elif reqType == '/content':
            handle_content(conn, reqType)
        elif reqType == '/file':
            handle_file(conn, reqType)
        elif reqType == '/image':
            handle_image(conn, reqType)
#        else:
#            handle_error()
    elif req == 'POST':
        handle_post(conn)
    conn.close()

def handle_slash(conn, reqType):
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

def handle_content(conn, reqType):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    info = '<h2>content</h2>'
    conn.send(info)

def handle_file(conn, reqType):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    info = '<h2>files</h2>'
    conn.send(info)

def handle_image(conn, reqType):
    content = 'HTTP/1.0 200 OK\r\n' + \
              'Content-type: text/html\r\n' + \
              '\r\n'
    conn.send(content)
    info = '<h2>images</h2>'
    conn.send(info)

def handle_post(conn):
    content = 'HTTP/1.0 200 OK\r\n'
#              'Content-type: text/html\r\n' + \
#             '\r\n'
    conn.send(content)
    info = '<h2>hello world</h2>'
    conn.send(info)

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
#        print c.recv(1000)
        print 'Got connection from', client_host, client_port
        handle_connection(c)

if __name__ == "__main__":
    main()
