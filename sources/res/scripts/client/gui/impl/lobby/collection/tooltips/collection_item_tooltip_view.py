# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/collection/tooltips/collection_item_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/collection/tooltips/collection_item_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.collection.collections_helpers import getItemResKey, getCollectionRes, getItemName, getImagePath
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.collection.tooltips.collection_item_tooltip_view_model import CollectionItemTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import ICollectionsSystemController

class CollectionItemTooltipView(ViewImpl):
    __slots__ = ('__collectionId', '__item', '__isDetailed')
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)

    def __init__(self, itemId, collectionId, isDetailed, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.collection.tooltips.CollectionItemTooltipView())
        settings.model = CollectionItemTooltipViewModel()
        settings.args = args
        settings.kwargs = kwargs
        self.__collectionId = collectionId
        self.__item = self.__collectionsSystem.getCollectionItem(self.__collectionId, itemId)
        self.__isDetailed = isDetailed
        super(CollectionItemTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CollectionItemTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CollectionItemTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            model.setName(getItemName(self.__collectionId, self.__item, collectionsSystem=self.__collectionsSystem))
            model.setImagePath(self.__getImage())
            model.setDescription(self.__getDescription())
            model.setIsReceived(self.__collectionsSystem.isItemReceived(self.__collectionId, self.__item.itemId))
            model.setIsDetailed(self.__isDetailed)

    def __getDescription(self):
        itemRes = getCollectionRes(self.__collectionId, collectionsSystem=self.__collectionsSystem).item
        isItemAvailable = self.__collectionsSystem.isRelatedEventActive(self.__collectionId)
        conditionRes = itemRes.condition.available if isItemAvailable else itemRes.condition.unavailable
        return backport.text(conditionRes.dyn(getItemResKey(self.__collectionId, self.__item))())

    def __getImage(self):
        return getImagePath(R.images.gui.maps.icons.collectionItems.c_296x222.dyn(getItemResKey(self.__collectionId, self.__item)))
