# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/bestiary_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName
from halloween.gui.impl.gen.view_models.views.lobby.bestiary_view_model import BestiaryViewModel as BestiaryViewModel
from halloween.gui.impl.gen.view_models.views.lobby.enemy_model import EnemyModel as EnemyModel
from halloween.gui.impl.lobby.hw_helpers.bestiary_helper import getEnemyRole as getEnemyRole, isEnemyUnlocked as isEnemyUnlocked, getUnlockMissionIdx as getUnlockMissionIdx, getEnemiesSeenList as getEnemiesSeenList, markEnemyAsSeen as markEnemyAsSeen, getLastSelectedEnemy as getLastSelectedEnemy, setLastSelectedEnemy as setLastSelectedEnemy
from halloween.gui.impl.lobby.widgets.shop_style_panel import ShopStylePanelPresenter as ShopStylePanelPresenter
from halloween.gui.shared.event_dispatcher import showBestiaryWindow as showBestiaryWindow
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import BESTIARY_ENTER as BESTIARY_ENTER, BESTIARY_EXIT as BESTIARY_EXIT
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys, HWLogActions as HWLogActions
from helpers import dependency as dependency
from items.vehicles import getVehicleType as getVehicleType

class BestiaryView(ViewComponent):
    __hwBestiaryCtrl: Any
    __enemyIntCD: Any
    __uiLogger: Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getChildComponents(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...
    @staticmethod
    def __onMoveSpace(moveTypeArgs=None):
        ...
    # decorador original: @args2params(...)
    def __onSelectEnemy(self, intCD):
        ...
    @staticmethod
    def __onResize(args):
        ...
    def __onSettingsUpdate(self):
        ...
    def __selectEnemy(self, vm, intCD, isInit=False):
        ...
    def __updateEnemiesModel(self, vm):
        ...

class BestiaryWindow(WindowImpl):
    def __init__(self, layer, ctx, **_):
        ...
