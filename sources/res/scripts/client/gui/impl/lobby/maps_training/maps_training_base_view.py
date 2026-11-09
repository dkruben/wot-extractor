# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/maps_training/maps_training_base_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/maps_training/maps_training_base_view.py
from gui.impl.pub import ViewImpl
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from frameworks.wulf import ViewSettings, ViewFlags
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader

class MapsTrainingBaseView(ViewImpl):
    appLoader = dependency.descriptor(IAppLoader)
    _BACKGROUND_ALPHA = 0

    def __init__(self, viewResource, viewModel, *args, **kwargs):
        settings = ViewSettings(viewResource)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = viewModel
        settings.args = args
        settings.kwargs = kwargs
        super(MapsTrainingBaseView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(MapsTrainingBaseView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(MapsTrainingBaseView, self)._initialize(*args, **kwargs)
        app = self.appLoader.getApp()
        app.setBackgroundAlpha(self._BACKGROUND_ALPHA)

    def _onLoading(self, *args, **kwargs):
        super(MapsTrainingBaseView, self)._onLoading(*args, **kwargs)
        self._addListeners()

    def _finalize(self):
        self._removeListeners()
        super(MapsTrainingBaseView, self)._finalize()

    def _addListeners(self):
        self.viewModel.onMoveSpace += self._onMoveSpace
        self.viewModel.onMouseOver3dScene += self._onMouseOver3dScene

    def _removeListeners(self):
        self.viewModel.onMoveSpace -= self._onMoveSpace
        self.viewModel.onMouseOver3dScene -= self._onMouseOver3dScene

    def _onMoveSpace(self, args=None):
        if args is None:
            return
        else:
            ctx = {'dx': (args.get('dx')), 'dy': (args.get('dy')), 'dz': (args.get('dz'))}
            g_eventBus.handleEvent(CameraRelatedEvents(CameraRelatedEvents.LOBBY_VIEW_MOUSE_MOVE, ctx=ctx), EVENT_BUS_SCOPE.GLOBAL)
            g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_SPACE_MOVED, ctx=ctx), EVENT_BUS_SCOPE.GLOBAL)
            return

    def _onMouseOver3dScene(self, args):
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_OVER_3DSCENE, ctx={'isOver3dScene': (bool(args.get('isOver3dScene')))}))
