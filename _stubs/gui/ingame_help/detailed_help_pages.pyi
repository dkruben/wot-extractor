# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ingame_help/detailed_help_pages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from itertools import chain as chain
import typing as typing
from shared_utils import findFirst as findFirst
import CommandMapping as CommandMapping
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, ROLE_TYPE as ROLE_TYPE, ACTION_TYPE_TO_LABEL as ACTION_TYPE_TO_LABEL, ROLE_TYPE_TO_LABEL as ROLE_TYPE_TO_LABEL
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HelpHintContext as HelpHintContext
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.system_factory import registerIngameHelpPagesBuilders as registerIngameHelpPagesBuilders, collectIngameHelpPagesBuilders as collectIngameHelpPagesBuilders
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey, getVirtualKey as getVirtualKey
from helpers import dependency as dependency
from items.vehicles import getRolesActions as getRolesActions
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from nations import NAMES as NATIONS_NAMES
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from soft_exception import SoftException as SoftException
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic, getVehicleMechanicsComponents as getVehicleMechanicsComponents
from skeletons.gui.battle_session import IClientArenaVisitor as IClientArenaVisitor
from Vehicle import Vehicle as Vehicle
_logger: Any

class HelpPagePriority(object):
    DEFAULT = 0
    MAPS = 1
    TRACK_WITHIN_TRACK = 2
    BATTLE_ROYALE = 3
    TURBOSHAFT_ENGINE = 4
    DUAL_GUN = 5
    WHEELED = 6
    BURNOUT = 7
    SIEGE_MODE = 8
    MECHANICS = 9
    ROLE_TYPE = 10
    PILLBOX_SIEGE = 16

class DetailedHelpPagesBuilder(object):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def isExclusive(cls):
        ...
    @classmethod
    def isSuitableForCtx(cls, ctx):
        ...
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...
    @classmethod
    def _buildKey(cls, virtualKey, keyName, isLong=False):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class SiegeModePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class BurnOutPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class WheeledPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class TrackWithinTrackPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class DualGunPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class BattleRoyalePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    __battleRoyaleController: Any
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class TurboshaftEnginePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class PillboxSiegePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class RoleTypePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class MapboxPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    _STR_PATH = R.strings.ingame_help.detailsHelp.mapbox
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class DevMapsPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    _STR_PATH = R.strings.ingame_help.detailsHelp.devMaps
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

class MechanicsPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS: tuple
    _VEHICLE_MECHANIC_KEYS: dict
    _VEHICLE_MECHANIC_PRIORITIES: tuple
    @classmethod
    def priority(cls):
        ...
    @classmethod
    def buildPages(cls, ctx):
        ...
    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ...

def addPage(datailedList, headerTitle, title, descr, keys, image, roleImage=None, roleActions=None, hintCtx=None):
    ...
def buildTitle(ctx):
    ...
def buildPagesData(ctx):
    ...
