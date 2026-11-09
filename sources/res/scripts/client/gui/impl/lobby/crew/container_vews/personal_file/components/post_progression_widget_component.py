# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/components/post_progression_widget_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/personal_file/components/post_progression_widget_component.py
import typing
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache
from gui.impl.gen import R
from gui.impl.lobby.container_views.base.components import ComponentBase
from gui.impl.lobby.crew.tooltips.post_progression_tooltip import PostProgressionTooltip
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from shared_utils import first
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Tuple
    from gui.impl.gen.view_models.views.lobby.crew.personal_case.post_progression_widget_model import PostProgressionWidgetModel
    from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_file_view_model import PersonalFileViewModel

class PostProgressionWidgetComponent(ComponentBase):
    _itemsCache = dependency.descriptor(IItemsCache)
    _appLoader = dependency.descriptor(IAppLoader)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.crew.tooltips.PostProgressionTooltip():
            return PostProgressionTooltip(self.context.tankmanID)

    def _getViewModel(self, vm):
        return vm.postProgression

    def _getEvents(self):
        return super(PostProgressionWidgetComponent, self)._getEvents() + (
         (
          self.viewModel.onWidgetClick, self._onWidgetClick),)

    def _fillViewModel(self, vm):
        self._setPostProgression(vm)

    def _setPostProgression(self, vm):
        crewBooksCache = crewBooksViewedCache()
        rewardBookId = crewBooksCache.rewardBookId()
        crewBook = first(self._itemsCache.items.getItems(GUI_ITEM_TYPE.CREW_BOOKS, REQ_CRITERIA.CREW_ITEM.ID(rewardBookId)).values())
        postProgressionXP = self._itemsCache.items.stats.postProgressionXP
        _, postProgressionXP = divmod(postProgressionXP, crewBook.getXP()) if postProgressionXP > 0 else (0,
                                                                                                          0)
        if crewBook:
            vm.setIcon(R.images.gui.maps.icons.crewBooks.books.big.dyn(crewBook.getBookType(), None)())
        vm.setProgressCurrent(postProgressionXP)
        vm.setProgressMax(crewBooksViewedCache().xppToConvert())
        vm.setHasWarning(not self.parent.context.tankman.isMaxSkillEfficiency)
        return

    def _onWidgetClick(self):
        self.events.onWidgetClick()
