# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from gui.impl import backport as backport
from gui.impl.gen import R as R
from account_helpers.AccountSettings import COMP7_LIGHT_BANNER_FIRST_APPEARANCE_TIMESTAMP as COMP7_LIGHT_BANNER_FIRST_APPEARANCE_TIMESTAMP
from comp7_core.gui.impl.lobby.event_banner import Comp7CoreEventBanner as Comp7CoreEventBanner
from comp7_light.gui.comp7_light_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES, COMP7_LIGHT_ENTRY_POINT_ALIAS as COMP7_LIGHT_ENTRY_POINT_ALIAS
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as Comp7LightSeasonState
from comp7_light.gui.impl.lobby.tooltips.entry_point_tooltip import Comp7LightEntryPointTooltip as Comp7LightEntryPointTooltip
from comp7_light.gui.prb_control.entities.comp7_light_prb_helpers import selectComp7Light as selectComp7Light
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightEventBanner(Comp7CoreEventBanner):
    NAME = COMP7_LIGHT_ENTRY_POINT_ALIAS
    __comp7LightController: Any
    @property
    def _modeController(self):
        ...
    @property
    def _seasonStateClazz(self):
        ...
    @property
    def _accountSettingsTimestampFlag(self):
        ...
    @property
    def _selectorBattleType(self):
        ...
    @staticmethod
    def _selectMode():
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    @property
    def borderColor(self):
        ...
    @staticmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def isEntryPointAvailable(modeCtrl=None):
        ...
    def createToolTipContent(self, event):
        ...
