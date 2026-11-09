# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/skills_training/events.py
from gui.impl.lobby.container_views.base.events import ComponentEventsBase

class SkillsTrainingComponentViewEvents(ComponentEventsBase):

    def __init__(self):
        super(SkillsTrainingComponentViewEvents, self).__init__()
        self.onSkillHover = self._createEvent()
        self.onSkillOut = self._createEvent()
        self.onSkillClick = self._createEvent()
        self.onTrain = self._createEvent()
        self.onCancel = self._createEvent()
        self.onClose = self._createEvent()
