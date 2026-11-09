# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/quick_training/events.py
from gui.impl.lobby.container_views.base.events import ComponentEventsBase

class QuickTrainingViewEvents(ComponentEventsBase):

    def __init__(self):
        super(QuickTrainingViewEvents, self).__init__()
        self.onFreeXpMouseEnter = self._createEvent()
        self.onFreeXpSelected = self._createEvent()
        self.onFreeXpUpdated = self._createEvent()
        self.onFreeXpManualInput = self._createEvent()
        self.onBookMouseEnter = self._createEvent()
        self.onBookSelected = self._createEvent()
        self.onBuyBook = self._createEvent()
        self.onPostProgressionOpen = self._createEvent()
        self.onLearn = self._createEvent()
        self.onCancel = self._createEvent()
        self.onMentoringClick = self._createEvent()
