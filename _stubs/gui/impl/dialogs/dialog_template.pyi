# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/dialog_template.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, ViewStatus as ViewStatus
from gui.impl.dialogs.dialog_template_focus import BaseFocusPresenter as BaseFocusPresenter, DialogTemplateFocusingSystem as DialogTemplateFocusingSystem
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.dialog_template_place_holder_view_model import DialogTemplatePlaceHolderViewModel as DialogTemplatePlaceHolderViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel as DialogTemplateViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from typing import List as List, Dict as Dict, Optional as Optional
from frameworks.wulf import View as View
from gui.impl.dialogs.dialog_template_button import ButtonPresenter as ButtonPresenter
DEFAULT_DIMMER_ALPHA = 0.5

class DialogTemplateView(FullScreenDialogBaseView):
    __slots__: tuple
    __appLoader: Any
    LAYOUT_ID: Any
    VIEW_MODEL = DialogTemplateViewModel
    _subViews: Any
    __buttonPresenters: Any
    __uniqueID: Any
    __focusingSystem: Any
    def __init__(self, layoutID=None, uniqueID=None, *args, **kwargs):
        ...
    @property
    def dialogUniqueID(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _closeClickHandler(self, _=None):
        ...
    def _buttonClickHandler(self, args):
        ...
    def addButton(self, buttonPresenter):
        ...
    def getButton(self, buttonID):
        ...
    def setSubView(self, placeHolderName, view):
        ...
    def getSubView(self, placeHolderName):
        ...
    def setBackgroundImagePath(self, resourceID):
        ...
    def removeBackgroundDimmer(self):
        ...
    def setBackgroundDimmerAlpha(self, alpha):
        ...
    def setDisplayFlags(self, *flags):
        ...
    def clearDisplayFlags(self):
        ...
    def setFocusedIndex(self, value):
        ...
