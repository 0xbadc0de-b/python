#!python3
#-*- coding: utf-8 -*-

f = open( "fileList.txt", "r")
lines = f.readlines()

for line in lines:
    print( line.strip() )