import zmq
import numpy as np
import json

port = "5555"
topic_filter = "iq"  # same topic as publisher

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://localhost:{port}")

# subscribe to the topic (filter by prefix)
socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

while True:
    # receive multipart message
    frames = socket.recv_multipart()
    
    # extract frames
    topic = frames[0].decode("utf-8")
    iq_bytes = frames[1]
    metadata_bytes = frames[2]
    
    # reconstruct IQ array
    iq_array = np.frombuffer(iq_bytes, dtype=np.complex64)
    
    # reconstruct metadata
    metadata = json.loads(metadata_bytes.decode("utf-8"))
    
    # print for testing
    print(f"Received topic: {topic}")
    print(f"IQ array shape: {iq_array.shape}, first 5 samples: {iq_array[:5]}")
    print(f"Metadata: {metadata}")
    print("="*50)

