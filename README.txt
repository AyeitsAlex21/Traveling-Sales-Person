#####################################################################################################################################
# README.txt                                                                                                                        #
# Author(s): Niklaas Cotta                                                                                                          #
# TEAM NASAK                                                                                                                        #
# CIS422 FA21 -- Project 1                                                                                                          # 
# Creation Date: 10/30/21                                                                                                           #
# File Description:  This is the master README. It explains what is in the directory, along with some other information             #
#   This contains a system description, how to use the application, list of subdirectories, and installation instructions           #
#   It combines parts from the README.txt, Programmer_Documentation.txt, Installation_Instructions.pdf, and User_Documentation.pdf  #
#####################################################################################################################################

####################################################################################################################################################################################

System Description:
   Our system is composed of 3 modules. Genetic Algorithm, Web Application, and Google Maps API. The purpose of this system is to provide a near-optimal routing algorithm. The program 
   accepts several locations (via a search bar or point-and-click) and will generate a path of minimum distance between the routes, starting from the first location input and ending in 
   the same place. It does so via a genetic algorithm that pulls information from Google Maps.
  
####################################################################################################################################################################################
   
How to use this application:
   The web application contains two main buttons:
   
   1) Add Location -- select a location on the embedded map.
      i)   added locations will be displayed below the Add Location button.
      ii)  the first location you add will be your assumed starting point.
      iii) the algorithm will assume that you return to your starting point after the last location.
      iv)  if you add a location, you may delete that location individually.
   
   2) Calculate Path -- determine the shortest path from the list of locations you've added.
      i)   the path will be represented on the map. locations will be listed alphabetically. there is a small flaw with the alphabetical representation. The first location (A), 
             is overwritten by the last location. Therefore, if you have four locations (A, B, C, D), then E will represent the path returning to the first location. E overwrites the 
             first location (A) since it is returning. Therefore, your circuitous path will be represented as such: (E, B, C, D, E).
      
      In addition to these functionalities, the embedded map has much of the same functionality as the vanilla google maps application.
      There are many real world applications that you can use this program for. One example would be if you have several grocery stores to shop at, and want to spend as little time   
        driving, then you can use this program to find the shortest path between grocery stores.

####################################################################################################################################################################################

Subdirectories:
  There is one subdirectory within the master folder:
  1) webapp -- this folder contains two folders containing all the files of the program
     i) api -- this folder contains all of the genetic algorithm files along with the Google Maps API request file. __pycache__ is from the python interpreter. The Dockerfile is the file used to create the container in Docker
     ii) website -- this folder contains all of the web application folders. It contains a templates folder, which contains all of the .html files that are the content of the web application. There is another Dockerfile for a second container. There is also a website.py file for Flask

####################################################################################################################################################################################

Installation/Compiling:
   This program does not need to be installed or compiled to access. It is a web application hosted via a docker hosting platform called Digital Ocean. The only thing that you need worry about is make sure that your browser is up to date. Any browser will work, but firefox is recommended. To access the website, you may visit it with this url: http://143.110.234.23:5000/. 
   
   If you would like to compile and host this web application on your own machine, you must install Docker from this website: https://docs.docker.com/get-docker/. After Docker is installed, from within the webapp folder, open up a terminal. Then type:

docker-compose up --build

This will take care of any and all installations for you. Once the docker container is built, you can access the web application being hosted on your own machine via this url: http://localhost:5000/. There are no further setup that must be done. There are no other software dependencies required as well.

TODO:
(d) how source code files relate 
to each other,
