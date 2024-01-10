import __builtin__

class game:
    name = 'toontown'
    process = 'server'
    
__builtin__.game = game

from pandac.PandaModules import *

loadPrcFile('etc/Configrc.exe.prc')

from otp.ai.AIBaseGlobal import *
from toontown.ai.ToontownAIRepository import ToontownAIRepository

aiConfig = ''
aiConfig += 'air-base-channel %s\n' % 101000000
aiConfig += 'air-channel-allocation %s\n' % 999999
aiConfig += 'air-stateserver %s\n' % 4002
aiConfig += 'district-name %s\n' % 'Toon Valley'
aiConfig += 'air-connect %s\n' % '127.0.0.1:7199'
aiConfig += 'eventlog-host %s\n' % '127.0.0.1:7197'
loadPrcFileData('AI Config', aiConfig)

simbase.air = ToontownAIRepository(config.GetInt('air-base-channel', 1000000), config.GetInt('air-stateserver', 4002), config.GetString('district-name', 'Toon Valley'))

host = config.GetString('air-connect', '127.0.0.1:7199')
port = 7199
if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)

simbase.air.connect (host, port)

try:    
    run()
except SystemExit:
    raise
except Exception:
    from direct.showbase import PythonUtil
    print PythonUtil.describeException()
    raise
