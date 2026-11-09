# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/battle/shared/premature_leave.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/battle/shared/premature_leave.py
from __future__ import absolute_import
from BWUtil import AsyncReturn
from gui.impl.gen import R
from gui.impl.pub.dialog_window import DialogButtons
from wg_async import wg_await, wg_async
_DIMMER_ALPHA = 0.7

@wg_async
def showComp7LightLeaverAliveWindow():
    from gui.impl.dialogs import dialogs
    from gui.impl.dialogs.gf_builders import ConfirmCancelDescriptionDialogBuilder
    builder = ConfirmCancelDescriptionDialogBuilder()
    builder.setBlur(False)
    builder.setDimmerAlpha(_DIMMER_ALPHA)
    builder.setTitle(R.strings.dialogs.comp7_light.deserter.title())
    builder.setCancelButtonLabel(R.strings.dialogs.comp7_light.deserter.cancel())
    builder.setConfirmButtonLabel(R.strings.dialogs.comp7_light.deserter.submit())
    builder.setFocusedButtonID(DialogButtons.CANCEL)
    builder.setDescriptionMsg(R.strings.dialogs.comp7_light.deserter.message())
    builder.setIcon(R.images.comp7_core.gui.maps.icons.battle.comp7DeserterLeaveBattle())
    result = yield wg_await(dialogs.show(builder.build()))
    raise AsyncReturn(result.result == DialogButtons.SUBMIT)
