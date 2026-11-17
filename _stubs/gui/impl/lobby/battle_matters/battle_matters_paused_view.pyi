# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_paused_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_paused_view_model import BattleMattersPausedViewModel as BattleMattersPausedViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.events_dispatcher import showBattleMatters as showBattleMatters
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController

class BattleMattersPausedView(ViewImpl):
    __slots__: tuple
    __battleMattersController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    @staticmethod
    def __gotoHangar():
        ...
    def __onStateChanged(self):
        ...
