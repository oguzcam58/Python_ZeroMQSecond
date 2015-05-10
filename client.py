import zmq
import json

context = zmq.Context()

print "Connecting to hello world server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print "Connected to hello world server..."

while True:
	info = dict()
	info["function"] = raw_input("Choose a function you want to use? 1: Sum, 2: Subtract, 3: Multiply, 4: Divide")
	arguments = []
	arguments.append(raw_input("Enter first number"))
	arguments.append(raw_input("Enter second number"))
	info["args"] = arguments
	socket.send(json.dumps(info))
	message = socket.recv();
	print (message)

socket.close()