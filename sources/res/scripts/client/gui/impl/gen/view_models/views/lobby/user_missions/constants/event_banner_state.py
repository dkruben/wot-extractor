# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/constants/event_banner_state.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/constants/event_banner_state.py
from frameworks.wulf import ViewModel

class EventBannerState(ViewModel):
    __slots__ = ()
    ANNOUNCE = 'announce'
    INTRO = 'intro'
    IN_PROGRESS = 'inProgress'
    INACTIVE = 'inactive'
    FINISHED = 'finished'

    def __init__(self, properties=0, commands=0):
        super(EventBannerState, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(EventBannerState, self)._initialize()
