#!/usr/bin/python
import time

######################
# Write Ping After Here
######################

class Ping:
    @staticmethod
    def bounce():
        print "Ping"
        time.sleep(1)
        Pong.bounce()

######################
# Write Pong After Here
######################

Ping.bounce()
