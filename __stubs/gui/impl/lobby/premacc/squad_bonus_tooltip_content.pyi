# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/premacc/squad_bonus_tooltip_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.premacc.squad_bonus_tooltip_content_model import SquadBonusTooltipContentModel as SquadBonusTooltipContentModel, SquadBonusTooltipType as SquadBonusTooltipType
from gui.impl.lobby.platoon.platoon_helpers import BonusState as BonusState
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache

class SquadBonusTooltipContent(ViewImpl):
    __slots__: tuple
    __lobbyContext: Any
    __eventsCache: Any
    __hangarGuiCtrl: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, battleType='', bonusState=..., *args, **kwargs):
        ...

def _floatToPercents(value):
    ...
def _getHeaderInfoTooltipType(bonusState):
    ...
