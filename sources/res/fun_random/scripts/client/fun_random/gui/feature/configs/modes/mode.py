# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/modes/mode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/configs/modes/mode.py
from __future__ import absolute_import
import typing
from dict2model import fields, models, schemas
from fun_random.gui.feature.configs.modes.assets_pack import funModeAssetsPackConfigurationSchema
if typing.TYPE_CHECKING:
    from fun_random.gui.feature.configs.modes.assets_pack import FunModeAssetsPackConfigurationModel

class FunModeConfigurationModel(models.Model):
    __slots__ = ('assetsPack', )

    def __init__(self, assetsPack):
        super(FunModeConfigurationModel, self).__init__()
        self.assetsPack = assetsPack


class FunModeCompositeConfigurationModel(models.Model):
    __slots__ = ('mode', )

    def __init__(self, mode):
        super(FunModeCompositeConfigurationModel, self).__init__()
        self.mode = mode


funModeConfigurationSchema = schemas.Schema[FunModeConfigurationModel](fields={'assetsPack': (fields.Nested(schema=funModeAssetsPackConfigurationSchema, required=True))}, modelClass=FunModeConfigurationModel)
funModeCompositeConfigurationSchema = schemas.Schema[FunModeCompositeConfigurationModel](fields={'mode': (fields.Nested(schema=funModeConfigurationSchema, required=True))}, modelClass=FunModeCompositeConfigurationModel)
