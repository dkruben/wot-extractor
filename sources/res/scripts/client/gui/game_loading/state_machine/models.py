# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/state_machine/models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/models.py
from gui.game_loading.resources.consts import Milestones
from gui.game_loading.resources.models import StatusTextModel
from gui.game_loading.state_machine.const import ContentState

class ImageViewSettingsModel(object):
    __slots__ = ('showVfx', 'contentState', 'ageRatingPath', 'info', 'showSmallLogo',
                 'minimalDuration')

    def __init__(self, showVfx=True, contentState=ContentState.INVISIBLE, ageRatingPath='', info='', showSmallLogo=True, minimalDuration=0.0):
        self.showVfx = showVfx
        self.contentState = contentState
        self.ageRatingPath = ageRatingPath
        self.info = info
        self.showSmallLogo = showSmallLogo
        self.minimalDuration = minimalDuration

    def __repr__(self):
        return ('<ImageViewSettingsModel(vfx={}, contentState={}, ageRatingPath={}, info={}, showSmallLogo={}, minimalDuration={})>').format(self.showVfx, self.contentState, self.ageRatingPath, self.info, self.showSmallLogo, self.minimalDuration)


class ProgressSettingsModel(object):
    __slots__ = ('startPercent', 'limitPercent', 'ticksInProgress', 'minTickTimeSec')

    def __init__(self, startPercent, limitPercent, ticksInProgress, minTickTimeSec):
        self.startPercent = startPercent
        self.limitPercent = limitPercent
        self.ticksInProgress = ticksInProgress
        self.minTickTimeSec = minTickTimeSec

    def __repr__(self):
        return ('<ProgressBarSettingsModel(start={}, limit={}, ticks={}, minTickTimeSec={})>').format(self.startPercent, self.limitPercent, self.ticksInProgress, self.minTickTimeSec)


class LoadingMilestoneModel(object):
    __slots__ = ('name', 'percent', 'forceApply', 'status')

    def __init__(self, name, percent, forceApply, status):
        self.name = name
        self.percent = percent
        self.forceApply = forceApply
        self.status = status

    def __repr__(self):
        return ('<LoadingMilestoneModel(name={}, percent={}, forceApply={}, status={}>').format(self.name, self.percent, self.forceApply, self.status)
