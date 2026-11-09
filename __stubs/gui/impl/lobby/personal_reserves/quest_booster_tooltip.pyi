# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/quest_booster_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.goodies.goodie_items import Booster as Booster, getFullNameForBoosterIcon as getFullNameForBoosterIcon
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import fillBoosterModelWithData as fillBoosterModelWithData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel as BoosterModel
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getBoostersInGroup as getBoostersInGroup
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from helpers.time_utils import ONE_DAY as ONE_DAY
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache

class QuestBoosterTooltip(ViewImpl):
    __slots__: tuple
    goodiesCache: Any
    boosterID: Any
    def __init__(self, boosterID):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
