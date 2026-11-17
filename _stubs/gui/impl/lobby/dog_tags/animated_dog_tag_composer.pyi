# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/animated_dog_tag_composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
import typing as typing
from dog_tags_common.components_config import componentConfigAdapter as componentConfig
from advanced_achievements_client.getters import getAchievementByID as getAchievementByID
from dog_tags_common.config.common import ComponentViewType as ComponentViewType, ComponentPurpose as ComponentPurpose
from gui.impl.gen.view_models.views.lobby.dog_tags.animated_dog_tag_component import AnimatedDogTagComponent as AnimatedDogTagComponent
from gui.impl.lobby.achievements.profile_utils import fillAdvancedAchievementModel as fillAdvancedAchievementModel
from gui.impl.lobby.dog_tags.dog_tag_composer import DogTagComposerLobby as DogTagComposerLobby
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.server_events import settings as userSettings
from typing import Iterable as Iterable
from dog_tags_common.components_config import DictIterator as DictIterator
from dog_tags_common.player_dog_tag import DisplayableDogTag as DisplayableDogTag
from frameworks.wulf import Array as Array
from gui.clans.clan_account_profile import ClanAccountProfile as ClanAccountProfile
from gui.impl.gen.view_models.views.lobby.dog_tags.animated_dog_tags_view_model import AnimatedDogTagsViewModel as AnimatedDogTagsViewModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.dog_tag_model import DogTagModel as DogTagModel
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel as AdvancedAchievementModel
_logger: Any

class AnimatedDogTagComposer(DogTagComposerLobby):
    def fillModel(self, model, dogtag, isUnlocked=True):
        ...
    def fillEntryPoint(self, model):
        ...
    def fillAnimatedDogTags(self, viewModel, backgroundId=0, engravingId=0):
        ...
    def getSelectedDogTag(self, clanProfile=None):
        ...
    def getInitialIndex(self, itemsArray, backgroundId, engravingId):
        ...
    def fillRequiredAchievement(self, model, unlockKey):
        ...
    def _fillItemsArray(self, itemsArray, components, unlockedIds):
        ...
