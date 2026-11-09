# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/players_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.Scaleform.daapi.view.battle.comp7_voip_helper import Comp7VoipHelper as Comp7VoipHelper, VoiceChatControlTextStyles as VoiceChatControlTextStyles
from comp7_core.gui.Scaleform.daapi.view.meta.Comp7PlayersPanelMeta import Comp7PlayersPanelMeta as Comp7PlayersPanelMeta
from constants import ARENA_PERIOD as ARENA_PERIOD

class PlayersPanel(Comp7PlayersPanelMeta):
    __voipHelper: Any
    def __init__(self):
        ...
    def onVoiceChatControlClick(self):
        ...
    def setPeriod(self, period):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    @classmethod
    def __isVoipControlEnabled(cls, period=None):
        ...
