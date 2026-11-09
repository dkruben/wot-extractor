# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/battle_entry.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from frameworks.wulf import WindowLayer as WindowLayer
from gui import DEPTH_OF_Battle as DEPTH_OF_Battle
from gui.shared.system_factory import collectBattleEntry as collectBattleEntry, collectBattleTooltipsBuilders as collectBattleTooltipsBuilders
from gui.Scaleform import SCALEFORM_SWF_PATH_V3 as SCALEFORM_SWF_PATH_V3
from gui.Scaleform.flash_wrapper import InputKeyMode as InputKeyMode
from gui.Scaleform.framework.managers.TutorialManager import ScaleformTutorialManager as ScaleformTutorialManager
from gui.Scaleform.framework.tooltip_mgr import ToolTip as ToolTip
from gui.Scaleform.framework.ui_logging_manager import UILoggerManager as UILoggerManager
from gui.Scaleform.framework.application import AppEntry as AppEntry, DAAPIRootBridge as DAAPIRootBridge
from gui.Scaleform.framework.managers import LoaderManager as LoaderManager, ContainerManager as ContainerManager
from gui.Scaleform.framework.managers.containers import DefaultContainer as DefaultContainer
from gui.Scaleform.framework.managers.containers import PopUpContainer as PopUpContainer
from gui.Scaleform.framework.managers.context_menu import ContextMenuManager as ContextMenuManager
from gui.Scaleform.framework.managers.optimization_manager import GraphicsOptimizationManager as GraphicsOptimizationManager
from gui.Scaleform.managers.ColorSchemeManager import BattleColorSchemeManager as BattleColorSchemeManager
from gui.Scaleform.managers.cursor_mgr import CursorManager as CursorManager
from gui.Scaleform.managers.GlobalVarsManager import GlobalVarsManager as GlobalVarsManager
from gui.Scaleform.managers.PopoverManager import PopoverManager as PopoverManager
from gui.Scaleform.framework.managers.ImageManager import ImageManager as ImageManager
from gui.Scaleform.required_libraries_config import BATTLE_REQUIRED_LIBRARIES as BATTLE_REQUIRED_LIBRARIES, ADDITIONAL_BATTLE_REQUIRED_LIBRARIES as ADDITIONAL_BATTLE_REQUIRED_LIBRARIES
from gui.sounds.SoundManager import SoundManager as SoundManager
from gui.Scaleform.managers.TweenSystem import TweenManager as TweenManager
from gui.Scaleform.managers.UtilsManager import UtilsManager as UtilsManager
from gui.Scaleform.managers.battle_input import BattleGameInputMgr as BattleGameInputMgr
from gui.Scaleform.managers.voice_chat import BattleVoiceChatManager as BattleVoiceChatManager
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import uniprof as uniprof
from skeletons.gui.app_loader import GuiGlobalSpaceID as GuiGlobalSpaceID

class TopWindowContainer(PopUpContainer):
    __app: Any
    def __init__(self, layer, app, manager=None):
        ...
    def clear(self):
        ...
    def addView(self, pyView):
        ...
    def removeView(self, pyView):
        ...

class BattleEntry(AppEntry):
    _arenaGuiType: Any
    __input: Any
    def __init__(self, appNS, ctrlModeFlags, arenaGuiType):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def afterCreate(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def beforeDelete(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def enterGuiControlMode(self, consumerID, cursorVisible=True, enableAiming=True, stopVehicle=False):
        ...
    def leaveGuiControlMode(self, consumerID):
        ...
    def hasGuiControlModeConsumers(self, *consumersIDs):
        ...
    def registerGuiKeyHandler(self, handler):
        ...
    def unregisterGuiKeyHandler(self, handler):
        ...
    def _createLoaderManager(self):
        ...
    def _createContainerManager(self):
        ...
    def _createToolTipManager(self):
        ...
    def _createGlobalVarsManager(self):
        ...
    def _createSoundManager(self):
        ...
    def _createCursorManager(self):
        ...
    def _createColorSchemeManager(self):
        ...
    def _createVoiceChatManager(self):
        ...
    def _createUtilsManager(self):
        ...
    def _createContextMenuManager(self):
        ...
    def _createTutorialManager(self):
        ...
    def _createUILoggerManager(self):
        ...
    def _createImageManager(self):
        ...
    def _createPopoverManager(self):
        ...
    def _createTweenManager(self):
        ...
    def _createGraphicsOptimizationManager(self):
        ...
    def _setup(self):
        ...
    def _loadWaiting(self):
        ...
    def _getRequiredLibraries(self):
        ...
    def __getCursorFromContainer(self):
        ...
