# File: T (Python 2.4)

from direct.interval.MetaInterval import Sequence
from direct.interval.FunctionInterval import Wait, Func
PULSE_GUI_DURATION = 0.20000000000000001
PULSE_GUI_CHANGE = 0.33300000000000002

def cleanup(name):
    taskMgr.remove(name)


def start(ival):
    cleanup(ival.getName())
    ival.start()


def loop(ival):
    cleanup(ival.getName())
    ival.loop()


def getPulseLargerIval(np, name, duration = PULSE_GUI_DURATION, scale = 1):
    return getPulseIval(np, name, 1 + PULSE_GUI_CHANGE, duration = duration, scale = scale)


def getPulseSmallerIval(np, name, duration = PULSE_GUI_DURATION, scale = 1):
    return getPulseIval(np, name, 1 - PULSE_GUI_CHANGE, duration = duration, scale = scale)


def getPulseIval(np, name, change, duration = PULSE_GUI_CHANGE, scale = 1):
    return Sequence(np.scaleInterval(duration, scale * change, blendType = 'easeOut'), np.scaleInterval(duration, scale, blendType = 'easeIn'), name = name, autoFinish = 1)


def getPresentGuiIval(np, name, waitDuration = 0.5, moveDuration = 1.0, parent = aspect2d):
    endPos = np.getPos()
    np.setPos(parent, 0, 0, 0)
    return Sequence(Func(np.show), getPulseLargerIval(np, '', scale = np.getScale()), Wait(waitDuration), np.posInterval(moveDuration, endPos, blendType = 'easeInOut'), name = name, autoFinish = 1)

