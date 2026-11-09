# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/base_crew_dialog_template_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/dialogs/base_crew_dialog_template_view.py
from gui.impl.dialogs.dialog_template import DialogTemplateView
from gui.impl.lobby.crew.crew_sounds import CREW_SOUND_OVERLAY_SPACE

class BaseCrewDialogTemplateView(DialogTemplateView):
    __slots__ = ('_isClosed', )
    _COMMON_SOUND_SPACE = CREW_SOUND_OVERLAY_SPACE

    def __init__(self, layoutID=None, uniqueID=None, *args, **kwargs):
        super(BaseCrewDialogTemplateView, self).__init__(layoutID, uniqueID, *args, **kwargs)
        self._isClosed = False

    def _closeClickHandler(self, args=None):
        self._isClosed = True
        super(BaseCrewDialogTemplateView, self)._closeClickHandler(args)
