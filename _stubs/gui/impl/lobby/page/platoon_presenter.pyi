# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/platoon_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import typing as t
import BigWorld as BigWorld
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, SquadManStates as SquadManStates, EPlatoonButtonState as EPlatoonButtonState, QUEUE_TYPE as QUEUE_TYPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.game_control.platoon_controller import PopoverParams as PopoverParams
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.page.footer.platoon_member_model import PlatoonMemberModel as PlatoonMemberModel
from gui.impl.gen.view_models.views.lobby.page.footer.platoon_model import PlatoonModel as PlatoonModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IPlatoonController as IPlatoonController, IHangarGuiController as IHangarGuiController
from frameworks.wulf import ViewEvent as ViewEvent, Window as Window
from gui.impl.lobby.platoon.platoon_config import SquadInfo as SquadInfo

# base nao representavel no stub: ViewComponent[...]
class PlatoonPresenter(IGlobalListener):
    __platoonCtrl: Any
    __appLoader: Any
    __hangarGuiCtrl: Any
    app: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createPopOver(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onUnitSizeChanged(self):
        ...
    def onEnqueued(self, *args, **kwargs):
        ...
    def onDequeued(self, *args, **kwargs):
        ...
    def onEnqueueError(self, *args, **kwargs):
        ...
    def onArenaJoinFailure(self, *args, **kwargs):
        ...
    def onKickedFromQueue(self, *args, **kwargs):
        ...
    def onKickedFromArena(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onInPlatoonAction(self):
        ...
    def _onUpdatePlatoon(self):
        ...
    def __onUpdatePrbControls(self, *_):
        ...
    def __getTooltip(self, extendedSquadInfoVo, isInSquad):
        ...
    def __getPlayerIndex(self):
        ...
    def __isNotAllowedQueueType(self):
        ...
