# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/platoon/settings_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.tiers_settings_model import TiersSettingsModel as TiersSettingsModel
from gui.impl.gen.view_models.views.lobby.platoon.voice_chat_settings_model import VoiceChatSettingsModel as VoiceChatSettingsModel
F: Any

class SearchFilterTypes(Enum):
    VOICE = 'voice'
    TIER = 'tier'

# base nao representavel no stub: typing.Generic[...]
class SettingsModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def tiersSettings(self):
        ...
    @staticmethod
    def getTiersSettingsType():
        ...
    @property
    def voiceSettings(self):
        ...
    @staticmethod
    def getVoiceSettingsType():
        ...
    def getSearchFilterTypes(self):
        ...
    def setSearchFilterTypes(self, value):
        ...
    @staticmethod
    def getSearchFilterTypesType():
        ...
    def _initialize(self):
        ...
