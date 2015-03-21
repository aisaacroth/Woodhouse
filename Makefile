# Makefile for the Jarvis Home automation system.
#
# Author: Alexander Roth
# Date:   2015-03-21

CC  = g++
CXX = g++

INCLUDES = 

CFLAGS   = -g -Wall $(INCLUDES)
CXXFLAGS = -g -Wall $(INCLUDES)

LDFLAGS = -g
LDLIBS  = 

jarvis: main.o
	$(CC) $(LDFLAGS) main.o -o jarvis

main.o: main.cpp
	$(CC) -c $(CXXFLAGS) main.cpp

.PHONY: clean
clean:
	rm -rf *~ a.out jarvis *.o

.PHONY: all
all: clean jarvis
