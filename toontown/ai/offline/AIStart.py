class game:
    name = "toontown"
    process = "ai"
builtins.game = game()

import time
import os
import sys
import string
import getopt

import ihooks
ihooks.install()

from direct.directnotify import RotatingLog

try:
    opts, pargs = getopt.getopt(sys.argv[1:], '', [
        'mdip=',
        'mdport=',
        'esip=',
        'esport=',
        'logpath=',
        'district_number=',
        'district_name=',
        'ssid=',
        'min_objid=',
        'max_objid=',
        'dcfile=',
        ])
except Exception as e:
    print(e)
    print(helpString)
    sys.exit(1)

if len(opts) < 4:
    print(helpString)
    sys.exit(1)

mdip = "localhost"
mdport = 6666
esip = "localhost"
esport = 4343
logpath = ""
dcFileNames = []
districtType = 0

for opt in opts:
    flag, value = opt
    if (flag == '--district_number'):
        districtNumber = int(value)
    elif (flag == '--district_name'):
        origDistrictName = value
        districtName = string.replace(value, "_", " ")
    elif (flag == '--logpath'):
        logpath = value
    elif (flag == '--ssid'):
        ssId = int(value)
    elif (flag == '--min_objid'):
        minObjId = int(value)
    elif (flag == '--max_objid'):
        maxObjId = int(value)
    elif (flag == '--mdip'):
        mdip = value
    elif (flag == '--mdport'):
        mdport = int(value)
    elif (flag == '--esip'):
        esip = value
    elif (flag == '--esport'):
        esport = int(value)
    elif (flag == '--dcfile'):
        dcFileNames.append(value)
    else:
        print("Error: Illegal option: " + flag)
        print(helpString)
        sys.exit(1)

if not dcFileNames:
    dcFileNames = ['otp.dc', 'toon.dc']

logfile = logpath + 'aidistrict_' + origDistrictName + "_" +str(districtNumber)

class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log
    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()
    def flush(self):
        self.log.flush()
        self.orig.flush()

log = RotatingLog.RotatingLog(logfile, hourInterval=24, megabyteLimit=1024)
logOut = LogAndOutput(sys.__stdout__, log)
logErr = LogAndOutput(sys.__stderr__, log)
sys.stdout = logOut
sys.stderr = logErr

from pandac.PandaModules import *

nout = MultiplexStream()
Notify.ptr().setOstreamPtr(nout, 0)
nout.addFile(Filename(logfile))
nout.addStandardOutput()
nout.addSystemDebug()

print("\n\nStarting %s (number: %s) on %s port %s. %s %s" % (
    districtName, districtNumber, mdip, mdport,
    time.asctime(time.localtime(time.time())), time.tzname[0]))

print("Initializing...")

from otp.ai.AIBaseGlobal import *
from toontown.ai import ToontownAIRepository
from direct.showbase import PythonUtil

simbase.air = ToontownAIRepository.ToontownAIRepository(
    mdip, mdport,
    esip, esport,
    dcFileNames,
    districtNumber,
    districtName,
    districtType,
    ssId,
    minObjId,
    maxObjId)

simbase.aiService = 1

try:
    run()
except:
    info = PythonUtil.describeException()
    simbase.air.writeServerEvent('ai-exception', districtNumber, info)
    raise
