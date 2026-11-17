# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/comp7_voip_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import typing as typing
import VOIP as VOIP
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from comp7_core.gui.battle_control.interfaces import IComp7VOIPController as IComp7VOIPController
_HTML_TEMPLATE = 'html_templates:comp7/voiceChat'

# decorador original: @enum.unique
class VoiceChatControlTextStyles(enum.Enum):
    FULL_STATS = 'fullStatsStyle'
    PLAYERS_PANEL = 'playersPanelStyle'

class Comp7VoipHelper(object):
    __slots__: tuple
    __sessionProvider: Any
    __component: Any
    __textStyle: Any
    __enabled: Any
    def __init__(self, component, textStyle):
        ...
    @property
    def _voipController(self):
        ...
    @property
    def __isVisible(self):
        ...
    @property
    def __isJoined(self):
        ...
    def populate(self):
        ...
    def dispose(self):
        ...
    def enable(self, enable):
        ...
    def onVoiceChatControlClick(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __update(self, *_, **__):
        ...
    def __makeHtmlString(self, text):
        ...
