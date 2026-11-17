# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/common/tankman_info_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import BigWorld as BigWorld
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import createAndLoadBackportTooltipWindow as createAndLoadBackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.crew.tooltips.premium_vehicle_tooltip import PremiumVehicleTooltip as PremiumVehicleTooltip
from gui.impl.lobby.crew.tooltips.specialization_wot_plus_tooltip import SpecializationWotPlusTooltip as SpecializationWotPlusTooltip
from gui.impl.lobby.crew.utils import convertMoneyToTuple as convertMoneyToTuple, playRecruitVoiceover as playRecruitVoiceover, VEHICLE_TAGS_FILTER as VEHICLE_TAGS_FILTER
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Any as Any, Callable as Callable, Tuple as Tuple
from gui.impl.gen.view_models.views.lobby.crew.common.tankman_info_model import TankmanInfoModel as TankmanInfoModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_file_view_model import PersonalFileViewModel as PersonalFileViewModel

class TankmanInfoComponent(ComponentBase):
    _itemsCache: _Any
    _appLoader: _Any
    _toolTipMgr: _Any
    __sound: _Any
    def __init__(self, key, parent):
        ...
    def _getViewModel(self, vm):
        ...
    def _getEvents(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _setTankmanInfo(self, vm):
        ...
    def _setVehicleInfo(self, vm):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onRetrain(self):
        ...
    def _onChangeVehicle(self):
        ...
    def _onPlayUniqueVoice(self):
        ...
