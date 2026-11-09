# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/modes/assets_pack.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/configs/modes/assets_pack.py
from __future__ import absolute_import
import typing
from dict2model import fields, models, schemas
from gui.impl.gen import R

class FunModeAssetsPackConfigurationModel(models.Model):
    __slots__ = ('assetsPointer', 'hangarEventBanner', 'progressionView')

    def __init__(self, assetsPointer, hangarEventBanner, progressionView):
        super(FunModeAssetsPackConfigurationModel, self).__init__()
        self.assetsPointer = assetsPointer
        self.hangarEventBanner = hangarEventBanner
        self.progressionView = progressionView

    def getIconsResRoot(self):
        return R.images.fun_random.gui.maps.icons.feature.asset_packs.modes.dyn(self.assetsPointer, R.images.fun_random.gui.maps.icons.feature.asset_packs.modes.undefined)

    def getLocalsResRoot(self):
        return R.strings.fun_random.modes.dyn(self.assetsPointer, R.strings.fun_random.modes.undefined)


class FunHangarEventBannerConfigModel(models.Model):
    __slots__ = ('borderColor', )

    def __init__(self, borderColor):
        super(FunHangarEventBannerConfigModel, self).__init__()
        self.borderColor = borderColor


class FunProgressionViewConfigModel(models.Model):
    __slots__ = ('pointsTitleFontColors', 'pointsValueFontColor', 'stagesFontColors',
                 'rewardCounterFontColor')

    def __init__(self, pointsTitleFontColors, pointsValueFontColor, stagesFontColors, rewardCounterFontColor):
        super(FunProgressionViewConfigModel, self).__init__()
        self.pointsTitleFontColors = pointsTitleFontColors
        self.pointsValueFontColor = pointsValueFontColor
        self.stagesFontColors = stagesFontColors
        self.rewardCounterFontColor = rewardCounterFontColor


funHangarEventBannerConfigurationSchema = schemas.Schema[FunHangarEventBannerConfigModel](fields={'borderColor': (fields.HexColorCode(required=True))}, modelClass=FunHangarEventBannerConfigModel)
funProgressionViewConfigurationSchema = schemas.Schema[FunProgressionViewConfigModel](fields={'pointsTitleFontColors': (fields.Dict(keyFieldOrSchema=fields.String(required=True), valueFieldOrSchema=fields.HexColorCode(required=True), required=True)), 
   'pointsValueFontColor': (fields.HexColorCode(required=True)), 
   'stagesFontColors': (fields.Dict(keyFieldOrSchema=fields.String(required=True), valueFieldOrSchema=fields.HexColorCode(required=True), required=True)), 
   'rewardCounterFontColor': (fields.HexColorCode(required=True))}, modelClass=FunProgressionViewConfigModel)
funModeAssetsPackConfigurationSchema = schemas.Schema[FunModeAssetsPackConfigurationModel](fields={'assetsPointer': (fields.String(required=True)), 
   'hangarEventBanner': (fields.Nested(schema=funHangarEventBannerConfigurationSchema, required=True)), 
   'progressionView': (fields.Nested(schema=funProgressionViewConfigurationSchema, required=True))}, modelClass=FunModeAssetsPackConfigurationModel)
