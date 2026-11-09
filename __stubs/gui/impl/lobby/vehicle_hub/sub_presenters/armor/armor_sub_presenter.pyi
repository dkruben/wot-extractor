# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/armor_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
import BigWorld as BigWorld
import GUI as GUI
import Math as Math
import math_utils as math_utils
import armor_inspector as armor_inspector
from AvatarInputHandler import cameras as cameras
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from account_helpers.settings_core import settings_constants as settings_constants
from constants import VehicleArmorTags as VehicleArmorTags
from frameworks.wulf import ViewStatus as ViewStatus
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui import g_mouseEventHandlers as g_mouseEventHandlers
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.app_loader import app_getter as app_getter
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_model import Modes as Modes
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_vehicle_module import ArmorVehicleModule as ArmorVehicleModule
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_shell_model import ArmorShellModel as ArmorShellModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.select_vehicle.select_vehicle import SelectVehicleWindow as SelectVehicleWindow, SelectVehicleTitles as SelectVehicleTitles
from gui.impl.lobby.tank_setup.tank_setup_helper import createShellMechanicsModels as createShellMechanicsModels
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.armor_tooltip import ArmorTooltipWindow as ArmorTooltipWindow
from cgf_components.armor_inspector_component import ArmorInspectorComponent as ArmorInspectorComponent
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.minor_tooltip import MinorTooltip as MinorTooltip
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.minor_short_tooltip import MinorShortTooltip as MinorShortTooltip
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.utils import fillArmorData as fillArmorData, getCursorPositionInPixels as getCursorPositionInPixels, getMaxArmor as getMaxArmor, getModuleForTurretRotation as getModuleForTurretRotation, getArmorInspectorSetting as getArmorInspectorSetting, setArmorInspectorSetting as setArmorInspectorSetting, ArmorInspectorSettingsKeys as ArmorInspectorSettingsKeys, AttackerVehicleConfiguration as AttackerVehicleConfiguration, getArmorInspectorAttackerVehicleConfig as getArmorInspectorAttackerVehicleConfig, getDefaultAttackerVehicleConfigByCD as getDefaultAttackerVehicleConfigByCD, setArmorInspectorAttackerVehicleConfig as setArmorInspectorAttackerVehicleConfig, MINOR_SHORT_TOOLTIP_DATA as MINOR_SHORT_TOOLTIP_DATA, getCollisionsAtCursor as getCollisionsAtCursor
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.penetration_utils import setShellParamsFromVehicle as setShellParamsFromVehicle
from gui.impl.lobby.vehicle_hub.sub_presenters.sub_presenter_base import SubPresenterBase as SubPresenterBase
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.vehicle_modules import ModulesIconNames as ModulesIconNames
from gui.shared.sort_key import SortKey as SortKey
from gun_rotation_shared import calcPitchLimitsFromDesc as calcPitchLimitsFromDesc
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from uilogging.vehicle_hub.loggers import ArmorTabLogger as ArmorTabLogger
import CGF as CGF
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle as ClientSelectableCameraVehicle
from gui.Scaleform.framework.application import AppEntry as AppEntry
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_model import ArmorModel as ArmorModel
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.penetration_utils import ShellParams as ShellParams
_ROTATION_PER_PX = 0.0015
_SUPPORTED_MECHANICS: Any
_logger: Any
_MODE_CLASSES: dict

class _ModeBase(object):
    __slots__: tuple
    isEntered: Any
    _p: Any
    needsFadeDelay: Any
    def __init__(self, presenter):
        ...
    def enter(self):
        ...
    def exit(self):
        ...

class _ArmorMode(_ModeBase):
    def enter(self):
        ...
    def exit(self):
        ...
    def _isShowProbability(self):
        ...

class _NominalMode(_ArmorMode):
    def enter(self):
        ...
    def _isShowProbability(self):
        ...

class _PenetrationMode(_ArmorMode):
    def enter(self):
        ...
    def _isShowProbability(self):
        ...

class _NoArmorMode(_ModeBase):
    needsFadeDelay: Any
    def __init__(self, presenter):
        ...
    def enter(self):
        ...

class ArmorSubPresenter(SubPresenterBase):
    __slots__: tuple
    _appLoader: Any
    _settingsCore: Any
    _hangarSpace: Any
    _isMouseOver: Any
    _tooltip: Any
    _level: Any
    _normalArmorMax: Any
    _spacedArmorMax: Any
    _uiLogger: Any
    _modes: Any
    _currentModeId: Any
    _currentMode: Any
    _modulesMover: Any
    _modulesSetup: Any
    _attackerSetup: Any
    _shellParams: Any
    vehicleEntity: Any
    isClosing: Any
    def __init__(self, model, parentView):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def vehicleLevel(self):
        ...
    def storeShellParams(self, shellParams):
        ...
    # decorador original: @app_getter
    def app(self):
        ...
    def initialize(self, vhCtx, *args, **kwargs):
        ...
    def finalize(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _fillArmorData(self):
        ...
    def _onAppearanceLoadingFinished(self):
        ...
    def _onAppearanceLoadingStarted(self):
        ...
    def _unsubscribeAppearanceLoadEvents(self):
        ...
    def _initialize(self):
        ...
    def _onComponentInstalled(self, *_):
        ...
    def _onVehicleLoadStarted(self):
        ...
    def _onVehicleLoadFinished(self):
        ...
    def _startUILogger(self):
        ...
    def _handleMouseEvent(self, _):
        ...
    def _onMouseEnter(self, entity):
        ...
    def _onMouseExit(self, entity):
        ...
    def _createTooltip(self):
        ...
    def _updateTooltip(self):
        ...
    def _applyScaleToPosition(self, position):
        ...
    def __onTooltipStatusChanged(self, status):
        ...
    def _destroyTooltip(self):
        ...
    def _onVehicleChanged(self):
        ...
    def _onSettingsChanged(self, diff):
        ...
    def _onModeChanged(self, event):
        ...
    def _setupModes(self):
        ...

class _ModulesMover(object):
    __slots__: tuple
    _vehicleEntity: Any
    _hoveredModule: Any
    _hoveredDistance: Any
    _dragModule: Any
    _gunMultiplier: Any
    _turretMultiplier: Any
    def __init__(self, vehicleEntity, viewModel):
        ...
    def finalize(self, viewModel):
        ...
    def resetModulesRotation(self):
        ...
    def onHover3DScene(self, viewModel):
        ...
    def _onDragStateChanged(self, args):
        ...
    def _updateInversion(self):
        ...
    def _onDragModule(self, args):
        ...

class _ModulesSetup(object):
    __slots__: tuple
    _itemsCache: Any
    _hangarSpace: Any
    _vehicleEntity: Any
    _initialVehicleCD: Any
    _initialTurretCD: Any
    _initialGunCD: Any
    _initialOutfit: Any
    def __init__(self, vehicleEntity, viewModel):
        ...
    def finalize(self, viewModel):
        ...
    def tryRestoreOutfit(self):
        ...
    def updateSelectedModules(self, viewModel):
        ...
    def _initModulesData(self, viewModel):
        ...
    def _updateConfigurationTitle(self, vehicleModel):
        ...
    def _onTurretItemClick(self, args):
        ...
    def _onGunItemClick(self, args):
        ...
    def _installSupportedTurret(self, gunCompactDescr):
        ...
    def _installTopSupportedGun(self, prevGunCD, turretCompactDescr):
        ...

class _AttackerSetup(object):
    __slots__: tuple
    _itemsCache: Any
    _hangarSpace: Any
    _attackerVehicle: Any
    _parent: Any
    def __init__(self, attackerConfig, parent):
        ...
    @property
    def vehicle(self):
        ...
    def finalize(self, viewModel):
        ...
    def _update(self, attackerModel, attackerConfig):
        ...
    def _updateAttackerGun(self, compactDescr, attackerModel, activeGunShotIndex=0):
        ...
    def _updateAttackerShell(self, index, attackerModel):
        ...
    def _onAttackerGunItemClick(self, args):
        ...
    def _onAttackerShellItemClick(self, args):
        ...
    def _onAttackerClicked(self):
        ...
    def _onSelectAttacker(self, vehicleCD):
        ...
    def __updateShellMechanics(self, shellDetailsModel, gun):
        ...

class _ModulesSortKey(SortKey):
    __slots__: tuple
    vehType: Any
    item: Any
    def __init__(self, vehType, item):
        ...
    def _cmp(self, other):
        ...

def _getSortedGuns(vehType):
    ...
