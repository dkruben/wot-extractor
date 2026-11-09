# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/hint_panel/hint_panel_plugin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from datetime import datetime as datetime
from helpers import time_utils as time_utils
from account_helpers.AccountSettings import HINTS_LEFT as HINTS_LEFT, NUM_BATTLES as NUM_BATTLES, LAST_DISPLAY_DAY as LAST_DISPLAY_DAY
from gui.shared.utils.plugins import IPlugin as IPlugin
_HINT_DISPLAY_COUNT_AFTER_RESET = 1
HintData: Any

class HintPriority(object):
    DYN_SQUAD = 1
    TRAJECTORY = 2
    HELP = 3
    MAPBOX = 4
    DEV_MAPS = 4
    BATTLE_COMMUNICATION = 5
    QUESTS = 6
    RESERVES = 7
    RADAR = 8
    SIEGE = 9
    PILLBOX = 10

class HelpHintContext(object):
    MECHANICS = 'mechanics'
    ROLE_HELP = 'roleHelp'
    MAPS_TRAINING = 'mapsTraining'
    MAPBOX = 'mapbox'
    DEV_MAPS = 'devMaps'
    BATTLE_ROYALE = 'battleRoyale'
    COMMANDER_CAMERA = 'commanderCamera'

class HintPanelPlugin(IPlugin):
    __slots__: tuple
    @classmethod
    def isSuitable(cls):
        ...
    def setPeriod(self, period):
        ...
    def updateMapping(self):
        ...
    def _getHint(self):
        ...
    @staticmethod
    def _shouldDelayHideTimeout(activeHint, btnID):
        ...
    @staticmethod
    def _updateCounterOnUsed(settings):
        ...
    @staticmethod
    def _updateBattleCounterOnUsed(settings):
        ...
    @staticmethod
    def _updateCounterOnStart(setting, dayCoolDown, battleCoolDown):
        ...
    @classmethod
    def _updateCounterOnBattle(cls, setting):
        ...
    @staticmethod
    def _haveHintsLeft(setting):
        ...
