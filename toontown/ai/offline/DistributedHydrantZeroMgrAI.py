from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from toontown.ai import DistributedPhaseEventMgrAI

class DistributedHydrantZeroMgrAI(DistributedPhaseEventMgrAI.DistributedPhaseEventMgrAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedHydrantZeroMgrAI')
    def __init__(self, air, startAndEndTimes, phaseDates):
        DistributedPhaseEventMgrAI.DistributedPhaseEventMgrAI.__init__(self, air, startAndEndTimes,phaseDates)
