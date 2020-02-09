# CNT-4731 Project 1

Jason Davila
PID: 4953994

# PROJECT REPORT

client.py

The client is executed with three input parameters, hostname/IP address, port number, and the file to be read from. A socket is created, then connected to a server witht the corresponding port number. The file is opened and then its contents are sent in large chunks over to the server until there is no more data left to be read. once all the data is sent, the client's job is done in this case and the socket is closed.

server.py

The entry point at the time of writing this report begins at around line 34. The first thing that we do is validate the port number to make sure it is above 1023. Then we bind to the host and port and listen for any valid connections. once we hit the forever loop, we hang out at accept() until we catch a client. Once we have one on the line, we create a directory to prep for the data we're about to recieve from the client (if a dir soes not already exist). We create a subthread of our data recieving method and begin running it. We open a file whose count depends on how many files were created before it, and we write the incoming clients' data into it. Once we stop recieving data, we close the connection and go back to listening for more clients.

PROBLEMS

The most significant problem I ran into involved the struct module. Online I found an incredibly effective and simpler way to bridge my server and client using pack and unpack from struct (https://stackoverflow.com/questions/42459499/what-is-the-proper-way-of-sending-a-large-amount-of-data-over-sockets-in-python). I didn't think it counted as a high level solution so I implemented it. Despite working perfectly fine on my end, the autograder was not too happy with it. I was honestly stuck for about 4 hours trying to figure out why the autograder ketp failing me until I remembered that you're probably testing my server against other clients and vice versa, where the expected order and contents of the send and recv were different. Another issue I had is with timeouts in the client side. 

RESOURCES

https://stackoverflow.com/questions/42459499/what-is-the-proper-way-of-sending-a-large-amount-of-data-over-sockets-in-python

https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
