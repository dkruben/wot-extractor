# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/dialogs/sub_views/icon/multiple_icons_set.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/sub_views/icon/multiple_icons_set.py
from __future__ import absolute_import
import typing
from gui.impl.gen import R
from gui.impl.dialogs.sub_views.common import IconSetData
from gui.impl.gen.view_models.views.dialogs.sub_views.multiple_icons_set_view_model import MultipleIconsSetViewModel, IconPositionLogicEnum
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.image_substitution_view_model import ImageSubstitutionViewModel
from gui.impl.pub import ViewImpl
from frameworks.wulf import ViewSettings
if typing.TYPE_CHECKING:
    from typing import List, Optional, Any
    from frameworks.wulf import Array
    TYPE_ICONS = Optional[List[IconSetData]]
    TYPE_RESOURCES = Optional[List[int]]

def _populateImageSubstitutionModel(substitution):
    imageSubstitutionVM = ImageSubstitutionViewModel()
    imageSubstitutionVM.setPath(substitution.resourceID)
    imageSubstitutionVM.setPlaceholder(substitution.placeholder)
    imageSubstitutionVM.setMarginTop(substitution.marginTop)
    imageSubstitutionVM.setMarginRight(substitution.marginRight)
    imageSubstitutionVM.setMarginBottom(substitution.marginBottom)
    imageSubstitutionVM.setMarginLeft(substitution.marginLeft)
    return imageSubstitutionVM


def _addIconResIdsToViewModelArray(source, target):
    if not source:
        return
    for iconData in source:
        if iconData.iconRes == R.invalid():
            continue
        iconVM = IconViewModel()
        iconVM.setPath(iconData.iconRes)
        if iconData.label:
            iconVM.iconLabel.setText(iconData.label)
            if iconData.imageSubstitutions:
                substitutionList = iconVM.iconLabel.getImageSubstitutions()
                for subs in iconData.imageSubstitutions:
                    substitutionList.addViewModel(_populateImageSubstitutionModel(subs))

        target.addViewModel(iconVM)


def _addLayersResIdsToViewModelArray(source, target):
    if not source:
        return
    for resID in source:
        if resID == R.invalid():
            continue
        iconVM = IconViewModel()
        iconVM.setPath(resID)
        target.addViewModel(iconVM)


class MultipleIconsSet(ViewImpl):
    __slots__ = ()

    def __init__(self, iconResIDList=None, backgroundResIDList=None, overlayResIDList=None, layoutID=None, iconPositionLogic=IconPositionLogicEnum.CENTREDANDTHROUGHCONTENT.value):
        settings = ViewSettings(layoutID or R.views.dialogs.sub_views.icon.MultipleIconsSet())
        settings.model = MultipleIconsSetViewModel()
        settings.kwargs = {'iconResIDList': iconResIDList, 
           'backgroundResIDList': backgroundResIDList, 
           'overlayResIDList': overlayResIDList, 
           'iconPositionLogic': iconPositionLogic}
        super(MultipleIconsSet, self).__init__(settings)

    def _onLoading(self, iconResIDList, backgroundResIDList, overlayResIDList, iconPositionLogic, *args, **kwargs):
        super(MultipleIconsSet, self)._onLoading(*args, **kwargs)
        viewModel = self.getViewModel()
        viewModel.setIconPositionLogic(iconPositionLogic)
        _addIconResIdsToViewModelArray(iconResIDList, viewModel.getIcons())
        _addLayersResIdsToViewModelArray(backgroundResIDList, viewModel.getBackgrounds())
        _addLayersResIdsToViewModelArray(overlayResIDList, viewModel.getOverlays())
