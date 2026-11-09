# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/scenario_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf.view.view import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_scenario_tooltip_model import MapsTrainingScenarioTooltipModel as MapsTrainingScenarioTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from maps_training_common.maps_training_constants import SCENARIO_INDEXES as SCENARIO_INDEXES

class ScenarioTooltip(ViewImpl):
    _vehicleType: Any
    _team: Any
    _mapId: Any
    _targets: Any
    _vehicleName: Any
    _isComplete: Any
    _rewards: Any
    def __init__(self, vehicleType, team, mapId, targets, vehicleName, isComplete, rewards):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
