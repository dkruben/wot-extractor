# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/tankman_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.tooltips.tankman_tooltip_modifier_model import TankmanTooltipModifierModel as TankmanTooltipModifierModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.tankman_tooltip_model import TankmanTooltipModel as TankmanTooltipModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanRestoreInfo as setTankmanRestoreInfo
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.tankman_skill import BROTHERHOOD_SKILL_NAME as BROTHERHOOD_SKILL_NAME, getTankmanSkill as getTankmanSkill
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from items.components.tankmen_components import SPECIAL_CREW_TAG as SPECIAL_CREW_TAG
from items.special_crew import isWitchesCrew as isWitchesCrew
from items.tankmen import getSpecialVoiceTag as getSpecialVoiceTag, tankmenGroupHasRole as tankmenGroupHasRole, getTankmenWithTag as getTankmenWithTag
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
from skeletons.gui.shared import IItemsCache as IItemsCache

class TankmanTooltip(ViewImpl):
    __slots__: tuple
    itemsCache: Any
    _specialSounds: Any
    tankmanID: Any
    isCalledFromCrewWidget: Any
    def __init__(self, tankmanID, isCalledFromCrewWidget=False, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self):
        ...
    def _setVoiceoverReason(self, vm, tankman, vehicle):
        ...
    def _setBonuses(self, vm, tankman, vehicle):
        ...
    @staticmethod
    def __addModifier(modifierViewList, value, icon, title, description=''):
        ...
