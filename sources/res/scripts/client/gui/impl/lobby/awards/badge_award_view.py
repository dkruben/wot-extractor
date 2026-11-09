# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/awards/badge_award_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/awards/badge_award_view.py
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.awards.badge_award_view_model import BadgeAwardViewModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.badge import Badge

class BadgeAwardView(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.awards.BadgeAwardView())
        settings.model = BadgeAwardViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(BadgeAwardView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BadgeAwardView, self).getViewModel()

    def _onLoading(self, badge):
        with self.viewModel.transaction() as model:
            model.setBadgeId(badge.badgeID)


class BadgeAwardViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, badge, parent=None):
        super(BadgeAwardViewWindow, self).__init__(content=BadgeAwardView(badge), parent=parent)
