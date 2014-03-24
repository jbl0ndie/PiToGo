#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bus_check.py
#  
#  Copyright 2014 Jonathon Hodges <jonathon@weepc>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



#def main():
#   
#   return 0

#if __name__ == '__main__':
#   main()

from time import strftime, localtime # needed to give human time tools
import requests

# data = json.load(urllib2.urlopen('http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?StopCode1=56321&DirectionID=1&VisitNumber=1&ReturnList=StopCode1,StopPointName,LineName,DestinationText,EstimatedTime,MessageUUID,MessageText,MessagePriority,MessageType,ExpireTime'))

stop_code = 56321 # in the future, this will be selectable or something

# payload = {'key1': 'value1', 'key2': 'value2'} example from requests docs

payload = {'StopCode1': stop_code} #form the JSON request payload from a dict
#~ reply = requests.get("http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?DirectionID=1&VisitNumber=1&ReturnList=StopPointName,LineName,DestinationText,EstimatedTime", params=payload) 
"""
I couldn't make requests.get accept dict value separated by commas
so have hard coded it. The bits I want to change are stop numbers anyway.
"""

# request string to tfl, note berkshire road is 56321, Gt Tichfield St is 51889


def check_bus():
    data = requests.get("http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?DirectionID=1&VisitNumber=1&ReturnList=StopPointName,LineName,DestinationText,EstimatedTime", params=payload) 
    
    reply = data.text # sets the reply as a global variable
    sep = reply.split(',') # separate the reply into parts in a list

    def unixtime_to_human(epoch):
    
        """
    (int) -> str
    
    Take Unix time and return human readable time.
    
    >>>unix_to_human(1395595339)
        Sun, 23 Mar 2014 17:22:19 GMT
        """
    
        return strftime("%a, %d %b %Y %H:%M:%S +0000", localtime(epoch / 1000))

    print("Bus: " + sep[4].strip('"[]')) # print the first bus number in list
    print("Destination: " + sep[5].strip('"[]')) # print the first destination in list
    
    bus_time_unix = sep[6] # set bus to 1st bus arrival time, including the ] delimiter
    bus_time_unix = int(bus_time_unix[:13]) # hack off the last character and convert to int
    
    tfl_time_now_unix = sep[2] # get the current UNIX time from tfl timestamp
    tfl_time_now_unix = int(tfl_time_now_unix[:13]) # strip trailing ] and convert to int
    
    time_to_bus_unix =  bus_time_unix - tfl_time_now_unix # time from now until next bus as unix
    
    def bus_time_mins(time_to_bus):
        return time_to_bus_unix // 1000 // 60 # convert tfl's time in milliseconds to minutes
    
    # Print the current TfL time to verify we're current
    print("TfL time is: " + str(unixtime_to_human(tfl_time_now_unix)))
    print("Next bus in: " + str(bus_time_mins(time_to_bus_unix)) + " minutes")
    

#~ def check_function(): # test for function call from other module when tfl feed is down
    #~ print("hello")


if __name__ == '__main__':
	print('## Now running bus_check in debug mode ## \n')
	check_bus() # get a normal request

""" ## Spare debug bits ##
print(reply) # print a whole reply for debug 
print(sep) # print the whole list for debug 
print(bus_time) # print unix time for bus arrival for debug
print(time_now) # print unix time now for debug

print("time to bus " + str(time_to_bus)) print time in UNIX timestamp
"""
