# GoogleSearchEngine

Mimic Google's search engine using python, html, and css.

This was a project done for the CSC326: Programming Languages Course.
We re-created Google's Search engine by using Bottle.

# Lab 2

AWS:

Instance created: Monday, November 12, 2018

Public IP address of live web server: 54.161.255.192

Public DNS: ec2-54-161-255-192.compute-1.amazonaws.com   

To view search engine, go to http://54.161.255.192:80/ or http://ec2-54-161-255-192.compute-1.amazonaws.com.

Benchmark Setup:

1. Used the following commands on Ubuntu:

a. sudo apt-get install apache2-utils
b. sudo apt-get install sysstat dstat

2. On another computer, used this command: ab -n 1000 -c 50 http://35.172.205.127:80/?keywords=csc326+lab2

3. On Ubuntu, used this command to get utilization of CPU, memory, disk IO, 
   and network when max performance is sustained: dstat -cmdn
   
Benchmarking results can be found in RESULT file. 

# Lab 3

Benchmark Setup:

1. Used the following commands on Ubuntu:

a. sudo apt-get install apache2-utils
b. sudo apt-get install sysstat dstat

2. On another computer, used this command: ab -n 1000 -c 50 http://54.161.255.192:80/?keywords=csc326+ece
   
Benchmarking results can be found in LAB3RESULT file.

Frontend:

The frontend searches the keywords against the persistent storage generated by the backend by converting dump.rdb to a json file (dump.json). The rdb file is converted to a json file using the command 'rdb --command json dump.rdb'. To use this command, rdbtools must be installed using 'pip install rdbtools python-lzf'. The frontend parses this json file to get the URLs, and these URLs are displayed using static pagination. 

Information on how to access the frontend on AWS and the Public DNS of the frontend on AWS will be provided when marking for this lab starts.

The frontend from lab 2 can be found at http://54.161.255.192:80/ or http://ec2-54-161-255-192.compute-1.amazonaws.com.

Backend:



