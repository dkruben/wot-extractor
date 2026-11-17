# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/attachments_preview/attachments_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachment_bonus_model import AttachmentBonusModel as AttachmentBonusModel
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachments_preview_model import AttachmentsPreviewModel as AttachmentsPreviewModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.server_events.bonuses import parseAttachmentsSetToken as parseAttachmentsSetToken
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID
from helpers import dependency as dependency
from items.components.c11n_constants import Rarity as Rarity
from skeletons.gui.customization import ICustomizationService as ICustomizationService
_RARITY_PRIORITY: dict

class AttachmentsPreview(ViewImpl):
    __customization: Any
    LAYOUT_ID: Any
    __tooltips: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, setTokenID, feature, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __fillModel(self, setTokenID, feature):
        ...
    def __getSortedAttachments(self, attachmentIDs):
        ...
    def __packAttachment(self, attachment):
        ...

class AttachmentsPreviewWindow(WindowImpl):
    def __init__(self, setTokenID, feature):
        ...
