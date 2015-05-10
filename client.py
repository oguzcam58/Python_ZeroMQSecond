import zmq

context = zmq.Context()

print "Connecting to hello world server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print "Connected to hello world server..."

while True:
	request = raw_input("Please enter what you want to say... ")
	socket.send(request)
	message = socket.recv();
	print (message)

socket.close()