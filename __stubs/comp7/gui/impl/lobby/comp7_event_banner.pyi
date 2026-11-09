# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from account_helpers.AccountSettings import COMP7_BANNER_FIRST_APPEARANCE_TIMESTAMP as COMP7_BANNER_FIRST_APPEARANCE_TIMESTAMP
from comp7_core.gui.impl.lobby.event_banner import Comp7CoreEventBanner as Comp7CoreEventBanner
from comp7.gui.impl.lobby.tooltips.entry_point_tooltip import Comp7EntryPointTooltip as Comp7EntryPointTooltip
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as Comp7SeasonState
from comp7.gui.comp7_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES, COMP7_ENTRY_POINT_ALIAS as COMP7_ENTRY_POINT_ALIAS
from comp7.gui.prb_control.entities.comp7_prb_helpers import selectComp7 as selectComp7
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7EventBanner(Comp7CoreEventBanner):
    NAME = COMP7_ENTRY_POINT_ALIAS
    __comp7Controller: Any
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
    def borderColor(self):
        ...
    @staticmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def isEntryPointAvailable(modeCtrl=None):
        ...
    def createToolTipContent(self, event):
        ...
