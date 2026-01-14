import zmq
import random
import sys
import time

# ZMQ DOCs: https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

port = "5555" # Port where zmq is listening

# Initializing zeromq "engine" (context) + initializing publisher only module
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

