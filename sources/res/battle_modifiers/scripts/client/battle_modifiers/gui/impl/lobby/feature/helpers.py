# wot-extractor: codigo DESCOMPILADO de sources/res/battle_modifiers/scripts/client/battle_modifiers/gui/impl/lobby/feature/helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_modifiers/scripts/client/battle_modifiers/gui/impl/lobby/feature/helpers.py
from __future__ import absolute_import
from typing import TYPE_CHECKING, Optional
from battle_modifiers.gui.impl.lobby.feature.constants import MOD_TYPE_MAP, PHYS_TYPE_MAP, USE_TYPE_MAP, GAMEPLAY_IMPACT_MAP
from battle_modifiers.gui.impl.gen.view_models.views.lobby.feature.modifier_model import ModifierModel
from battle_modifiers.gui.impl.gen.view_models.views.lobby.feature.limit_model import LimitModel, LimitType
if TYPE_CHECKING:
    from battle_modifiers_ext.battle_modifiers import ModifierBase
    from frameworks.wulf import Array

def packModifierModel(modifier):
    result = ModifierModel()
    result.setValue(modifier.value)
    result.setUseType(USE_TYPE_MAP[modifier.useType])
    result.setModificationType(MOD_TYPE_MAP[modifier.param.id])
    result.setResName(modifier.param.clientData.resName)
    result.setPhysicalType(PHYS_TYPE_MAP[modifier.param.clientData.physicalType])
    result.setGameplayImpact(GAMEPLAY_IMPACT_MAP[modifier.gameplayImpact])
    _invalidateLimits(modifier, result.getLimits())
    return result


def _invalidateLimits(modifier, limitsModel):
    limitsModel.clear()
    models = [
     _packLimitModel(modifier.minValue, LimitType.MIN),
     _packLimitModel(modifier.maxValue, LimitType.MAX)]
    models = [model for model in models if model is not None]
    for model in models:
        limitsModel.addViewModel(model)

    limitsModel.invalidate()
    return


def _packLimitModel(value, limitType):
    if value is None:
        return
    else:
        model = LimitModel()
        model.setLimitType(limitType)
        model.setValue(value)
        return model
