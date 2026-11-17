# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Tuple as Tuple
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.Tankman import Tankman as Tankman
_logger: Any

# decorador original: @replace_none_kwargs(...)
def _getVehicleFromTankman(tankman, itemsCache=None):
    ...
# decorador original: @replace_none_kwargs(...)
def tankmanHasCrewAssistOrderSets(tankman, tankmanRole, wotPlusCtrl=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getTankmanCrewAssistOrderSets(tankman, tankmanRole, wotPlusCtrl=None):
    ...
