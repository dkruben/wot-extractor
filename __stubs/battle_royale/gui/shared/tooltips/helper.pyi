# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/shared/tooltips/helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import lmap as lmap
from functools import partial as partial
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.reward_points_place_model import RewardPointsPlaceModel as RewardPointsPlaceModel
from frameworks.wulf import Array as Array
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray, fillStringsArray as fillStringsArray
from gui.impl import backport as backport
from gui.impl.gen import R as R
_string = R.strings.battle_royale.tooltip.progression.leaderboardReward

def fillProgressionPointsTableModel(viewModel, progressionPointsList, headerResource=...):
    ...
def _getGameModeName(headerResource, gameMode):
    ...
def _setRangeLabel(points, prevLevel, headerResource):
    ...
def _getRowPointsCell(points, prevLevel, headerResource):
    ...
