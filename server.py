import zmq
import json

def wrongRequest(socket):
	socket.send("Wrong request")

context = zmq.Context()

print "Starting server..."

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print "Started server..."

while True:
	message = socket.recv()
	print "Got: ", message

	request = dict()
	request = json.loads(message)

	function = request["function"]
	if (function != None):
		if (function == "1"):
			args = request["args"]
			result = int(args[0]) + int(args[1])
			print result
			socket.send(str(result))
		# elif (function == 2):
		# elif (function == 3):
		# elif (function == 4):
		# else:
		else:
			wrongRequest(socket)
	else:
		wrongRequest(socket)
