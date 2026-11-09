# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/reset_all_perks_confirm_dialog.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/dialogs/reset_all_perks_confirm_dialog.py
from gui.impl.dialogs.dialog_template_button import CancelButton, ConfirmButton
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.lobby.crew.dialogs.recruit_window.base_crew_dialog_template_with_blur_view import BaseCrewDialogTemplateWithBlurView

class ResetAllPerksConfirmDialog(BaseCrewDialogTemplateWithBlurView):

    def _onLoading(self, *args, **kwargs):
        rDialogTemplates = R.strings.dialogs.resetAllPerks
        rDialogs = R.images.gui.maps.uiKit.dialogs
        self.setSubView(Placeholder.TITLE, SimpleTextTitle(rDialogTemplates.title()))
        self.setSubView(Placeholder.ICON, IconSet(rDialogs.icons.alert(), [
         rDialogs.highlights.yellow_1()]))
        self.setSubView(Placeholder.CONTENT, SimpleTextContent(rDialogTemplates.warning()))
        self.addButton(ConfirmButton(rDialogTemplates.submit()))
        self.addButton(CancelButton(rDialogTemplates.cancel()))
        super(ResetAllPerksConfirmDialog, self)._onLoading(*args, **kwargs)
