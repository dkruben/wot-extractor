# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/dog_tags_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from account_helpers.AccountSettings import AccountSettings as AccountSettings, DOG_TAGS as DOG_TAGS
from constants import DOG_TAGS_CONFIG as DOG_TAGS_CONFIG
from gui.impl.gen.view_models.views.lobby.account_dashboard.dog_tags_model import DogTagsModel as DogTagsModel
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.lobby.dog_tags.animated_dog_tag_composer import AnimatedDogTagComposer as AnimatedDogTagComposer
from gui.impl.lobby.dog_tags.dog_tag_composer import DogTagComposerLobby as DogTagComposerLobby
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showDogTags as showDogTags, showAnimatedDogTags as showAnimatedDogTags
from gui.shared.events import DogTagsEvent as DogTagsEvent
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, ILimitedUIController as ILimitedUIController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class DogTagsFeature(FeatureItem):
    __lobbyContext: Any
    __gameSession: Any
    __limitedUIController: Any
    __slots__: tuple
    _dtHelper: Any
    _customizableComposer: Any
    _animatedComposer: Any
    def __init__(self, viewModel):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _fillModel(self, model):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def __updatePrem(self, *_):
        ...
    def __onDogTagDataChanged(self, diff):
        ...
    def __onCountersUpdated(self, event):
        ...
    def __onLuiRuleDogTagCompleted(self, *_):
        ...
    def __onAccountSettingsChanging(self, key, _):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateModel(self, model=None):
        ...
    @staticmethod
    def __onCustomizableDogTagClick():
        ...
    @staticmethod
    def __onAnimatedDogTagClick():
        ...
