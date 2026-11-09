# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/battle_pass_service.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from gui.impl.lobby.user_missions.hangar_widget.services import IBattlePassService as IBattlePassService
from gui.impl.lobby.user_missions.hangar_widget.services.service_events import ServiceEvents as ServiceEvents
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class BattlePassService(IBattlePassService, ServiceEvents):
    __battlePassController: Any
    onBattlePassChanged: Any
    def __init__(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def isVisible(self):
        ...
    def startListening(self):
        ...
    def stopListening(self):
        ...
    def finalize(self):
        ...
    def _isValidBattleTypeForBattlePass(self):
        ...
    def _onBattlePassEvent(self, *_):
        ...
