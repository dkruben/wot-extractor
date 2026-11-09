# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/dialogs/contents/easy_tank_equip_exchange_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.gen.view_models.views.lobby.exchange.currency_model import CurrencyType as CurrencyType
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeContent as ExchangeContent
from gui.impl.lobby.exchange.currency_tab_view import getCurrencyValueFromType as getCurrencyValueFromType
from gui.impl.gen.view_models.common.exchange_panel_model import ExchangePanelModel as ExchangePanelModel
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeMoneyInfo as ExchangeMoneyInfo

class EasyTankEquipExchangeContent(ExchangeContent):
    __availableGoldAmount: Any
    def __init__(self, fromItem, toItem, viewModel=None, needItem=0, availableGoldAmount=0):
        ...
    def _getAvailableGoldAmount(self):
        ...
