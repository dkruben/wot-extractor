# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/dialogs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from frameworks.wulf import WindowStatus as WindowStatus
from gui.impl.gen import R as R
from gui.impl.lobby.battle_pass.trophy_device_confirm_view import TrophyDeviceUpgradeConfirmView as TrophyDeviceUpgradeConfirmView
from gui.impl.lobby.blueprints.blueprints_conversion_view import BlueprintsConversionView as BlueprintsConversionView
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import isPremiumRetrainWarning as isPremiumRetrainWarning
from gui.impl.lobby.crew.dialogs.mentor_assignment_dialog import MentorAssignmentDialog as MentorAssignmentDialog
from gui.impl.lobby.crew.dialogs.skills_training_confirm_dialog import SkillsTrainingConfirmDialog as SkillsTrainingConfirmDialog
from gui.impl.lobby.crew.free_skill_confirmation_dialog import FreeSkillConfirmationDialog as FreeSkillConfirmationDialog
from gui.impl.lobby.dialogs.exchange_with_items import ExchangeToBuyItems as ExchangeToBuyItems, ExchangeToUpgradeDevice as ExchangeToUpgradeDevice
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper as FullScreenDialogWindowWrapper
from gui.impl.lobby.dialogs.quit_game_dialog import QuitGameDialogWindow as QuitGameDialogWindow
from gui.impl.lobby.dialogs.wot_plus.base_dialog import BaseDialog as BaseDialog
from gui.impl.lobby.dialogs.wot_plus.pro_boost_confirm_dialog import ProBoostConfirmDialog as ProBoostConfirmDialog
from gui.impl.lobby.dialogs.wot_plus.pro_boost_switch_dialog import ProBoostSwitchDialog as ProBoostSwitchDialog
from gui.impl.lobby.dialogs.wot_plus.service_record_customization_confirm_dialog import ServiceRecordCustomizationConfirmDialog as ServiceRecordCustomizationConfirmDialog
from gui.impl.lobby.dialogs.wot_plus.subscription_award_dialog import SubscriptionAwardDialog as SubscriptionAwardDialog
from gui.impl.lobby.tank_setup.upgradable_device.UpgradeDeviceView import UpgradableDeviceUpgradeConfirmView as UpgradableDeviceUpgradeConfirmView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons, DialogWindow as DialogWindow, SingleDialogResult as SingleDialogResult
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from wg_async import wg_async as wg_async, wg_await as wg_await
from typing import Any as Any, Optional as Optional, Union as Union, List as List
from gui.impl.lobby.dialogs.wot_plus.pro_boost_confirm_dialog import _ProBoostConfirmDialogParams as _ProBoostConfirmDialogParams
from gui.impl.lobby.dialogs.wot_plus.pro_boost_switch_dialog import _ProBoostSwitchDialogParams as _ProBoostSwitchDialogParams

# decorador original: @wg_async
def show(dialog):
    ...
# decorador original: @wg_async
def showSimpleWithResultData(dialog, submitResults=...):
    ...
# decorador original: @wg_async
def showSimple(dialog, submitResult=...):
    ...
# decorador original: @wg_async
# decorador original: @dependency.replace_none_kwargs(...)
def quitGame(parent=None, guiLoader=None):
    ...
# decorador original: @wg_async
def blueprintsConversion(vehicleCD, fragmentCount=1, parent=None):
    ...
# decorador original: @wg_async
def trophyDeviceUpgradeConfirm(trophyBasicModule, parent=None):
    ...
# decorador original: @wg_async
def modernizedDeviceUpgradeConfirm(currentModule, vehicle=None, onDeconstructed=None, parent=None):
    ...
# decorador original: @wg_async
def showExchangeToBuyItemsDialog(itemsCountMap, parent=None):
    ...
# decorador original: @wg_async
def showSingleDialog(wrappedViewClass, layoutID, parent=None, **kwargs):
    ...
# decorador original: @wg_async
def showSingleDialogWithResultData(wrappedViewClass, layoutID, parent=None, **kwargs):
    ...
# decorador original: @wg_async
# decorador original: @dependency.replace_none_kwargs(...)
def showCustomBlurSingleDialog(wrappedViewClass, layoutID, parent=None, gui=None, **kwargs):
    ...
# decorador original: @wg_async
def showExchangeToUpgradeDeviceDialog(device, parent=None):
    ...
# decorador original: @wg_async
def showFreeSkillConfirmationDialog(skill):
    ...
# decorador original: @wg_async
def showLearnPerkConfirmationDialog(skill, level):
    ...
# decorador original: @wg_async
def showPerksDropDialog(tankmanId):
    ...
# decorador original: @wg_async
def showRetrainMassiveDialog(tankmenIds, vehicleCD):
    ...
# decorador original: @wg_async
def showRetrainSingleDialog(tankmanId, vehicleCD, targetRole=None, targetSlotIdx=None, isChangeRoleVisible=False, beforeActions=None):
    ...
# decorador original: @wg_async
def showRetrainPremiumVehicleDialog(vehicleCD, isMassive=False):
    ...
# decorador original: @wg_async
def showRecruitNewTankmanDialog(vehicleCD, slotIdx, putInTank=False):
    ...
# decorador original: @wg_async
def showEnlargeBarracksDialog():
    ...
# decorador original: @wg_async
def showCrewBooksPurchaseDialog(crewBookCD):
    ...
# decorador original: @wg_async
def showDocumentChangeDialog(tankmanInvID, ctx=None):
    ...
# decorador original: @wg_async
def showSkinApplyDialog(crewSkinID, tankManInvID):
    ...
# decorador original: @wg_async
def showDismissTankmanDialog(tankmanId):
    ...
# decorador original: @wg_async
def showRestoreTankmanDialog(tankmanId, vehicleId, slotIdx):
    ...
# decorador original: @wg_async
def showSkillsTrainingConfirmDialog(tankman, skillsRole, skillsList, availableSkillsData):
    ...
# decorador original: @wg_async
def showMentorAssignmentConfirmDialog(sourceTmanId, targetTmanId):
    ...
# decorador original: @wg_async
def showProBoostConfirmDialog(dialogParams):
    ...
# decorador original: @wg_async
def showProBoostSwitchDialog(dialogParams):
    ...
# decorador original: @wg_async
def showServiceRecordCustomizationConfirmDialog():
    ...
# decorador original: @wg_async
def showRenewableSubscriptionRewardDialog(unlockedTier, expirationTime, billingDays, messageType):
    ...
# decorador original: @wg_async
def showBaseDialog(layoutID=...):
    ...
