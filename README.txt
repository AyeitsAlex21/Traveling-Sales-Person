Author(s): Niklaas Cotta
TEAM NASAK
CIS422 FA21 -- Project 1
Creation Date: 10/30/21
File Description:  This is the master README. It explains what is in the directory, along with some other information

System Description:
   Our system is composed of 3 modules. Genetic Algorithm, Web Application, and Google Maps API. The purpose of this system is to provide a near-optimal routing algorithm. The program 
   accepts several locations (via a search bar or point-and-click) and will generate a path of minimum distance between the routes, starting from the first location input and ending in 
   the same place. It does so via a genetic algorithm that pulls information from Google Maps.

Subdirectories:
  There is one subdirectory within the master folder:
  1) webapp -- this folder contains two folders containing all the files of the program
     i) api -- this folder contains all of the genetic algorithm files along with the Google Maps API request file. __pycache__ is from the python interpreter. The Dockerfile is the file used to create the container in Docker
     ii) website -- this folder contains all of the web application folders. It contains a templates folder, which contains all of the .html files that are the content of the web application. There is another Dockerfile for a second container. There is also a website.py file for Flask

TODO:
v. Necessary steps to compile the source code and run the program 
vi. Any additional required setup 
vii. Software dependencies such as the version of the compiler 
