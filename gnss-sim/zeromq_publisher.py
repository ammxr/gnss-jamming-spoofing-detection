import zmq
import time


# ZMQ DOCs: https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

port = "5555" # Port where zmq is listening

# Initializing zeromq "engine" (context) + initializing publisher only module
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

time.sleep(10) # 10 seconds for sub to connect

def publish_iq(topic, iq, metadata):
    # 3 Frames (func parameters), the common  send_string() or send() methods only supports single frame, so we use send_multipart() 
    
    # zmq expects bytes
    socket.send_multipart([
        topic.encode("utf-8"),                  
        iq.tobytes(),                           # np.ndarray uses tobytes() to convert complex64 -> bytes
        json.dumps(metadata).encode("utf-8"),   # Json dumps used as dict cannot be encoded otherwise... Python obj -> json string -> bytes
    ])
