# GoogleSearchEngine

Mimic Google's search engine using python, html, and css.

This was a project done for the CSC326: Programming Languages Course.
We re-created Google's Search engine by using Bottle.

# Lab 2

Public IP address of live web server: 35.172.205.127

Instance created: Saturday, October 27, 2018

To view search engine, follow these steps:

1. Change working directory to lab2_group_24
2. chmod 400 my_key.pem
3. ssh -i my_key.pem ubuntu@35.172.205.127
4. Change working directory to lab2_group_24 (cd lab2_group_24)
5. Run frontend.py (sudo python frontend.py)
6. Go to http://35.172.205.127:80/

Benchmark Setup:

1. Used the following commands on Ubuntu:

a. sudo apt-get install apache2-utils
b. sudo apt-get install sysstat dstat

2. On another computer, used this command: ab -n 1000 -c 50 http://35.172.205.127:80/?keywords=csc326+lab2

3. On Ubuntu, used this command to get utilization of CPU, memory, disk IO, 
   and network when max performance is sustained: dstat -cmdn
   
Benchmarking results can be found in RESULT file. 




