# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/prebattle_highlights/presenters/prebattle_highlights_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.battle.prebattle_highlights.presenters.statistics_sub_presenter import StatisticsSubPresenter as StatisticsSubPresenter
from gui.impl.battle.prebattle_highlights.presenters.vehicle_markers_sub_presenter import VehicleMarkersSubPresenter as VehicleMarkersSubPresenter
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class PrebattleHighlightsPresenter(SubModelPresenter):
    __sessionProvider: Any
    _subPresenters: Any
    _pbhCtrl: Any
    def __init__(self, viewModel, parentView, pbhCtrl):
        ...
    def addSubPresenter(self, subPresenter):
        ...
    def packModel(self):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onStartPbhStage(self):
        ...
