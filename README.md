# Multi-threaded-communication
Multi-threaded communication、web crawler

This project is based on the producer-consumer model of multi-threaded network communication and web crawler. 

First, the web crawler on the client acts as a producer and crawls images from the web. 

In the next step, the client, as a consumer, sends the local images to the server through socket network communication, and the server uses the trained deep learning model to check the faces of the images and sends the detection results to the client.

# Useage
1: The code in the server folder you need to deploy to the server side.

2: Other code you need to deploy to the client.

3: Run my_server.py on the server side firstly, and then run main.py on the client side.

