# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collection/awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import SoundGroups as SoundGroups
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.collection.collections_helpers import composeBonuses as composeBonuses
from gui.collection.resources.cdn.models import Group as Group, makeImageID as makeImageID
from gui.collection.sounds import Sounds as Sounds
from gui.impl.auxiliary.collections_helper import getCollectionsBonusPacker as getCollectionsBonusPacker
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.collection.awards_view_model import AwardsViewModel as AwardsViewModel
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView as BattlePassCoinTooltipView
from gui.impl.lobby.collection.tooltips.collection_item_tooltip_view import CollectionItemTooltipView as CollectionItemTooltipView
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showCollectionWindow as showCollectionWindow, showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController
from typing import Dict as Dict
_logger: Any

class AwardsView(ViewImpl):
    __slots__: tuple
    __collectionsSystem: Any
    __collectionId: Any
    __bonuses: Any
    __tooltips: Any
    __content: Any
    def __init__(self, collectionId, bonuses):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __updateContentData(self):
        ...
    def __generateContentData(self):
        ...
    def __onContentUpdated(self, isOk, data):
        ...
    def __fillBackground(self):
        ...
    def __openCollection(self):
        ...
    def __onSettingsChanged(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setAvailability(self, model=None):
        ...
    def __getContent(self, group, sub, name):
        ...

class AwardsWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, collectionId, bonuses):
        ...
