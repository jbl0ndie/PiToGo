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
    bus_check.check_bus() # this should call the main function from bus_check
    # do your stuff
    sc.enter(30, 1, periodic_poll, (sc,)) # 30 sec poll, need to understand syntax

s.enter(30, 1, periodic_poll, (s,)) # 30 sec poll
s.run()

"""
def main():
    
    return 0

if __name__ == '__main__':
    main()
"""
