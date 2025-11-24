Contact Info
============

Group Members & Email Addresses:

    Krishna Angal, aean231@uky.edu
    Lucy Rosys, lero241@uky.edu
    Andres Aguirre, aag245@uky.edu

Versioning
==========

Github Link: https://github.com/A-Aguirre245/CS371_Project/

General Info
============
Run the server code to start server, and read the IP address and port number from the output. Run the client code to start the client, and input the IP address and port number to the game window. Game will start when both clients have connected.

Install Instructions
====================

Run the following line to install the required libraries for this project:

`pip3 install -r requirements.txt`

Known Bugs
==========
- Ball position diverges when the paddle position has not updated between clients quickly enough
    -This can also cause scores to become different, and one player to win while the other game is still in progress
