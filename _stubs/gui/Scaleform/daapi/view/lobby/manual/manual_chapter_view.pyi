# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/manual/manual_chapter_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController
from gui.doc_loaders.manual_xml_data_reader import ManualPageTypes as ManualPageTypes
from account_helpers import AccountSettings as AccountSettings
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.meta.ManualChapterViewMeta import ManualChapterViewMeta as ManualChapterViewMeta
from gui.Scaleform.daapi.view.lobby.manual.manual_view_base import ManualViewBase as ManualViewBase
from web.web_client_api import webApiCollection as webApiCollection, ui as ui_web_api, sound as sound_web_api
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
_logger: Any

class ManualChapterView(ManualViewBase, ManualChapterViewMeta):
    BC_HANGAR_GUIDE_CARD_SWIPE_SOUND_ID = 'bc_hangar_guide_card_swipe'
    BC_GUIDE_ELEMENT_BUTTON_SOUND_ID = 'bc_guide_element_button'
    mapsTrainingController: Any
    __chapterIndex: Any
    _pageIndex: Any
    chapterData: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def pageButtonClicked(self, pageType):
        ...
    def buttonHighlighted(self):
        ...
    def _populate(self):
        ...
    def setData(self, chapterIndex, pageIndex):
        ...
    def openVideo(self, url):
        ...
    def onPreviewClicked(self, videoUrl):
        ...
    def onPageChanged(self, pageId):
        ...
    def markPageAsRead(self, pageId):
        ...
    def getUnreadPages(self):
        ...
    def markChapterPagesAsRead(self, chapterUIData):
        ...
    def updatePaginator(self):
        ...
