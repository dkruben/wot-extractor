# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_no_vehicles_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.impl.lobby.no_vehicles_screen import NoVehiclesScreen as NoVehiclesScreen
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_LIGHT_TOOLTIPS
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7_light.gui.impl.gen.view_models.views.lobby.no_vehicles_screen_model import ErrorReason as ErrorReason
from comp7_light.gui.impl.gen.view_models.views.lobby.no_vehicles_screen_model import NoVehiclesScreenModel as NoVehiclesScreenModel
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7_light.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightNoVehiclesScreen(NoVehiclesScreen):
    __comp7LightController: Any
    @property
    def _modeController(self):
        ...
    @property
    def _modelClazz(self):
        ...
    @property
    def _seasonStateClazz(self):
        ...
    @property
    def _yearStateClazz(self):
        ...
    @property
    def _errorReasonClazz(self):
        ...
    @property
    def _seasonNameClazz(self):
        ...
    @property
    def _calendarDayTooltipID(self):
        ...
