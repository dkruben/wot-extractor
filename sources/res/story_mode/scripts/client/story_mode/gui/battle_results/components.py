# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/battle_results/components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/battle_results/components.py
from __future__ import absolute_import
from future.utils import viewitems
from gui.battle_results.components import base
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import getUserName
from helpers import dependency
from items import vehicles
from skeletons.gui.game_control import IBattlePassController
from story_mode.skeletons.story_mode_controller import IStoryModeController
from story_mode_common.configs.story_mode_missions import missionsSchema
from story_mode.gui.shared.utils import getRewardList

class FinishResultItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return reusable.getPersonalTeamResult()


class FinishReasonItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        finishReason = reusable.common.finishReason
        rReason = R.strings.sm_battle.finish.reason
        return rReason.num(finishReason, rReason.default)()


class MissionIdItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return value['avatar']['missionId']


class IsForceOnboardingItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return value['avatar']['isForceOnboarding']


class VehicleNameItem(base.StatsItem):
    __slots__ = ()
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def _convert(self, value, reusable):
        mission = self._storyModeCtrl.missions.getMission(value['avatar']['missionId'])
        if mission is None:
            return ''
        else:
            return getUserName(vehicles.makeVehicleTypeByName(mission.vehicle.name))


class VehicleBlock(base.StatsBlock):

    def setRecord(self, result, reusable):
        vehicleInfo = reusable.getPersonalVehiclesInfo(result['personal'])
        self.addNextComponent(base.DirectStatsItem('deathReason', vehicleInfo.deathReason))
        self.addNextComponent(base.DirectStatsItem('damageDealt', vehicleInfo.damageDealt))
        self.addNextComponent(base.DirectStatsItem('kills', vehicleInfo.kills))
        self.addNextComponent(base.DirectStatsItem('damageAssisted', vehicleInfo.damageAssisted + vehicleInfo.equipmentDamageAssisted))
        self.addNextComponent(base.DirectStatsItem('damageBlockedByArmor', vehicleInfo.damageBlockedByArmor))


class RewardsBlock(base.StatsBlock):
    __slots__ = ()
    _battlePass = dependency.descriptor(IBattlePassController)

    def setRecord(self, result, reusable):
        progressInfo = result['personal']['avatar'].get('progressionInfo', {})
        missionSettings = missionsSchema.getModel()
        if missionSettings is None:
            return
        else:
            rewardsList = getRewardList(progressInfo, self._battlePass.isActive(), True)
            bonuses = []
            for rewardRecord in rewardsList:
                for rewardName, rewardData in viewitems(rewardRecord):
                    for item in getNonQuestBonuses(rewardName, rewardData):
                        bonuses.append(item)

            for item in mergeBonuses(bonuses):
                self.addNextComponent(base.DirectStatsItem('', item))

            return


class ProgressionInfoItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, value, reusable):
        return value['avatar'].get('progressionInfo', {})
