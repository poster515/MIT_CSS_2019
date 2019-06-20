These are files created during a shortcourse at MIT. 

server.js is a Javascript server hosted via node.js which serves as a proxy for locahost:9000/?url=<your_url> traffic. 
The proxy will parse the request, resend the relevant portions to the destination server and repackage and return the data.

simple_system.py is a simple system representing a tank, fed by a constant volumetric pump which is controlled by a simple 
controller which turns on when the tank level drops below a setpoint, and offf when tank level exceeds another setpoint. 
The tank is assumed constantly draining by a varying amount every time step (1 ms). 
