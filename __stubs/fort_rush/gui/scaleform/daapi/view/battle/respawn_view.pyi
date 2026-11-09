# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/respawn_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from fort_rush.gui.battle_control.controllers.respawn_ctrl import ISpawnListener as ISpawnListener
from fort_rush.gui.scaleform.daapi.view.meta.FortRushRespawnViewMeta import FortRushRespawnViewMeta as FortRushRespawnViewMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class FortRushRespawnView(FortRushRespawnViewMeta, ISpawnListener):
    _guiSessionProvider: Any
    __delayCallbackID: Any
    def __init__(self):
        ...
    def onRespawnPointClick(self, id):
        ...
    def showSpawnPoints(self):
        ...
    @property
    def _respawnCtrl(self):
        ...
