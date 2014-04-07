#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  requestss_test.py
#  
#  Copyright 2014 Jonathon Hodges <jonathon@weepc>
#
#  Thank you to @acarabott for the example code.
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


import requests

DEFAULT_DATA = {'status': 'No Internet connection', 'content': 'hello world'}

def getSomeData(url):
    
    try:
        
        r = requests.get(url)
    
        data = {
        'status': r.status_code,
        'content': r.content
        }
    
    except requests.ConnectionError:
        print("couldn't connect to url " + url)
        
        data = DEFAULT_DATA
        
    for item in data:
        print(item + ": " + str(data[item]))
        
if __name__ == '__main__':
    getSomeData("http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?StopCode1=56321&DirectionID=1&VisitNumber=1&ReturnList=StopPointName,LineName,DestinationText,EstimatedTime")

"""
def main():
    
    return 0

if __name__ == '__main__':
    main()
"""
