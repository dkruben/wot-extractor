# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/lootbox_system/base/bonuses_packers.pyc (uncompyle6 3.9.3 / Python 3.14.3) - nao e o codigo original
# uncompyle6 version 3.9.3
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lootbox_system/base/bonuses_packers.py
import logging
from typing import TYPE_CHECKING
from battle_pass_common import CurrencyBP
from constants import PREMIUM_ENTITLEMENTS
from gui import GUI_NATIONS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.customization.shared import getSingleVehicleForCustomization
from gui.impl import backport
from gui.impl.backport import TooltipData, createTooltipData
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.lootbox_system.bonus_model import BonusModel, BonusRarity, VehicleType
from gui.lootbox_system.base.awards_manager import AwardsManager
from gui.lootbox_system.base.common import LOOTBOX_RANDOM_NATIONAL_BLUEPRINT, LOOTBOX_RANDOM_NATIONAL_BROCHURE, LOOTBOX_RANDOM_NATIONAL_CREW_BOOK, LOOTBOX_RANDOM_NATIONAL_GUIDE, LOOTBOX_COMPENSATION_BONUS
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN, CREW_BONUS_X3_TOKEN
from gui.server_events.bonuses import BlueprintsBonusSubtypes, LootBoxRandomNationalBonus, PlusPremiumDaysBonus, VehiclesBonus, _BONUSES, LootBoxTokensBonus
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Vehicle import getIconResourceName, getNationLessName, getUnicName
from gui.shared.gui_items.customization import CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker, BlueprintBonusUIPacker, BonusUIPacker, CrewBookBonusUIPacker, CrewSkinBonusUIPacker, GoodiesBonusUIPacker, ItemBonusUIPacker, SimpleBonusUIPacker, TokenBonusUIPacker, VehiclesBonusUIPacker, getDefaultBonusPackersMap, getLocalizedBonusName, CurrenciesBonusUIPacker
from gui.shared.money import Currency, Money
from gui.shared.utils.functions import makeTooltip
from helpers import dependency, int2roman
from items.components.crew_books_constants import CREW_BOOK_RARITY
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first
from skeletons.gui.shared import IItemsCache
if TYPE_CHECKING:
    from typing import Dict, List, Optional, Tuple, Union
    from frameworks.wulf import Array
    from gui.impl.wrappers.user_list_model import UserListModel
    from gui.server_events.bonuses import CustomizationsBonus, SimpleBonus, TokensBonus
    BonusModelsList = Union[(Array[BonusModel], UserListModel[BonusModel])]
_logger = logging.getLogger(__name__)
VEH_COMP_R_ID = R.views.lobby.awards.tooltips.RewardCompensationTooltip()
_LOOTBOX_BONUS_NAME = 'lootBox'
_EXTRA_BONUSES_NAMES = ('slots', )
_MAIN_REWARD_COUNT_RARE_OR_EPIC = 3
_MAIN_REWARD_COUNT = 4

def getLootBoxesBonusPackerMap():
    simplePacker = LootBoxSimpleBonusUIPacker()
    blueprintPacker = LootBoxBlueprintBonusUIPacker()
    specialRandomPacker = LootBoxSpecialRandomBonusUIPacker()
    return {'battleToken': LootBoxTokenBonusUIPacker, 
       'blueprints': blueprintPacker, 
       'blueprintsAny': blueprintPacker, 
       'crewBooks': (LootBoxCrewBookBonusUIPacker()), 
       'crewSkins': (LootBoxCrewSkinBonusUIPacker()), 
       'customizations': LootBoxCustomizationsBonusUIPacker, 
       'currencies': (LootBoxCurrenciesBonusUIPacker()), 
       'finalBlueprints': blueprintPacker, 
       'goodies': (LootBoxGoodiesBonusUIPacker()), 
       'items': (LootBoxItemBonusUIPacker()), 
       'slots': (LootBoxSlotsBonusUIPacker()), 
       'tmanToken': (LootBoxTmanTemplateBonusUIPacker()), 
       'tokens': LootBoxTokenBonusUIPacker, 
       'vehicles': (LootBoxVehiclesBonusUIPacker()), 
       (Currency.FREE_XP): simplePacker, 
       (Currency.CREDITS): simplePacker, 
       (Currency.GOLD): simplePacker, 
       (Currency.EQUIP_COIN): simplePacker, 
       (Currency.CRYSTAL): simplePacker, 
       (Currency.BPCOIN): (LootBoxBPCoinBonusUIPacker()), 
       (PREMIUM_ENTITLEMENTS.PLUS): (LootBoxPremiumBonusUIPacker()), 
       LOOTBOX_RANDOM_NATIONAL_BLUEPRINT: specialRandomPacker, 
       LOOTBOX_RANDOM_NATIONAL_BROCHURE: specialRandomPacker, 
       LOOTBOX_RANDOM_NATIONAL_GUIDE: specialRandomPacker, 
       LOOTBOX_RANDOM_NATIONAL_CREW_BOOK: specialRandomPacker, 
       _LOOTBOX_BONUS_NAME: (LootBoxesLootBoxBonusUIPacker()), 
       LOOTBOX_COMPENSATION_BONUS: (LootBoxCompensationPacker())}


def getLootBoxesBonusPacker(eventName):
    mapping = getDefaultBonusPackersMap()
    lootBoxPackersMap = getLootBoxesBonusPackerMap()
    for packer in lootBoxPackersMap.itervalues():
        packer.init(eventName)

    mapping.update(lootBoxPackersMap)
    return BonusUIPacker(mapping)


def packBonusModelAndTooltipData(bonuses, bonusModelsList, eventName, tooltipData=None, merge=False, packer=None, showLootboxCompensation=False):
    if packer is None:
        packer = getLootBoxesBonusPacker(eventName)
    bonusIndexTotal = 0
    if tooltipData is not None:
        bonusIndexTotal = len(tooltipData)
    bonusesList = bonuses
    if merge:
        bonusesList = mergeNeededBonuses(bonuses, eventName)
    bonusesList = processCompensationsWithLootbox(bonusesList, eventName, showLootboxCompensation)
    bonusesCount = 0
    for bonus in bonusesList:
        if bonus.isShowInGUI():
            bonusList = packer.pack(bonus)
            bonusTooltipList = []
            bonusContentIdList = []
            if bonusList and tooltipData is not None:
                bonusTooltipList = packer.getToolTip(bonus)
                bonusContentIdList = packer.getContentId(bonus)
            for bonusIndex, item in enumerate(bonusList):
                item.setIndex(bonusIndex)
                bonusModelsList.addViewModel(item)
                bonusesCount += _getBonusCount(item)
                if tooltipData is not None:
                    tooltipIdx = str(bonusIndexTotal)
                    item.setTooltipId(tooltipIdx)
                    if bonusTooltipList:
                        tooltipData[tooltipIdx] = bonusTooltipList[bonusIndex]
                    if bonusContentIdList:
                        item.setTooltipContentId(str(bonusContentIdList[bonusIndex]))
                    bonusIndexTotal += 1

    return bonusesCount


def mergeNeededBonusesParse error at or near `BUILD_LIST_0' instruction at offset 0


def processCompensationsWithLootbox(bonuses, eventName, showLootboxCompensation):
    if not showLootboxCompensation:
        return [bonus for bonus in bonuses if bonus.getName() != LOOTBOX_COMPENSATION_BONUS]
    else:
        finalBonuses = []
        boxCompensations = {}
        for bonus in bonuses:
            if bonus.getName() == LOOTBOX_COMPENSATION_BONUS:
                category = bonus.getCategory()
                boxCompensations.setdefault(category, 0)
                boxCompensations[category] += sum(b.getCount() for b in bonuses if b.getName() == LOOTBOX_COMPENSATION_BONUS and b.getCategory() == category)

        for bonus in bonuses:
            if bonus.getName() == _LOOTBOX_BONUS_NAME:
                box = bonus.getBox()
                category = box.getCategory() if box is not None else ''
                if category in boxCompensations:
                    categoryCompensation = boxCompensations[category]
                    if categoryCompensation:
                        boxCount = bonus.getCount()
                        newBoxCount = max(0, boxCount - categoryCompensation)
                        boxCompensations[category] = max(0, categoryCompensation - boxCount)
                        if newBoxCount:
                            tokenData = first(bonus.getTokens().itervalues())
                            if tokenData is not None:
                                finalBonuses.append(LootBoxTokensBonus({(tokenData.id): {'count': newBoxCount, 'expires': {'at': (tokenData.expires)}}}, bonus.isCompensation(), {}))
                        continue
            finalBonuses.append(bonus)

        return AwardsManager.sortBonuses(eventName, finalBonuses)


def splitBonusesToExtra(bonuses, eventName):
    extraBonuses = []
    regularBonuses = []
    for bonus in bonuses:
        if bonus.getName() in _EXTRA_BONUSES_NAMES:
            extraBonuses.append(bonus)
        else:
            regularBonuses.append(bonus)

    sortedBonuses = AwardsManager.sortBonuses(eventName, regularBonuses)
    hasRareOrEpic = any(AwardsManager.getRarity(eventName, bonus) in (BonusRarity.RARE, BonusRarity.EPIC) for bonus in sortedBonuses)
    splitIndex = _MAIN_REWARD_COUNT_RARE_OR_EPIC if hasRareOrEpic else _MAIN_REWARD_COUNT
    mainRewards = sortedBonuses[-splitIndex:]
    additionalRewards = AwardsManager.sortBonuses(eventName, sortedBonuses[:-splitIndex] + extraBonuses)
    return (
     mainRewards, additionalRewards)


def _getBonusCount(bonusModel):
    bonusName = bonusModel.getName()
    if bonusName in Currency.ALL or bonusName in (
     'vehicles', Currency.FREE_XP, PREMIUM_ENTITLEMENTS.PLUS, CurrencyBP.TALER.value):
        return 1
    count = bonusModel.getCount()
    if not count:
        return 1
    return int(count)


def _getVehicleUIData(vehicle):
    return {'vehicleName': (vehicle.shortUserName), 
       'vehicleType': (getIconResourceName(vehicle.type)), 
       'isElite': (vehicle.isElite), 
       'vehicleLvl': (int2roman(vehicle.level)), 
       'vehicleLvlNum': (vehicle.level)}


def getPreparedBonusModel(bonus, eventName):
    model = BonusModel()
    model.setName(bonus.getName())
    model.setIsCompensation(bonus.isCompensation())
    model.setRarity(AwardsManager.getRarity(eventName, bonus) or BonusRarity.COMMON)
    return model


def _injectSpecialRewardName(item, postfix=''):
    if item.getRarity() in (BonusRarity.RARE, BonusRarity.EPIC):
        item.setSpecialAwardName(('_').join([item.getName(), postfix]) if postfix else item.getName())
    return


class LootBoxSimpleBonusUIPacker(SimpleBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBonus(cls, bonus, label):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setValue(str(bonus.getValue()))
        model.setIcon(bonus.getName())
        model.setLabel(label)
        return model

    @classmethod
    def _getToolTip(cls, bonus):
        if bonus.getName() == Currency.GOLD and bonus.isCompensation():
            return [
             createTooltipData(makeTooltip(header=backport.text(R.strings.tooltips.awardItem.gold.header()), body=backport.text(R.strings.tooltips.awardItem.gold.body()), note=backport.text(R.strings.tooltips.awardItem.gold.compensation())))]
        return super(LootBoxSimpleBonusUIPacker, cls)._getToolTip(bonus)


class LootBoxSpecialRandomBonusUIPacker(SimpleBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _pack(cls, bonus):
        label = backport.text(R.strings.tooltips.awardItem.dyn(bonus.getName()).header())
        return [cls._packSingleBonus(bonus, label if label else '')]

    @classmethod
    def _packSingleBonus(cls, bonus, label):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setCount(bonus.getCount())
        model.setIcon(bonus.getIconName())
        model.setLabel(label)
        return model

    @classmethod
    def _getContentId(cls, bonus):
        return [
         R.views.mono.lootbox.tooltips.random_national_bonus()]

    @classmethod
    def _getToolTip(cls, bonus):
        return [
         TooltipData(tooltip=None, isSpecial=True, specialAlias=None, specialArgs=[
          bonus.getName(), bonus.getValue(), bonus.getIconName()])]


class LootBoxSlotsBonusUIPacker(SimpleBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBonus(cls, bonus, label):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setCount(bonus.getCount())
        model.setIcon(bonus.getName())
        model.setLabel(backport.text(R.strings.tooltips.awardItem.slots.header()))
        return model


class LootBoxTmanTemplateBonusUIPacker(SimpleBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _pack(cls, bonus):
        result = []
        for tokenID, tokenRecord in bonus.getTokens().iteritems():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                count = tokenRecord.count
                packed = cls.__packTmanTemplateToken(tokenID, bonus, count)
                if packed is None:
                    _logger.error('Received wrong tman_template token from server: %s', tokenID)
                else:
                    result.append(packed)

        return result

    @classmethod
    def __packTmanTemplateToken(cls, tokenID, bonus, count):
        recruit = getRecruitInfo(tokenID)
        if recruit is None:
            return
        else:
            model = getPreparedBonusModel(bonus, cls.__eventName)
            model.setCount(count)
            model.setIcon(cls.__getBonusImageName(recruit))
            model.setLabel(recruit.getFullUserName())
            model.setValue(recruit.getGroupName())
            groupName = recruit.getGroupName()
            model.setValue('' if groupName in ('men1', 'women1') else groupName)
            _injectSpecialRewardName(model, recruit.getGroupName())
            return model

    @classmethod
    def __getBonusImageName(cls, recruitInfo):
        baseName = ('tank{}man').format('wo' if recruitInfo.isFemale() else '')
        return baseName

    @classmethod
    def _getToolTip(cls, bonus):
        tooltipData = []
        for tokenID in bonus.getTokens().iterkeys():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.TANKMAN_NOT_RECRUITED, specialArgs=[
                 tokenID]))

        return tooltipData

    @classmethod
    def _getContentId(cls, bonus):
        result = []
        for tokenID in bonus.getTokens().iterkeys():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                result.append(BACKPORT_TOOLTIP_CONTENT_ID)

        return result


class LootBoxCustomizationsBonusUIPacker(BaseBonusUIPacker):
    __eventName = ''
    __itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _pack(cls, bonus):
        result = []
        for item, data in zip(bonus.getCustomizations(), bonus.getList()):
            if item is None or cls.__isLockedStyle(bonus, item):
                continue
            result.append(cls._packSingleBonus(bonus, item, data))

        return result

    @classmethod
    def _packSingleBonus(cls, bonus, item, data):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        custItem = bonus.getC11nItem(item)
        itemName = custItem.itemTypeName
        description = custItem.userType
        if itemName == GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.ATTACHMENT]:
            model.setName(itemName)
            model.setIcon(custItem.name)
            model.setOverlayType(custItem.rarity)
        elif itemName == GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.STYLE]:
            description = backport.text(R.strings.lootbox_system.bonuses.description.style())
            vehicleCD = getSingleVehicleForCustomization(custItem)
            model.setIsInHangar(vehicleCD is not None and custItem.fullCount() > 0)
            if custItem.is3D:
                itemName = 'style_3d'
                description = backport.text(R.strings.lootbox_system.bonuses.description.style3D())
                vehicle = cls.__itemsCache.items.getItemByCD(vehicleCD) if vehicleCD is not None else None
                if vehicle is not None:
                    model.setIsElite(vehicle.isElite)
                    model.setLevel(vehicle.level)
                    model.setType(VehicleType(vehicle.type))
                    model.setVehicle3DStyleName(vehicle.userName)
        model.setIcon(itemName)
        model.setId(custItem.id)
        model.setCount(item.get('value', 0))
        model.setLabel(cls._getLabel(custItem))
        model.setDescription(description)
        _injectSpecialRewardName(model, str(custItem.id))
        return model

    @classmethod
    def _getToolTip(cls, bonus):
        tooltipData = []
        for item, _ in zip(bonus.getCustomizations(), bonus.getList()):
            if item is None:
                continue
            itemCustomization = bonus.getC11nItem(item)
            specialAlias = TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_AWARD
            specialArgs = CustomizationTooltipContext(itemCD=itemCustomization.intCD)
            if itemCustomization.itemTypeName in ('camouflage', 'style'):
                vehicle = getSingleVehicleForCustomization(itemCustomization)
                if vehicle is not None:
                    specialAlias = TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM
                    specialArgs = CustomizationTooltipContext(itemCD=itemCustomization.intCD, vehicleIntCD=vehicle)
            tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=specialAlias, specialArgs=specialArgs))

        return tooltipData

    @classmethod
    def _getContentId(cls, bonus):
        result = []
        for item, _ in zip(bonus.getCustomizations(), bonus.getList()):
            if item is not None:
                result.append(BACKPORT_TOOLTIP_CONTENT_ID)

        return result

    @classmethod
    def _getLabel(cls, customizationItem):
        return customizationItem.userName

    @classmethod
    def __isLockedStyle(cls, bonus, item):
        customizationItem = bonus.getC11nItem(item)
        return customizationItem.itemTypeName == 'style' and customizationItem.isLockedOnVehicle


class LootBoxGoodiesBonusUIPacker(GoodiesBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBoosterBonus(cls, bonus, booster, count):
        return cls._packIconBonusModel(bonus, booster.getFullNameForResource(), count, backport.text(R.strings.menu.booster.label.dyn(booster.boosterGuiType)(), effectValue=booster.getFormattedValue()), description=backport.text(R.strings.lootbox_system.bonuses.description.booster()))

    @classmethod
    def _packIconBonusModel(cls, bonus, icon, count, label, description=''):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setCount(count)
        model.setIcon(icon)
        model.setLabel(label)
        model.setDescription(description)
        return model

    @classmethod
    def _getToolTip(cls, bonus):
        tooltipData = []
        for booster, _ in sorted(bonus.getBoosters().iteritems(), key=(lambda b: b[0].boosterID)):
            tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=None, specialArgs=[
             booster.boosterID]))

        for demountkit in sorted(bonus.getDemountKits().iterkeys()):
            tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.AWARD_DEMOUNT_KIT, specialArgs=[
             demountkit.intCD]))

        for form in sorted(bonus.getRecertificationForms().iterkeys()):
            tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.EPIC_BATTLE_RECERTIFICATION_FORM_TOOLTIP, specialArgs=[
             form.intCD]))

        for item in sorted(bonus.getMentoringLicenses().iterkeys()):
            tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=None, specialArgs=[
             item.inventoryCount]))

        return tooltipData

    @classmethod
    def _getContentId(cls, bonus):
        tooltipData = []
        for _ in sorted(bonus.getBoosters().iterkeys(), key=(lambda b: b.boosterID)):
            tooltipData.append(R.views.lobby.personal_reserves.QuestBoosterTooltip())

        for _ in sorted(bonus.getDemountKits().iterkeys()):
            tooltipData.append(BACKPORT_TOOLTIP_CONTENT_ID)

        for _ in sorted(bonus.getRecertificationForms().iterkeys()):
            tooltipData.append(BACKPORT_TOOLTIP_CONTENT_ID)

        for _ in sorted(bonus.getMentoringLicenses().iterkeys()):
            tooltipData.append(R.views.lobby.crew.tooltips.MentoringLicenseTooltip())

        return tooltipData


class LootBoxBlueprintBonusUIPacker(BlueprintBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _pack(cls, bonus):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        label = bonus.getBlueprintTooltipName()
        blueprintName = bonus.getBlueprintName()
        if blueprintName == BlueprintsBonusSubtypes.NATION_FRAGMENT:
            label = backport.text(R.strings.lootbox_system.bonuses.label.blueprints.nationalFragment(), nation=backport.text(R.strings.blueprints.nations.dyn(bonus.getImageCategory())()))
        elif blueprintName == BlueprintsBonusSubtypes.UNIVERSAL_FRAGMENT:
            label = backport.text(R.strings.lootbox_system.bonuses.label.blueprints.universalFragment())
        model.setIcon(bonus.getImageCategory())
        model.setLabel(label)
        model.setCount(bonus.getCount())
        return [model]

    @staticmethod
    def getTooltip(bonuses):
        fragmentCDs = [bonus.getBlueprintSpecialArgs() for bonus in bonuses]
        specialAlias = [bonus.getBlueprintSpecialAlias() for bonus in bonuses]
        return TooltipData(tooltip=None, isSpecial=True, specialAlias=specialAlias, specialArgs=[
         fragmentCDs])


class LootBoxItemBonusUIPacker(ItemBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBonus(cls, bonus, item, count):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setCount(count)
        icon, overlay = (item.name, '') if item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER else (
         item.getGUIEmblemID(), item.getOverlayType())
        model.setIcon(icon)
        model.setOverlayType(overlay)
        model.setLabel(item.userName)
        if item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER:
            model.setDescription(backport.text(R.strings.lootbox_system.bonuses.description.battle_booster()))
        elif item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE and item.isRegular:
            model.setDescription(backport.text(R.strings.lootbox_system.bonuses.description.standard_equipment()))
        return model


class LootBoxCrewBookBonusUIPacker(CrewBookBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBonus(cls, bonus, book, count):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setCount(count)
        model.setLabel(book.userName)
        model.setIcon(book.getBonusIconName())
        return model


class LootBoxCrewSkinBonusUIPacker(CrewSkinBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBonus(cls, bonus, crewSkin, count, label):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setCount(count)
        model.setIcon(str(crewSkin.itemTypeName + str(crewSkin.getRarity())))
        model.setLabel(label)
        model.setDescription(backport.text(R.strings.lootbox_system.bonuses.description.crewSkin()))
        return model


class LootBoxesLootBoxBonusUIPacker(SimpleBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _pack(cls, bonus):
        return [
         cls._packSingleBonus(bonus)]

    @classmethod
    def _packSingleBonus(cls, bonus):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        box = bonus.getBox()
        model.setId(bonus.lootBoxID)
        model.setIcon(box.getCategory() if box else bonus.getName())
        model.setCount(bonus.getCount())
        model.setLabel(box.getUserName() if box else '')
        _injectSpecialRewardName(model, str(bonus.lootBoxID))
        return model

    @classmethod
    def _getContentId(cls, _):
        return [R.views.mono.lootbox.tooltips.box_tooltip()]


class LootBoxTokenBonusUIPacker(TokenBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        return bonusPacker(model, bonus, *args)

    @classmethod
    def _getTokenBonusPackers(cls):
        return {BATTLE_BONUS_X5_TOKEN: (cls.__packBattleBonusX5Token), 
           CREW_BONUS_X3_TOKEN: (cls.__packCrewBonusX3Token)}

    @classmethod
    def _getTooltipsPackers(cls):
        packers = super(LootBoxTokenBonusUIPacker, cls)._getTooltipsPackers()
        return {BATTLE_BONUS_X5_TOKEN: (packers[BATTLE_BONUS_X5_TOKEN]), 
           CREW_BONUS_X3_TOKEN: (packers[CREW_BONUS_X3_TOKEN])}

    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        model.setCount(bonus.getCount())
        model.setLabel(backport.text(R.strings.tooltips.quests.bonuses.token.battle_bonus_x5.label()))
        model.setIcon(BATTLE_BONUS_X5_TOKEN)
        return model

    @classmethod
    def __packCrewBonusX3Token(cls, model, bonus, *args):
        model.setCount(bonus.getCount())
        model.setLabel(backport.text(R.strings.tooltips.quests.bonuses.token.crew_bonus_x3.label()))
        model.setIcon(CREW_BONUS_X3_TOKEN)
        return model


class LootBoxPremiumBonusUIPacker(BaseBonusUIPacker):
    __eventName = ''
    _ICONS_AVAILABLE = (1, 2, 3, 7, 14, 30, 90, 180, 360)

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _pack(cls, bonus):
        return [
         cls._packSingleBonus(bonus)]

    @classmethod
    def _packSingleBonus(cls, bonus):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        icon = 'premium_plus_universal'
        days = bonus.getValue()
        if days in cls._ICONS_AVAILABLE:
            icon = ('{}_{}').format(bonus.getName(), str(days))
        model.setName(bonus.getName())
        model.setIcon(icon)
        model.setIsCompensation(bonus.isCompensation())
        model.setValue(str(days))
        model.setLabel(backport.text(R.strings.tooltips.awardItem.premium_plus.header()))
        return model


class LootBoxVehiclesBonusUIPacker(VehiclesBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packVehicles(cls, bonus, vehicles):
        return [cls._packVehicle(bonus, vehInfo, vehicle) for vehicle, vehInfo in vehicles]

    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        styleID = vehInfo.get('customization', {}).get('styleId')
        if styleID is not None and vehicle.isOutfitLocked:
            model.setStyleID(styleID)
        model.setName(bonus.getName())
        model.setIsRent(isRent)
        compensation = cls.__getCompensation(bonus, vehInfo)
        model.setIsCompensation(bool(compensation))
        if compensation:
            for bonusComp in compensation:
                model.compensation.setName(bonusComp.getName())
                model.compensation.setValue(str(bonusComp.getValue()))
                model.compensation.setIcon(bonusComp.getName())
                model.compensation.setLabel(getLocalizedBonusName(bonusComp.getName()))

        cls.__fillVehicleInfo(model, vehicle)
        _injectSpecialRewardName(model, str(vehicle.intCD))
        return model

    @classmethod
    def __fillVehicleInfo(cls, model, vehicle):
        model.setIsInHangar(vehicle.isInInventory)
        model.setId(vehicle.intCD)
        model.setLabel(vehicle.userName)
        model.setVehicleShortName(vehicle.shortUserName)
        model.setType(VehicleType(vehicle.type))
        model.setLevel(vehicle.level)
        model.setIsElite(vehicle.isElite)
        model.setIsWheeled(vehicle.isWheeledTech)
        model.setIcon(getUnicName(vehicle.name))
        return

    @classmethod
    def _packTooltips(cls, bonus, vehicles):
        packedTooltips = []
        for vehicle, vehInfo in vehicles:
            compensation = cls.__getCompensation(bonus, vehInfo)
            if compensation:
                for bonusComp in compensation:
                    packedTooltips.extend(cls._packCompensationTooltip(bonusComp, vehicle))

            else:
                packedTooltips.append(cls._packTooltip(bonus, vehicle, vehInfo))

        return packedTooltips

    @classmethod
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        compensation = cls.__getCompensation(bonus, vehInfo)
        if compensation:
            return first(cls._packCompensationTooltip(first(compensation), vehicle))
        return super(LootBoxVehiclesBonusUIPacker, cls)._packTooltip(bonus, vehicle, vehInfo)

    @classmethod
    def _packCompensationTooltip(cls, bonusComp, vehicle):
        tooltipDataList = super(LootBoxVehiclesBonusUIPacker, cls)._packCompensationTooltip(bonusComp, vehicle)
        return [cls.__convertCompensationTooltip(bonusComp, vehicle, tooltipData) for tooltipData in tooltipDataList]

    @classmethod
    def _getContentId(cls, bonus):
        outcome = []
        for _, vehInfo in bonus.getVehicles():
            compensation = cls.__getCompensation(bonus, vehInfo)
            if compensation:
                outcome.append(VEH_COMP_R_ID)
            else:
                outcome.append(BACKPORT_TOOLTIP_CONTENT_ID)

        return outcome

    @classmethod
    def __convertCompensationTooltip(cls, bonusComp, vehicle, tooltipData):
        iconAfterRes = R.images.gui.maps.icons.quests.bonuses.big.dyn(bonusComp.getName())
        if not iconAfterRes.exists():
            iconAfterRes = R.images.gui.maps.icons.quests.bonuses.big.gold
        specialArgs = {'labelBefore': '', 
           'iconAfter': (backport.image(iconAfterRes())), 
           'labelAfter': (bonusComp.getIconLabel()), 
           'bonusName': (bonusComp.getName())}
        uiData = _getVehicleUIData(vehicle)
        formattedTypeName = uiData['vehicleType']
        isElite = vehicle.isElite
        uiData['vehicleType'] = ('{}_elite').format(formattedTypeName) if isElite else formattedTypeName
        specialArgs.update(uiData)
        vehicleName = getNationLessName(vehicle.name)
        vehIcon = R.images.gui.maps.shop.vehicles.c_180x135.dyn(vehicleName)()
        if vehIcon < 1:
            vehicleName = vehicleName.replace('-', '_')
            vehIcon = R.images.gui.maps.shop.vehicles.c_180x135.dyn(vehicleName)()
        specialArgs['iconBefore'] = backport.image(vehIcon) if vehIcon > 0 else ''
        return createTooltipData(tooltip=tooltipData.tooltip, specialAlias=VEH_COMP_R_ID, specialArgs=specialArgs)

    @classmethod
    def __getCompensation(cls, bonus, vehInfo):
        compBonuses = []
        compensatedNumber = vehInfo.get('compensatedNumber', 0)
        compensation = vehInfo.get('customCompensation')
        if compensatedNumber and compensation is not None:
            money = Money(*compensation)
            for currency, value in money.iteritems():
                if value:
                    bonusClass = _BONUSES.get(currency)
                    compBonuses.append(bonusClass(currency, value, isCompensation=True, compensationReason=bonus))

        return compBonuses


class LootBoxCurrenciesBonusUIPacker(CurrenciesBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBonus(cls, bonus, label):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setName(bonus.getCode())
        model.setValue(str(bonus.getValue()))
        model.setIcon(bonus.getCode())
        model.setLabel(label)
        return model

    @classmethod
    def _getContentId(cls, bonus):
        if bonus.getCode() == CurrencyBP.TALER.value:
            return [R.views.mono.battle_pass.tooltips.bptaler()]
        return super(LootBoxCurrenciesBonusUIPacker, cls)._getContentId(bonus)


class LootBoxBPCoinBonusUIPacker(SimpleBonusUIPacker):
    __eventName = ''

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _packSingleBonus(cls, bonus, label):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setValue(str(bonus.getValue()))
        model.setIcon(bonus.getName())
        model.setLabel(backport.text(R.strings.lootbox_system.bonuses.label.bpcoin()))
        return model

    @classmethod
    def _getContentId(cls, bonus):
        return [R.views.mono.battle_pass.tooltips.bpcoin()]


class LootBoxCompensationPacker(SimpleBonusUIPacker):
    __eventName = ''
    __VEHICLE_BONUS_NAME = 'vehicles'

    @classmethod
    def init(cls, eventName):
        cls.__eventName = eventName
        return

    @classmethod
    def _pack(cls, bonus):
        return [
         cls._packSingleBonus(bonus, label='')]

    @classmethod
    def _packSingleBonus(cls, bonus, label):
        model = getPreparedBonusModel(bonus, cls.__eventName)
        model.setIcon(cls.__VEHICLE_BONUS_NAME)
        model.setLabel('')
        model.compensation.setName(_LOOTBOX_BONUS_NAME)
        box = bonus.getBox()
        model.compensation.setIcon(box.getCategory() if box is not None else '')
        model.compensation.setLabel(box.getUserName() if box is not None else '')
        return model

    @classmethod
    def _getContentId(cls, bonus):
        return [R.views.mono.lootbox.tooltips.box_compensation()]

    @classmethod
    def _getToolTip(cls, bonus):
        return [
         TooltipData(tooltip=None, isSpecial=True, specialAlias=None, specialArgs=[
          bonus.getCategory(), cls.__eventName])]


return
# wot-extractor: AVISO - descompilacao partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 124)
