# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/debug_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.DebugPanelMeta import DebugPanelMeta as DebugPanelMeta
from gui.battle_control.controllers.debug_ctrl import IDebugPanel as IDebugPanel

class DebugPanel(DebugPanelMeta, IDebugPanel):
    _fps: Any
    _ping: Any
    _isLaggingNow: Any
    def __init__(self):
        ...
    def updateDebugInfo(self, ping, fps, isLaggingNow, fpsReplay):
        ...
