# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/consumables_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from battle_modifiers_common import BattleParams as BattleParams
from constants import DAMAGE_INTERPOLATION_DIST_FIRST as DAMAGE_INTERPOLATION_DIST_FIRST, DAMAGE_INTERPOLATION_DIST_LAST as DAMAGE_INTERPOLATION_DIST_LAST
from constants import SHELL_TYPES as SHELL_TYPES
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.battle_control.components_states.ammo.constants import ShellMode as ShellMode
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.shared.formatters import text_styles as text_styles
from gui.shared.items_parameters.functions import getBustleFeedModifiedShells as getBustleFeedModifiedShells, getShellCalibrationShells as getShellCalibrationShells, getShellParamsSwitcherModifiedShells as getShellParamsSwitcherModifiedShells
from gui.shared.items_parameters import getShellDescriptors as getShellDescriptors, NO_DATA as NO_DATA
from gui.shared.items_parameters.shell_params import ShellParams as ShellParams
from gui.shared.items_parameters.formatters import CRITICAL_HIT_CHANCE_TYPE_DYN_PATH as CRITICAL_HIT_CHANCE_TYPE_DYN_PATH
from gui.shared.utils.functions import stripColorTagDescrTags as stripColorTagDescrTags
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.artefacts import Equipment as Equipment, Artefact as Artefact
from items.utils import getVehicleShotSpeedByFactors as getVehicleShotSpeedByFactors, getVehicleDescriptorWithoutMechanic as getVehicleDescriptorWithoutMechanic
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from math_common import round_py2_style_int as round_py2_style_int
from post_progression_common import TankSetupLayouts as TankSetupLayouts, TankSetupGroupsId as TankSetupGroupsId
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
from typing import Tuple as Tuple, Optional as Optional, Type as Type
from items.vehicle_items import Shell as Shell
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from gui.battle_control.controllers.consumables.ammo_ctrl import _GunSettings as _GunSettings
from gui.battle_control.arena_info.interfaces import IPrebattleSetupsController as IPrebattleSetupsController
from battle_modifiers_common import BattleModifiers as BattleModifiers
ASTERISK = '*'
TOOLTIP_FORMAT = '{{HEADER}}{0:>s}{{/HEADER}}\n/{{BODY}}{1:>s}{{/BODY}}'
TOOLTIP_NO_BODY_FORMAT = '{{HEADER}}{0:>s}{{/HEADER}}'
BULLET: Any
LIST_PREFIX: Any
DASH: Any
GROUP_AND_LAYOUT: dict
_PARAM_BUILDERS: dict
_PARAM_BUILDERS_BY_MECHANIC: dict

class IShellParamsBuilder(object):
    def build(self, shellDescr, vDescr, gunSettings):
        ...

class _StandardShellParamsBuilder(IShellParamsBuilder):
    _sessionProvider: Any
    _lobbyContext: Any
    def build(self, shellDescr, vDescr, gunSettings):
        ...
    def _appendDamage(self, params, shellDescr, vDescr, shellParams, footnotes):
        ...
    def _appendDamagePerSec(self, params, shellDescr, vDescr):
        ...
    def _appendPiercingPower(self, params, shellDescr, gunSettings, shellParams, footnotes):
        ...
    def _appendShotSpeed(self, params, shellDescr, gunSettings):
        ...
    def _appendExplosionRadius(self, params, shellDescr):
        ...
    def _appendStunDuration(self, params, shellDescr):
        ...

class _ComplexMechanicParamsBuilder(IShellParamsBuilder):
    _sessionProvider: Any
    _mechanic = None
    def build(self, shellDescr, vDescr, gunSettings):
        ...
    def _getLabel(self):
        ...
    def _getDescriptors(self, vDescr):
        ...
    def _getBaseParams(self, shellDescr, basicVDescr, specVDescr, footnotes):
        ...
    def _getExtendedParams(self, shellDescr, basicVDescr, specVDescr):
        ...

class _LowChargeShotParamsBuilder(_ComplexMechanicParamsBuilder):
    _mechanic = VehicleMechanicKeys.LOW_CHARGE_SHOT
    def _getDescriptors(self, vDescr):
        ...

class _ShellCalibrationParamsBuilder(_ComplexMechanicParamsBuilder):
    _mechanic = VehicleMechanicKeys.SHELL_CALIBRATION
    def _getDescriptors(self, vDescr):
        ...

class _ShellParamsSwitcherParamsBuilder(_ComplexMechanicParamsBuilder):
    _mechanic = VehicleMechanicKeys.SHELL_PARAMS_SWITCHER
    def _getDescriptors(self, vDescr):
        ...
    def _getExtendedParams(self, shellDescr, basicVDescr, specVDescr):
        ...

class _BustleFeedParamsBuilder(_ComplexMechanicParamsBuilder):
    _mechanic = VehicleMechanicKeys.BUSTLE_FEED
    def _getDescriptors(self, vDescr):
        ...

class _FootnoteCollector(object):
    __notes: Any
    __distanceNoteMarker: Any
    def __init__(self):
        ...
    def addNote(self, text):
        ...
    def addDistanceNote(self, minDist, maxDist):
        ...
    def addNoDistanceNote(self):
        ...
    def collectNotes(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def buildEquipmentSlotTooltipTextBySlotInfo(slotType, slotId, battleSessionProvider=None):
    ...
def _getEquipmentTooltipContent(item, modifiers):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def makeShellTooltip(intCD, sessionProvider=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def applyBoundFactors(value, sessionProvider=None):
    ...
def getShellTooltipsParamBuilder(shellMode):
    ...
def getShellTooltipsParamBuilderByMechanic(mechanic):
    ...
def _getShellMechanic(descriptor, vehicleDescriptor):
    ...
def _formatPairOfValues(value1, value2, formattingFunc=...):
    ...
def _formatPairOfValuesByTemplate(value1, value2, template, formattingFunc=...):
    ...
def _getNormalizationAngleBlock(basicShellParams, specShellParams):
    ...
def _getRicochetAngleBlock(basicShellParams, specShellParams):
    ...
def _getCriticalHitChanceBlock(basicShellParams, specShellParams):
    ...
def _getPenetrationLossBlock(basicShellParams, specShellParams):
    ...
