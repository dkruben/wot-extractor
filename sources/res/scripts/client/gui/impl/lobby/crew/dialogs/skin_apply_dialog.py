# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/skin_apply_dialog.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/dialogs/skin_apply_dialog.py
from base_crew_dialog_template_view import BaseCrewDialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton, ConfirmButton
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.lobby.crew.dialogs.skin_apply_dialog_model import SkinApplyDialogModel
from gui.impl.pub.dialog_window import DialogButtons
from gui.shared.gui_items.crew_skin import localizedFullName
from gui.shared.gui_items.processors.tankman import CrewSkinEquip
from gui.shared.utils import decorators
from helpers import dependency, i18n
from skeletons.gui.shared import IItemsCache

class SkinApplyDialog(BaseCrewDialogTemplateView):
    __slots__ = ('_crewSkinID', '_tankManInvID')
    LAYOUT_ID = R.views.lobby.crew.dialogs.SkinApplyDialog()
    VIEW_MODEL = SkinApplyDialogModel
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, crewSkinID, tankManInvID):
        super(SkinApplyDialog, self).__init__()
        self._crewSkinID = crewSkinID
        self._tankManInvID = tankManInvID

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        skinItem = self._itemsCache.items.getCrewSkin(self._crewSkinID)
        self.setBackgroundImagePath(R.images.gui.maps.icons.windows.background())
        self.setSubView(Placeholder.TITLE, SimpleTextTitle(localizedFullName(skinItem)))
        self.setSubView(Placeholder.ICON, IconSet(R.images.gui.maps.icons.tankmen.icons.big.crewSkins.dyn(skinItem.getIconID())(), None, [
         R.images.gui.maps.icons.tankmen.windows.lipSmall_dialogs()]))
        self.addButton(ConfirmButton(R.strings.dialogs.skinApplyDialog.button.submit()))
        self.addButton(CancelButton())
        self._updateViewModel()
        super(SkinApplyDialog, self)._onLoading(*args, **kwargs)
        return

    def _setResult(self, result):
        if result == DialogButtons.SUBMIT:
            self._equipCrewSkin()
        super(SkinApplyDialog, self)._setResult(result)

    @decorators.adisp_process('updating')
    def _equipCrewSkin(self):
        equip = CrewSkinEquip(self._tankManInvID, self._crewSkinID)
        yield equip.request()

    def _updateViewModel(self):
        with self.viewModel.transaction() as vm:
            self._fillViewModel(vm)

    def _fillViewModel(self, vm):
        skinItem = self._itemsCache.items.getCrewSkin(self._crewSkinID)
        vm.setDescription(str(i18n.makeString(skinItem.getDescription())))
