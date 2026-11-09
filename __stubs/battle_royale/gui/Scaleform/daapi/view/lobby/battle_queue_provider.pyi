# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/battle_queue_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from battle_royale.gui.constants import BattleRoyaleSubMode as BattleRoyaleSubMode
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider as RandomQueueProvider
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle_royale.battle_results.player_battle_type_status_model import BattleType as BattleType
from gui.prb_control import prb_getters as prb_getters
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
_SUBMODE_ID_TO_BATTLE_TYPE: dict

class BattleRoyaleQueueProvider(RandomQueueProvider):
    __battleRoyaleController: Any
    def processQueueInfo(self, qInfo):
        ...
    def getLayoutStr(self):
        ...
    def getIconPath(self, iconlabel):
        ...
    def getAdditionalParams(self):
        ...
