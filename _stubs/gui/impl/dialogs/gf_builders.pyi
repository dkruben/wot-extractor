# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/gf_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import WindowLayer as WindowLayer, PyResAccessor as PyResAccessor
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView, DEFAULT_DIMMER_ALPHA as DEFAULT_DIMMER_ALPHA
from gui.impl.dialogs.sub_views.common.simple_text import ImageSubstitution as ImageSubstitution
from gui.impl.dialogs.sub_views.content.text_warning_content import TextWithWarning as TextWithWarning
from gui.impl.dialogs.dialog_template_button import ButtonPresenter as ButtonPresenter, CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.dialog_template_utils import toString as toString
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent as SimpleTextContent
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet as IconSet
from gui.impl.dialogs.sub_views.icon.item_icon import ItemIcons as ItemIcons
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as DefaultDialogPlaceHolders
from gui.impl.gen.view_models.views.dialogs.sub_views.multiple_icons_set_view_model import IconPositionLogicEnum as IconPositionLogicEnum
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType as ButtonType
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper as FullScreenDialogWindowWrapper
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from typing import Optional as Optional, List as List, Union as Union

class BuilderDialogTemplateView(DialogTemplateView):
    __slots__: tuple
    def _closeClickHandler(self, args=None):
        ...

class BaseDialogBuilder(object):
    __slots__: tuple
    __title: Any
    __description: Any
    __icon: Any
    __buttons: Any
    __uniqueID: Any
    __backgroundID: Any
    __dimmerAlpha: Any
    __layoutID: Any
    __selectedButtonID: Any
    __doBlur: Any
    __layer: Any
    __displayFlags: Any
    def __init__(self, uniqueID=None):
        ...
    def buildView(self):
        ...
    def build(self):
        ...
    def setTitle(self, text):
        ...
    def setDescription(self, text):
        ...
    def setIcon(self, mainIcon, backgrounds=None, overlays=None, layoutID=None, iconPositionLogic=...):
        ...
    def addButton(self, buttonSettings):
        ...
    def getButton(self, buttonID):
        ...
    def setBackground(self, resourceID):
        ...
    def setDimmerAlpha(self, value):
        ...
    def setLayoutID(self, layoutID):
        ...
    def setFocusedButtonID(self, buttonID):
        ...
    def setBlur(self, value=True):
        ...
    def setLayer(self, layerID):
        ...
    def setDisplayFlags(self, *displayFlags):
        ...
    def _extendTemplate(self, template):
        ...

class ResDialogBuilder(BaseDialogBuilder):
    __slots__: tuple
    __showBalance: Any
    def __init__(self, uniqueID=None):
        ...
    def setShowBalance(self, value):
        ...
    def setMessagesAndButtons(self, message, buttons=..., focusedButtonID=...):
        ...
    def _extendTemplate(self, template):
        ...

class ConfirmCancelDialogBuilder(BaseDialogBuilder):
    __slots__: tuple
    def __init__(self, uniqueID=None):
        ...
    def setConfirmButtonLabel(self, text):
        ...
    def setCancelButtonLabel(self, text):
        ...

class ConfirmCancelWarningDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__: tuple
    __descriptionMsg: Any
    __warningMsg: Any
    def __init__(self, uniqueID=None):
        ...
    def setDescription(self, text):
        ...
    def setDescriptionMsg(self, text):
        ...
    def setWarningMsg(self, text):
        ...
    def _extendTemplate(self, template):
        ...

class ConfirmCancelDescriptionDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__: tuple
    __descriptionMsg: Any
    def __init__(self, uniqueID=None):
        ...
    def setDescriptionMsg(self, text):
        ...
    def _extendTemplate(self, template):
        ...

class AlertBuilder(BaseDialogBuilder):
    __slots__: tuple
    def __init__(self, uniqueID=None):
        ...
    def setButtonLabel(self, text):
        ...

class InfoDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__: tuple
    def __init__(self, uniqueID=None):
        ...

class AcceleratedCrewTrainingDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__: tuple
    def __init__(self, uniqueID=None):
        ...

class PassiveXPDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__: tuple
    __descriptionMsg: Any
    __iconFrom: Any
    __iconTo: Any
    __vehsCD: Any
    def __init__(self, uniqueID=None):
        ...
    def setDescriptionMsg(self, text):
        ...
    def setMessageIconFrom(self, icon):
        ...
    def setMessageIconTo(self, icon):
        ...
    def setVehiclesCD(self, vehsCD):
        ...
    def _extendTemplate(self, template):
        ...

class WarningDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__: tuple
    def __init__(self, uniqueID=None):
        ...

class ErrorAlertBuilder(AlertBuilder):
    __slots__: tuple
    def __init__(self, uniqueID=None):
        ...
