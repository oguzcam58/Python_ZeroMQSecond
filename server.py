import zmq

context = zmq.Context()

print "Starting server..."

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print "Started server..."

while True:
	message = socket.recv()
	print "Got: ", message

	# Send the reply.
	socket.send(message)