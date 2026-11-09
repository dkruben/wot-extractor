# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/platoon/settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/settings_model.py
import typing
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.tiers_settings_model import TiersSettingsModel
from gui.impl.gen.view_models.views.lobby.platoon.voice_chat_settings_model import VoiceChatSettingsModel
F = typing.TypeVar('F')

class SearchFilterTypes(Enum):
    VOICE = 'voice'
    TIER = 'tier'


class SettingsModel(ViewModel, typing.Generic[F]):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SettingsModel, self).__init__(properties=properties, commands=commands)

    @property
    def tiersSettings(self):
        return self._getViewModel(0)

    @staticmethod
    def getTiersSettingsType():
        return TiersSettingsModel

    @property
    def voiceSettings(self):
        return self._getViewModel(1)

    @staticmethod
    def getVoiceSettingsType():
        return VoiceChatSettingsModel

    def getSearchFilterTypes(self):
        return self._getArray(2)

    def setSearchFilterTypes(self, value):
        self._setArray(2, value)

    @staticmethod
    def getSearchFilterTypesType():
        return F

    def _initialize(self):
        super(SettingsModel, self)._initialize()
        self._addViewModelProperty('tiersSettings', TiersSettingsModel())
        self._addViewModelProperty('voiceSettings', VoiceChatSettingsModel())
        self._addArrayProperty('searchFilterTypes', Array())
