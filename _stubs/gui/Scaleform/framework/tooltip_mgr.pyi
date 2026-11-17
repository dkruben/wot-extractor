# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/tooltip_mgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from future.moves import itertools as itertools
import BigWorld as BigWorld
import Keys as Keys
from Event import SafeEvent as SafeEvent, EventManager as EventManager
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewStatus as ViewStatus
from gui import InputHandler as InputHandler
from gui.Scaleform.framework.entities.abstract.ToolTipMgrMeta import ToolTipMgrMeta as ToolTipMgrMeta
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared import events as events
from gui.shared.tooltips import builders as builders
from helpers import dependency as dependency, uniprof as uniprof
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from py2to3.backport.inspect import getargspec as getargspec
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from soft_exception import SoftException as SoftException
ToolTipInfo: Any
_logger: Any
_id_generator: Any
LIVE_REGION_COLOR = 9611473
LOADING_REGION_COLOR = 12757201
_TOOLTIP_VARIANT_TYPED = 'typed'
_TOOLTIP_VARIANT_COMPLEX = 'complex'
_TOOLTIP_VARIANT_WULF = 'wulf'

class ToolTip(ToolTipMgrMeta):
    appLoader: Any
    gui: Any
    _areTooltipsDisabled: Any
    _isAllowedTypedTooltip: Any
    _noTooltipSpaceIDs: Any
    _complex: Any
    _builders: Any
    _dynamic: Any
    __fastRedraw: Any
    __isAdvancedKeyPressed: Any
    __tooltipVariant: Any
    __tooltipID: Any
    __args: Any
    __stateType: Any
    __tooltipInfos: Any
    __tooltipWindowId: Any
    __em: Any
    onShow: Any
    onHide: Any
    def __init__(self, settings, advComplexSettings, *noTooltipSpaceIDs):
        ...
    @property
    def tooltipWindow(self):
        ...
    def show(self, data, linkage):
        ...
    def hide(self):
        ...
    def handleKeyEvent(self, event):
        ...
    def isReadyToHandleKey(self, event):
        ...
    def getTypedTooltipDefaultBuildArgs(self, tooltipType):
        ...
    def onCreateTypedTooltip(self, tooltipType, args, stateType):
        ...
    def onCreateWulfTooltip(self, tooltipType, args, x, y, parent=None, ownerViewID=None):
        ...
    def onCreateComplexTooltip(self, tooltipId, stateType):
        ...
    def onHideTooltip(self, tooltipId):
        ...
    def _onWulfWindowStatusChanged(self, state):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onAccountBecomeNonPlayer(self):
        ...
    def __onGUISpaceEntered(self, spaceID):
        ...
    def __onAppCreating(self, appNS):
        ...
    def isSupportAdvanced(self, tooltipType, *args):
        ...
    def __cacheTooltipData(self, tooltipType, tooltipID, args, stateType):
        ...
    def __destroyTooltipWindow(self):
        ...
