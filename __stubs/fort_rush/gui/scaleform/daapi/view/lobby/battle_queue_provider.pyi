# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/lobby/battle_queue_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform import MENU as MENU
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import QueueProvider as QueueProvider, TYPES_ORDERED as TYPES_ORDERED, needShowLongWaitingWarning as needShowLongWaitingWarning
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.Vehicle import getTypeBigIconPath as getTypeBigIconPath
from gui.shared.formatters import text_styles as text_styles
from helpers.i18n import makeString as makeString
_HTMLTEMP_PLAYERSLABEL = 'html_templates:lobby/queue/playersLabel'
_FOUR_ROWS_BATTLE_QUEUE_LAYOUT = 'fourRowsBattleQueue'
_FORT_RUSH_BATTLE_ICON: Any
_FORT_RUSH_BATTLE_QUEUE_TITLE: Any
_FORT_RUSH_EXCLUDED_BATTLE_QUEUE_CLASS: Any

class FortRushQueueProvider(QueueProvider):
    _needAdditionalInfo: Any
    def __init__(self, proxy, qType=...):
        ...
    def processQueueInfo(self, qInfo):
        ...
    def needAdditionalInfo(self):
        ...
    def getLayoutStr(self):
        ...
    def getIconPath(self, iconLabel):
        ...
    def getTitle(self, guiType):
        ...
    def additionalInfo(self):
        ...
    @staticmethod
    def _isStartButtonDisplayed(vClasses):
        ...
    def _createCommonPlayerString(self, playerCount):
        ...
