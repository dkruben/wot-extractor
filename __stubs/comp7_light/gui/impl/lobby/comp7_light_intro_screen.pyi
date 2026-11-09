# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_intro_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.impl.lobby.intro_screen import IntroScreen as IntroScreen
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_LIGHT_TOOLTIPS
from comp7_light.gui.impl.gen.view_models.views.lobby.intro_screen_model import IntroScreenModel as IntroScreenModel
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7_light.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_gui_helper import updateComp7LightLastSeason as updateComp7LightLastSeason
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightIntroScreen(IntroScreen):
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
    def _seasonNameClazz(self):
        ...
    @property
    def _calendarDayTooltipID(self):
        ...
    def _onLoaded(self):
        ...
