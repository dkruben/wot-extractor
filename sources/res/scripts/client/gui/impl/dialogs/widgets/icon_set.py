# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/dialogs/widgets/icon_set.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/widgets/icon_set.py
from __future__ import absolute_import
import typing
from gui.impl.dialogs.sub_views.common import IconSetData
from gui.impl.dialogs.sub_views.icon.multiple_icons_set import MultipleIconsSet
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.multiple_icons_set_view_model import IconPositionLogicEnum
if typing.TYPE_CHECKING:
    from typing import List, Optional
    from frameworks.wulf import Array

def _addIconResIdsToViewModelArray(source, target):
    if source:
        for resID in source:
            if resID != R.invalid():
                iconVM = IconViewModel()
                iconVM.setPath(resID)
                target.addViewModel(iconVM)


class IconSet(MultipleIconsSet):
    __slots__ = ()

    def __init__(self, iconResID, backgroundResIDList=None, overlayResIDList=None, layoutID=None, iconPositionLogic=IconPositionLogicEnum.CENTREDANDTHROUGHCONTENT.value):
        iconsRes = [
         IconSetData(iconResID, None, None)]
        super(IconSet, self).__init__(iconsRes, backgroundResIDList, overlayResIDList, layoutID, iconPositionLogic)
        return
