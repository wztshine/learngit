import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} send:".format(self.client_address), self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('Error: ',e)
                break

if __name__ == '__main__':
    host,port = 'localhost',9999
    server = socketserver.ThreadingTCPServer((host,port),MyTCPHandler)
    server.serve_forever()
