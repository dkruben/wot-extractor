# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/base_crew_dialog_template_with_blur_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/base_crew_dialog_template_with_blur_view.py
from gui.impl.lobby.crew.dialogs.base_crew_dialog_template_view import BaseCrewDialogTemplateView
from gui.shared.view_helpers.blur_manager import CachedBlur

class BaseCrewDialogTemplateWithBlurView(BaseCrewDialogTemplateView):
    __slots__ = ('_blur', )

    def __init__(self, layoutID=None, uniqueID=None, *args, **kwargs):
        super(BaseCrewDialogTemplateWithBlurView, self).__init__(layoutID, uniqueID, *args, **kwargs)
        self._blur = None
        return

    def _onLoading(self, *args, **kwargs):
        super(BaseCrewDialogTemplateWithBlurView, self)._onLoading(*args, **kwargs)
        self._blur = CachedBlur(enabled=True, ownLayer=self.getParentWindow().layer - 1, uiBlurRadius=35)

    def _finalize(self):
        super(BaseCrewDialogTemplateWithBlurView, self)._finalize()
        if self._blur:
            self._blur.fini()
