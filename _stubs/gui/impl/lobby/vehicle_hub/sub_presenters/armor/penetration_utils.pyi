# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/penetration_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
from builtins import round as round
from collections import namedtuple as namedtuple
import armor_inspector as armor_inspector
import math_utils as math_utils
from account_helpers.settings_core import settings_constants as settings_constants
from constants import SHELL_TYPES as SHELL_TYPES, SHELL_MECHANICS_TYPE as SHELL_MECHANICS_TYPE
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.utils import colorInt2Str as colorInt2Str, applyNormalizationForArmor as applyNormalizationForArmor
from helpers import dependency as dependency
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.config import getConfig as getConfig
from gui.shared.utils.functions import getShellImpactParams as getShellImpactParams
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_model import DCCType as DCCType
from items.components.component_constants import MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS as MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS, MODERN_HE_DAMAGE_ABSORPTION_FACTOR as MODERN_HE_DAMAGE_ABSORPTION_FACTOR
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from helpers.collisions import SegmentCollisionResultExt as SegmentCollisionResultExt
from items.components.gun_components import GunShot as GunShot
ShellParams: Any
PenetrationInfo: Any
_EPS = 1e-05
_HALF_PI: Any
_MM_TO_M = 0.001
_PEN_SIGMA = 0.33
_INV_SQRT2: Any

def setShellParamsFromVehicle(shot, spaceID):
    ...
def calculatePenetrationInfo(shellParams, collisions):
    ...
def _shouldHitRicochet(matInfo, hitAngleCos, params):
    ...
def _buildPenetrationResult(remainingShellPen, penArmor, params):
    ...
def _computePenetrationChance(piercingRatio, randomization):
    ...
