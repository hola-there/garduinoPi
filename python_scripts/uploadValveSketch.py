#!/usr/bin/python
import subprocess
bashCommand = "sudo pio run -e uno -t upload -d /opt/garduinoPi/projects/valueTime/src/valve.cpp"

process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashOutputToFile =  "uploadValveResult.txt < %s" % output

anotherProcess = subprocess.Popen(bashOutputToFile.split())
