#!/usr/bin/env python

import socket, select, Queue

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSocket.setblocking(0)
tcpSocket.bind(("0.0.0.0", 8000))
tcpSocket.listen(2)

inputs = [tcpSocket]
outputs = []
messageQueues = {}
while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
                if s is tcpSocket:
                        (client, (ip, port)) = tcpSocket.accept()

                        print "Received connection from: ", ip, port
                        client.setblocking(0)
                        inputs.append(client)
                        messageQueues[client] = Queue.Queue()
                        print "Starting ECHO output ... "
                else:
                        data = s.recv(2048)
                        if data:
                                print "Client sent: ", data
                                messageQueues[s].put(data)
                                if s not in outputs:
                                        outputs.append(s)
                        else:
                                if s in outputs:
                                        outputs.remove(s)
                                inputs.remove(s)
                                s.close()
                                del messageQueues[s]
        for s in writable:
                try:
                        nextMsg = messageQueues[s].get_nowait()
                except Queue.Empty:
                        outputs.remove(s)
                else:
                        s.send(nextMsg)
        for s in exceptional:
                inputs.remove(s)
                if s in outputs:
                        outputs.remove(s)
                s.close()
                del messageQueues[s]
