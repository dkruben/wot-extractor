# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/shared/tooltips/helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/shared/tooltips/helper.py
from __future__ import absolute_import
from future.utils import lmap
from functools import partial
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.reward_points_place_model import RewardPointsPlaceModel
from frameworks.wulf import Array
from frameworks.wulf.view.array import fillViewModelsArray, fillStringsArray
from gui.impl import backport
from gui.impl.gen import R
_string = R.strings.battle_royale.tooltip.progression.leaderboardReward

def fillProgressionPointsTableModel(viewModel, progressionPointsList, headerResource=_string):
    gameModes, gameModeLists = progressionPointsList
    fillStringsArray(lmap(partial(_getGameModeName, headerResource), gameModes), viewModel.getBattleTypes())
    gameModeColLists = []
    for points in gameModeLists:
        prevLevel = 1
        gameModeCellList = []
        for point in points:
            gameModeCellList.append(_getRowPointsCell(point, prevLevel, headerResource))
            prevLevel = point.lastInRange + 1

        gameModeColLists.append(gameModeCellList)

    battleModesArray = viewModel.getBattleModes()
    battleModesArray.clear()
    for colList in gameModeColLists:
        array = Array()
        fillViewModelsArray(colList, array)
        battleModesArray.addArray(array)

    battleModesArray.invalidate()


def _getGameModeName(headerResource, gameMode):
    return backport.text(headerResource.battleTypesHeader.num(gameMode)())


def _setRangeLabel(points, prevLevel, headerResource):
    numRange = (
     prevLevel, points.lastInRange)
    rangeTemplate = headerResource.text.places()
    if prevLevel == points.lastInRange:
        numRange = (
         points.lastInRange,)
        rangeTemplate = headerResource.text.place()
    return backport.text(rangeTemplate, place=('-').join(map(str, numRange)))


def _getRowPointsCell(points, prevLevel, headerResource):
    cell = RewardPointsPlaceModel()
    cell.setPlace(_setRangeLabel(points, prevLevel, headerResource))
    cell.setPoints(points.points)
    return cell
