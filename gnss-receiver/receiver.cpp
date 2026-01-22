#include <zmq.hpp>
#include <iostream>

int main() {
	zmq::context_t context{1};
	// SUB socket
	zmq::socket_t sub{context, zmq::socket_type::sub};
	// localhost for demo
	sub.connect("tcp://localhost:5555");
       	// Topic the receiver is subscribing to
    	sub.set(zmq::sockopt::subscribe, "GNSS");
	

	while (true) {
		// Each message contains 3 frames: topic, iq signal, and metadata
		zmq::message_t topic;
		zmq::message_t payload;
		zmq::message_t metadata;
		
		sub.recv(topic);
		sub.recv(payload);
		sub.recv(metadata);

		std::cout << "Topic: " << topic.to_string() << std::endl;
		std::cout << "Payload size: " << payload.size() << " bytes\n";
		std::cout << "Metadata size: " << metadata.size() << " bytes\n";
	}
}
