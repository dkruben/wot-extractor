# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/notification/decorators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/notification/decorators.py
from __future__ import absolute_import
from fun_random.gui.feature.fun_constants import FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher, FunSubModesWatcher
from notification.decorators import MessageDecorator
from notification.settings import NOTIFICATION_BUTTON_STATE as _BUTTON_STATE

class FunRandomNewSubModesMessageDecorator(MessageDecorator, FunSubModesWatcher):
    _HIDDEN_STATES = (
     FunSubModesState.UNDEFINED, FunSubModesState.SINGLE_FROZEN, FunSubModesState.AFTER_SEASON)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(FunRandomNewSubModesMessageDecorator, self).__init__(entityID, entity, settings, model)
        self.startSubSettingsListening(self.__updateSubModes)
        self.startSubStatusListening(self.__updateSubModes)

    def clear(self):
        self.stopSubStatusListening(self.__updateSubModes)
        self.stopSubSettingsListening(self.__updateSubModes)
        super(FunRandomNewSubModesMessageDecorator, self).clear()

    def _make(self, entity=None, settings=None):
        self.__updateButtons()
        super(FunRandomNewSubModesMessageDecorator, self)._make(entity, settings)

    def __updateButtons(self):
        if self._entity and self._entity.get('buttonsLayout'):
            subModesState = self._funRandomCtrl.subModesInfo.getSubModesStatus().state
            state = _BUTTON_STATE.HIDDEN if subModesState in self._HIDDEN_STATES else _BUTTON_STATE.DEFAULT
            self._entity.setdefault('buttonsStates', {}).update({'submit': state})

    def __updateSubModes(self, *_):
        self.__updateButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


class FunRandomProgressionStageMessageDecorator(MessageDecorator, FunProgressionWatcher):

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(FunRandomProgressionStageMessageDecorator, self).__init__(entityID, entity, settings, model)
        self.startProgressionListening(self.__updateProgression)

    def clear(self):
        self.startProgressionListening(self.__updateProgression)
        super(FunRandomProgressionStageMessageDecorator, self).clear()

    def _make(self, entity=None, settings=None):
        self.__updateButtons()
        super(FunRandomProgressionStageMessageDecorator, self)._make(entity, settings)

    def __updateButtons(self):
        if self._entity and self._entity.get('buttonsLayout'):
            state = _BUTTON_STATE.DEFAULT if self.getActiveProgression() else _BUTTON_STATE.HIDDEN
            self._entity.setdefault('buttonsStates', {}).update({'submit': state})

    def __updateProgression(self, *_):
        self.__updateButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return
