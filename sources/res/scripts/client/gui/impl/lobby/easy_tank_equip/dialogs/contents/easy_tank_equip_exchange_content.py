# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/dialogs/contents/easy_tank_equip_exchange_content.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/easy_tank_equip/dialogs/contents/easy_tank_equip_exchange_content.py
from typing import TYPE_CHECKING
from gui.impl.gen.view_models.views.lobby.exchange.currency_model import CurrencyType
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeContent
from gui.impl.lobby.exchange.currency_tab_view import getCurrencyValueFromType
if TYPE_CHECKING:
    from gui.impl.gen.view_models.common.exchange_panel_model import ExchangePanelModel
    from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeMoneyInfo

class EasyTankEquipExchangeContent(ExchangeContent):

    def __init__(self, fromItem, toItem, viewModel=None, needItem=0, availableGoldAmount=0):
        super(EasyTankEquipExchangeContent, self).__init__(fromItem, toItem, viewModel, needItem)
        self.__availableGoldAmount = availableGoldAmount

    def _getAvailableGoldAmount(self):
        availableGoldAmount = getCurrencyValueFromType(CurrencyType.GOLD) if self.__availableGoldAmount == 0 else self.__availableGoldAmount
        return availableGoldAmount
