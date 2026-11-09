# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_modes/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/sub_modes/__init__.py
from __future__ import absolute_import
import typing
from fun_random_common.fun_constants import FunSubModeImpl
from fun_random.gui.feature.sub_modes.base_sub_mode import FunBaseSubMode
from fun_random.gui.feature.sub_modes.dev_sub_mode import FunDevSubMode
from fun_random.gui.shared.fun_system_factory import registerFunRandomSubMode, collectFunRandomSubMode
if typing.TYPE_CHECKING:
    from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode
    from fun_random.helpers.server_settings import FunSubModeConfig

def registerFunRandomSubModes():
    registerFunRandomSubMode(FunSubModeImpl.DEV_TEST, FunDevSubMode)


def createFunSubMode(subModeSettings):
    return (collectFunRandomSubMode(subModeSettings.client.subModeImpl) or FunBaseSubMode)(subModeSettings)
