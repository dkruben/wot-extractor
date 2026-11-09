# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_setup/base_hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from BWUtil import AsyncReturn as AsyncReturn
import adisp as adisp
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from Event import Event as Event
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_setup_view_model import AmmunitionSetupViewModel as AmmunitionSetupViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.warning_tooltip_view_model import WarningDescription as WarningDescription
from gui.impl.lobby.tank_setup.ammunition_setup.base import BaseAmmunitionSetupView as BaseAmmunitionSetupView
from gui.impl.lobby.tank_setup.backports.context_menu import getContextMenuData as getContextMenuData
from gui.impl.lobby.tank_setup.backports.tooltips import getSlotTooltipData as getSlotTooltipData, getShellsPriceDiscountTooltipData as getShellsPriceDiscountTooltipData, getSlotSpecTooltipData as getSlotSpecTooltipData
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem
from gui.impl.lobby.tank_setup.tank_setup_sounds import playEnterTankSetupView as playEnterTankSetupView, playExitTankSetupView as playExitTankSetupView
from gui.impl.lobby.tank_setup.tooltips.setup_tab_tooltip_view import SetupTabTooltipView as SetupTabTooltipView
from gui.impl.lobby.tank_setup.tooltips.warning_tooltip_view import WarningTooltipView as WarningTooltipView
from gui.impl.lobby.tanksetup.tooltips.popular_loadouts_tooltip import PopularLoadoutsTooltip as PopularLoadoutsTooltip
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.close_confiramtor_helper import CloseConfirmatorsHelper as CloseConfirmatorsHelper
from gui.shared.events import AmmunitionSetupViewEvent as AmmunitionSetupViewEvent, PrbActionEvent as PrbActionEvent
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from post_progression_common import TANK_SETUP_GROUPS as TANK_SETUP_GROUPS, TankSetupGroupsId as TankSetupGroupsId
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from soft_exception import SoftException as SoftException
from wg_async import wg_async as wg_async, wg_await as wg_await

class TankSetupCloseConfirmatorsHelper(CloseConfirmatorsHelper):
    def getRestrictedSfViews(self):
        ...
    def getRestrictedEvents(self):
        ...

class BaseHangarAmmunitionSetupView(BaseAmmunitionSetupView):
    _lobbyContext: Any
    _VIEW_FLAG = ViewFlags.VIEW
    _VIEW_MODEL = AmmunitionSetupViewModel
    __slots__: tuple
    __blur: Any
    _isClosed: Any
    __closeConfirmatorHelper: Any
    __moneyCache: Any
    _previousSectionName: Any
    onClose: Any
    onAnimationEnd: Any
    def __init__(self, layoutID=..., **kwargs):
        ...
    def _createBlur(self):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def sendSlotAction(self, args):
        ...
    def setLastSlotAction(self, *args, **kwargs):
        ...
    def getVehicleItem(self):
        ...
    def getSelectedSetup(self):
        ...
    def _getBackportTooltipData(self, event):
        ...
    def _getBackportContextMenuData(self, event):
        ...
    def _createVehicleItem(self):
        ...
    def _recreateVehicleItem(self):
        ...
    def _recreateVehicleSetups(self):
        ...
    def _getEquipmentsPairs(self, groupID):
        ...
    def _createMainTankSetup(self):
        ...
    def _createAmmunitionPanel(self):
        ...
    def _onLoading(self, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    # decorador original: @wg_async
    def _onClose(self):
        ...
    # decorador original: @adisp.adisp_process
    def __onSpecializationSelect(self, args=None):
        ...
    def _updateAmmunitionPanel(self, sectionName=None):
        ...
    def __updateTTC(self, sectionName=None):
        ...
    def __createCopyVehicle(self):
        ...
    def __onResized(self, args):
        ...
    def __onCloseView(self, event):
        ...
    def __onViewRendered(self):
        ...
    def __onAnimationEnd(self):
        ...
    def _onAcceptComplete(self):
        ...
    def __onDragDropSwap(self, args):
        ...
    def _onSyncCompleted(self, _, diff):
        ...
    def _closeWindow(self):
        ...
    # decorador original: @wg_async
    def _closeConfirmator(self):
        ...
