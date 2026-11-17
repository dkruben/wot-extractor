# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collection/collection_item_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_SOUND_SPACE as ACHIEVEMENTS_SOUND_SPACE
from gui.collection.collections_helpers import getItemInfo as getItemInfo, getVehicleForStyleItem as getVehicleForStyleItem, showCollectionStylePreview as showCollectionStylePreview
from gui.collection.resources.cdn.models import Group as Group, makeImageID as makeImageID
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.collection.collection_item_preview_model import CollectionItemPreviewModel as CollectionItemPreviewModel, ItemType as ItemType
from gui.impl.gen.view_models.views.lobby.collection.pages_blurred_background_model import PagesBlurredBackgroundModel as PagesBlurredBackgroundModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from items.components.c11n_components import splitIntDescr as splitIntDescr
from items.components.c11n_constants import CustomizationType as CustomizationType
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_logger: Any

class CollectionItemPreview(ViewImpl):
    _COMMON_SOUND_SPACE = ACHIEVEMENTS_SOUND_SPACE
    __appLoader: Any
    __collectionsSystem: Any
    __guiLoader: Any
    __itemId: Any
    __collectionId: Any
    __page: Any
    __collection: Any
    __content: Any
    __pagesCount: Any
    def __init__(self, layoutID, itemId, collectionId, page, pagesCount):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillVehicleInfo(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillPagesBlurredBackgrounds(self, model=None):
        ...
    def __updateContentData(self):
        ...
    def __generateContentData(self):
        ...
    def __onContentUpdated(self, isOk, data):
        ...
    def __onClosePreview(self):
        ...
    def __onOpenPreview(self, args):
        ...
    def __openStylePreview(self, itemCD):
        ...
    def __onSettingsChanged(self):
        ...
    def __onDisconnected(self):
        ...
    def __getContent(self, group, sub, name):
        ...

class CollectionItemPreviewWindow(WindowImpl):
    def __init__(self, itemId, collectionId, page, pagesCount):
        ...
