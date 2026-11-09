# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/comp7_prime_time_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.comp7_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from comp7_core.gui.Scaleform.daapi.view.lobby.comp7_core_prime_time_view import Comp7CorePrimeTimeView as Comp7CorePrimeTimeView
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7PrimeTimeView(Comp7CorePrimeTimeView):
    _RES_STATUS_ROOT = R.strings.comp7_ext.primeTimeView.status
    __comp7Ctrl: Any
    def _getController(self):
        ...
    def _getPrbActionName(self):
        ...
    def _getPrbForcedActionName(self):
        ...
    @property
    def _seasonNameClazz(self):
        ...
