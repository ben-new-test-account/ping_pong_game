#!/usr/bin/python
import time

######################
# Write Ping After Here
######################

######################
# Write Pong After Here
######################

class Pong:
    @staticmethod
    def bounce():
        print "Pong"
        time.sleep(1)
        Ping.bounce()

Ping.bounce()
