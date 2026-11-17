# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/rent_confirm_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta as I18nConfirmDialogMeta, DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import formatPrice as formatPrice, text_styles as text_styles
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class RentConfirmDialogMeta(I18nConfirmDialogMeta):
    epicController: Any
    itemsCache: Any
    _messageCtx: Any
    def __init__(self, intCD, rentType, nums=..., price=..., seasonType=0, renew=False):
        ...
