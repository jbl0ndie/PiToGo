#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  periodic_check.py
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

import bus_check # import the bus checker module
import sched, time

s = sched.scheduler(time.time, time.sleep)

def periodic_poll(sc): # this must call a function that does what we want
    bus_check.bus_time_mins() # this is broken
    # do your stuff
    sc.enter(2, 1, periodic_poll, (sc,)) # note this is 2 sec poll

s.enter(2, 1, periodic_poll, (s,)) # note this is 2 sec poll
s.run()

"""
def main():
    
    return 0

if __name__ == '__main__':
    main()
"""

timeout = 2.0 # Two seconds

def doWork():
    i = 0
    print(i)
    i = i + 1
    pass

l = task.LoopingCall(doWork)
l.start(timeout) # call every two seconds

reactor.run()
