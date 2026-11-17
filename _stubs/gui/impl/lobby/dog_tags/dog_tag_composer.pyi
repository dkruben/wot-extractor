# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/dog_tag_composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
import typing as typing
from enum import Enum as Enum
from gui.impl.lobby.dog_tags.dog_tag_processors import getCoupledDogTagProgress as getCoupledDogTagProgress
from gui.server_events import settings as userSettings
from dog_tags_common.components_config import componentConfigAdapter as componentConfig, SourceData as SourceData, DictIterator as DictIterator
from dog_tags_common.config.common import ComponentViewType as ComponentViewType, ComponentPurpose as ComponentPurpose, NO_PROGRESS as NO_PROGRESS
from dog_tags_common.number_formatter import formatComponentValue as formatComponentValue, customRound as customRound
from gui.dog_tag_composer import DogTagComposerClient as DogTagComposerClient
from gui.impl.gen.view_models.views.lobby.account_dashboard.dog_tag_model import DogTagModel as DogTagModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_component import DtComponent as DtComponent
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_grid_section import DtGridSection as DtGridSection
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from helpers import dependency as dependency
from helpers import getLanguageCode as getLanguageCode
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Iterable as Iterable
from account_helpers.dog_tags import DogTags as DogTags
from dog_tags_common.config.dog_tag_framework import ComponentDefinition as ComponentDefinition
from dog_tags_common.dog_tags_storage import ProgressRecord as ProgressRecord
from dog_tags_common.player_dog_tag import DisplayableDogTag as DisplayableDogTag
from frameworks.wulf import Array as Array
from gui.clans.clan_account_profile import ClanAccountProfile as ClanAccountProfile
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_dog_tag import DtDogTag as DtDogTag
from gui.impl.gen.view_models.views.lobby.dog_tags.dog_tags_view_model import DogTagsViewModel as DogTagsViewModel
_logger: Any
PURPOSE_TO_TOOLTIP_PURPOSE_GROUP_MAP: dict
SECTION_ORDER_MAP: dict
IN_SECTION_ORDER_WEIGHT: list
SECTION_BY_PURPOSE: dict
SECTION_TYPE_BY_COMPONENT_VIEW_TYPE: dict

class TooltipPurposeGroup(Enum):
    TRIUMPH = 'TRIUMPH'
    DEDICATION = 'DEDICATION'
    SEASON = 'SEASON'

class SectionType(Enum):
    BACKGROUND = ComponentViewType.BACKGROUND.value
    ENGRAVING = ComponentViewType.ENGRAVING.value
    COUPLED = 'coupled'

class EngravingSection(Enum):
    TRIUMPH = 'TRIUMPH'
    DEDICATION = 'DEDICATION'
    SKILL = 'SKILL'

class BackgroundSection(Enum):
    TRIUMPH_MEDAL = 'TRIUMPH_MEDAL'

class CoupledSection(Enum):
    Animated = 'ANIMATED'

class DogTagComposerLobby(DogTagComposerClient):
    lobbyContext: Any
    _limitedUIController: Any
    _dtHelper: Any
    serverSettings: Any
    __dossierDescr: Any
    def __init__(self, dtHelper):
        ...
    def fillModel(self, model, dogtag, isUnlocked=True):
        ...
    def fillEntryPoint(self, model):
        ...
    def getSelectedDogTag(self, clanProfile=None):
        ...
    def fillGrid(self, viewModel):
        ...
    def updateComponentModel(self, viewModel, compId):
        ...
    def isDogTagEquipped(self, dogTag):
        ...
    @staticmethod
    def _getVisibleComponents(unlockedComponents):
        ...
    @staticmethod
    def _getCorrespondingCompModel(viewModel, comp):
        ...
    def _fillSectionArray(self, section, components, unlockedComponents, sectionType):
        ...
    def _createSection(self, components, unlockedIds, sectionName):
        ...
    @staticmethod
    def _getSortedKeys(item):
        ...
    def _fillItems(self, components, itemsArray, unlocked):
        ...
    def _fillComponentModel(self, componentDef, model, isUnlocked=True):
        ...
    def __getComponentProgress(self, component):
        ...
    # decorador original: @replace_none_kwargs(...)
    def _getDossier(self, itemsCache=None):
        ...
    @staticmethod
    def __getUnlockThresholdForGrade(compId, grade):
        ...
