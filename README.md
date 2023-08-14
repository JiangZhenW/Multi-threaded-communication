# Multi-threaded-communication
Multi-threaded communication、web crawler

This project is based on the producer-consumer model of multi-threaded network communication and web crawler. 
First, the web crawler on the client acts as a producer and crawls images from the web. 
In the next step, the client, as a consumer, sends the local images to the server through socket network communication, and the server uses the trained deep learning model to check the faces of the images and sends the detection results to the client.
