# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/story_choice.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from halloween.gui.impl.gen.view_models.views.lobby.story_choice_view_model import StoryChoiceViewModel as StoryChoiceViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from halloween.gui.shared.event_dispatcher import showStoryChoiceDialog as showStoryChoiceDialog, showAwardCongratsWindow as showAwardCongratsWindow
from halloween.gui.shared.gui_items.processors.processors import ChoiceProcessor as ChoiceProcessor
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import STORY_CHOICE_WINDOW_EXIT as STORY_CHOICE_WINDOW_EXIT, STORY_CHOICE_WINDOW_ENTER as STORY_CHOICE_WINDOW_ENTER
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui import SystemMessages as SystemMessages
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.utils import decorators as decorators
from gui.shared.utils.decorators import adisp_async as adisp_async
from helpers import dependency as dependency
from halloween.gui.impl.lobby.hw_helpers import getEndingToken as getEndingToken
from halloween_common.halloween_constants import HWStoryChoiceSettings as HWStoryChoiceSettings
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, wg_await as wg_await

class StoryChoiceView(BaseView):
    __slots__: tuple
    layoutID: Any
    _hwArtifactsCtrl: Any
    __itemsCache: Any
    def __init__(self, layoutID=None):
        ...
    @property
    def viewModel(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def __acrualArtefact(self, artefactID):
        ...
    # decorador original: @wg_async
    def __onSelectSide(self, args):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def __acrualChoice(self, choiceID):
        ...

class StoryChoiceWindow(LobbyNotificationWindow):
    _args: Any
    def __init__(self, layoutID, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
