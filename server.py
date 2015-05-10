import zmq
import json

wrongRequest = "Wrong request"
wrongArguments = "Wrong arguments"

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
			try:
				args = request["args"]
				result = int(args[0]) + int(args[1])
				socket.send(str(result))
			except:
				socket.send(wrongArguments)
		elif (function == "2"):
			try:
				args = request["args"]
				result = int(args[0]) - int(args[1])
				socket.send(str(result))
			except:
				socket.send(wrongArguments)
		elif (function == "3"):
			try:
				args = request["args"]
				result = int(args[0]) * int(args[1])
				socket.send(str(result))
			except:
				socket.send(wrongArguments)
		elif (function == "4"):
			try:
				args = request["args"]
				result = int(args[0]) / int(args[1])
				socket.send(str(result))
			except:
				socket.send(wrongArguments)
		else:
			socket.send(wrongRequest)
	else:
		socket.send(wrongRequest)
