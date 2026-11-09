# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/__init__.py
from __future__ import absolute_import
from future.utils import itervalues
import BigWorld
from items import vehicles

def getWholeVehModels(vDesc):
    nationID, vehicleTypeID = vehicles.g_list.getIDsByName(vDesc.name)
    vType = vehicles.g_cache.vehicle(nationID, vehicleTypeID)
    prereqs = set(vDesc.prerequisites())
    models = set()
    bspModels = set()
    index = 0
    for chassie in vType.chassis:
        models.add(chassie.models.undamaged)
        splinePairs = chassie.splineDesc.trackPairs if chassie.splineDesc else {}
        for splinePairDesc in itervalues(splinePairs):
            if splinePairDesc is not None:
                models.add(splinePairDesc.segmentModelLeft())
                models.add(splinePairDesc.segmentModelRight())
                models.add(splinePairDesc.segment2ModelLeft())
                models.add(splinePairDesc.segment2ModelRight())

        bspModels.add((index, chassie.hitTester.bspModelName))
        index += 1

    for hull in vType.hulls:
        prereqs.add(hull.models.undamaged)
        bspModels.add((index, hull.hitTester.bspModelName))
        index += 1

    for turrets in vType.turrets:
        for turret in turrets:
            models.add(turret.models.undamaged)
            bspModels.add((index, turret.hitTester.bspModelName))
            index += 1
            for gun in turret.guns:
                models.add(gun.models.undamaged)
                bspModels.add((index, gun.hitTester.bspModelName))
                index += 1

    result = list(prereqs)
    for model in models:
        if not model:
            continue
        compoundAssembler = BigWorld.CompoundAssembler()
        compoundAssembler.addRootPart(model, 'root')
        compoundAssembler.name = model
        compoundAssembler.spaceID = BigWorld.player().spaceID
        result.append(compoundAssembler)

    result.append(BigWorld.CollisionAssembler(tuple(bspModels), BigWorld.player().spaceID))
    return result
