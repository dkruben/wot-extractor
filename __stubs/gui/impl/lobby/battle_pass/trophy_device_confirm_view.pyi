# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/trophy_device_confirm_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.trophy_device_confirm_bonus_model import TrophyDeviceConfirmBonusModel as TrophyDeviceConfirmBonusModel
from gui.impl.gen.view_models.views.lobby.battle_pass.trophy_device_confirm_dialog_model import TrophyDeviceConfirmDialogModel as TrophyDeviceConfirmDialogModel
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets as DialogPresets
from gui.impl.pub.dialog_window import DialogWindow as DialogWindow, DialogContent as DialogContent, DialogButtons as DialogButtons
from gui.impl.lobby.dialogs.contents.common_balance_content import CommonBalanceContent as CommonBalanceContent
from gui.impl.lobby.dialogs.contents.prices_content import DialogPricesContent as DialogPricesContent
from gui.shared.gui_items import getKpiValueString as getKpiValueString
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
_logger: Any

class TrophyDeviceUpgradeConfirmView(DialogWindow):
    __slots__: tuple
    __itemsCache: Any
    __wallet: Any
    __appLoader: Any
    __trophyBasicModule: Any
    __upgradePrice: Any
    __goldOperationsEnabled: Any
    def __init__(self, trophyBasicModule, parent):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _getResultData(self):
        ...
    def __setUpgradeCost(self):
        ...
    def __canPurchaseUpgrade(self):
        ...
    def __onMoneyUpdated(self, _):
        ...
    def __onWalletStatusChanged(self, *_):
        ...
    def __getSubmitBtnTooltip(self, canUpgrade):
        ...

class TrophyDeviceUpgradeConfirmDialogContent(DialogContent):
    __slots__: tuple
    __itemsCache: Any
    __trophyBasicModule: Any
    __trophyUpgadedModule: Any
    def __init__(self, trophyBasicModule):
        ...
    def _initialize(self):
        ...
