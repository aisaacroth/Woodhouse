# Makefile for the Jarvis Home automation system.
#
# Author: Alexander Roth
# Date:   2015-03-21

.PHONY: default
jarvis:

.PHONY: clean
clean:
	rm -rf *~ a.out jarvis *.o

.PHONY: all
all:
	clean jarvis
