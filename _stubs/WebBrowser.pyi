# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/WebBrowser.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import functools as functools
import logging as logging
from builtins import zip as zip
from enum import Enum as Enum
from future.moves.urllib import parse as parse
import BigWorld as BigWorld
import Keys as Keys
import SoundGroups as SoundGroups
import Settings as Settings
from gui.shared import event_dispatcher as event_dispatcher
from Event import Event as Event, EventManager as EventManager
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui import GUI_SETTINGS as GUI_SETTINGS
from web.cache.web_cache import WebExternalCache as WebExternalCache
_logger: Any
_webAppLogger: Any
_BROWSER_KEY_LOGGING = False
_WOT_CLIENT_PARAM_NAME = 'wot_client_param'
_WOT_RESOURCE_CUSTOM_SCHEME = 'wotdata'
_WEB_CACHE_FOLDER = 'web_cache'
_WEB_MANIFEST_KEY = 'webManifestURL'
_EXTENDED_LOGGING = False
_g_webCache = None
_LOG_SEVERITY_TO_LOG_LEVEL_MAP: dict
g_mgr: Any

class LogSeverity(Enum):
    disable = 0
    verbose = 1
    info = 2
    warning = 3
    error = 4

class WebBrowser(object):
    id: Any
    hasBrowser: Any
    initializationUrl: Any
    baseUrl: Any
    url: Any
    width: Any
    height: Any
    cursor: Any
    isNavigationComplete: Any
    isFocused: Any
    isAudioPlaying: Any
    isReady: Any
    updateInterval = 0.01
    isSuccessfulLoad: Any
    __skipEscape: Any
    __ignoreKeyEvents: Any
    __ignoreAltKey: Any
    __ignoreCtrlClick: Any
    __ignoreShiftClick: Any
    __useSpecialKeys: Any
    __allowMiddleClick: Any
    __allowRightClick: Any
    __allowMouseWheel: Any
    __browserID: Any
    __cbID: Any
    __baseUrl: Any
    __uiObj: Any
    __startFocused: Any
    __browser: Any
    __isNavigationComplete: Any
    __isFocused: Any
    __isAudioPlaying: Any
    __navigationFilters: Any
    __allowAutoLoadingScreenChange: Any
    __isCloseTriggered: Any
    __isAudioMutable: Any
    __ctrlDown: Any
    __shiftDown: Any
    __isReady: Any
    _enableUpdate: Any
    __eventMgr: Any
    onLoadStart: Any
    onLoadEnd: Any
    onLoadingStateChange: Any
    onReadyToShowContent: Any
    onNavigate: Any
    onReady: Any
    onJsHostQuery: Any
    onTitleChange: Any
    onFailedCreation: Any
    onCanCreateNewBrowser: Any
    onUserRequestToClose: Any
    onAudioStatusChanged: Any
    onCursorUpdated: Any
    onChangeAddressBar: Any
    onFocusChanged: Any
    onResized: Any
    onTextureStateChanged: Any
    __disableKeyHandlers: Any
    __readyToShow: Any
    __successfulLoad: Any
    __isMouseDown: Any
    __isWaitingForUnfocus: Any
    __specialKeyHandlers: Any
    __browserKeyHandlers: Any
    # decorador original: @skipEscape.setter
    def skipEscape(self, value):
        ...
    # decorador original: @ignoreKeyEvents.setter
    def ignoreKeyEvents(self, value):
        ...
    # decorador original: @ignoreAltKey.setter
    def ignoreAltKey(self, value):
        ...
    # decorador original: @ignoreCtrlClick.setter
    def ignoreCtrlClick(self, value):
        ...
    # decorador original: @ignoreShiftClick.setter
    def ignoreShiftClick(self, value):
        ...
    # decorador original: @useSpecialKeys.setter
    def useSpecialKeys(self, value):
        ...
    # decorador original: @allowMiddleClick.setter
    def allowMiddleClick(self, value):
        ...
    # decorador original: @allowRightClick.setter
    def allowRightClick(self, value):
        ...
    # decorador original: @allowMouseWheel.setter
    def allowMouseWheel(self, value):
        ...
    def __init__(self, browserID, uiObj, url='about:blank', isFocused=False, handlers=None):
        ...
    def create(self):
        ...
    def setDisabledKeys(self, keys):
        ...
    def ready(self, success):
        ...
    def invalidateView(self):
        ...
    def updateSize(self, size):
        ...
    def destroy(self):
        ...
    def focus(self, silent=False):
        ...
    def unfocus(self, silent=False):
        ...
    def refresh(self, ignoreCache=True):
        ...
    def navigate(self, url):
        ...
    def sendMessage(self, message):
        ...
    def sendEvent(self, webEvent):
        ...
    def navigateBack(self):
        ...
    def navigateForward(self):
        ...
    def navigateStop(self):
        ...
    def __getBrowserKeyHandler(self, key, isKeyDown, isAltDown, isShiftDown, isCtrlDown):
        ...
    def handleKeyEvent(self, event):
        ...
    def browserMove(self, x, y, z):
        ...
    def browserDown(self, x, y, z):
        ...
    def browserUp(self, x, y, z):
        ...
    def browserFocusOut(self):
        ...
    def browserAction(self, action):
        ...
    def onBrowserShow(self, needRefresh):
        ...
    def onBrowserHide(self):
        ...
    def addFilter(self, handler):
        ...
    def removeFilter(self, handler):
        ...
    def filterNavigation(self, url):
        ...
    def onResourceLoadRequest(self, url):
        ...
    def setAllowAutoLoadingScreen(self, enabled):
        ...
    def setIsAudioMutable(self, isAudioMutable):
        ...
    def changeTitle(self, title):
        ...
    def __onLoadStart(self, url):
        ...
    def __onLoadEnd(self, url, isLoaded=True, httpStatusCode=None, errorDesc=None):
        ...
    def __onLoadingStateChange(self, isLoading):
        ...
    def __onReadyToShowContent(self, url):
        ...
    def __isValidTitle(self, title):
        ...
    def __onTitleChange(self, title):
        ...
    def __onCursorUpdated(self, cursor):
        ...
    def __onReady(self, success):
        ...
    def __onDestroy(self):
        ...
    def __onJsHostQuery(self, command):
        ...
    def __onConsoleMessage(self, level, message, lineNumber, source, viewId):
        ...
    def __onChangeAddressBar(self, url):
        ...
    def __onResized(self, width, height):
        ...
    def __onTextureStateChanged(self, isOk):
        ...
    def __onAudioStatusChanged(self, isPlaying):
        ...
    def executeJavascript(self, script, frame):
        ...

class EventListener(object):
    isBrowserPlayingAudio = False
    __eventMgr: Any
    onLoadStart: Any
    onLoadEnd: Any
    onLoadingStateChange: Any
    onCursorUpdated: Any
    onDOMReady: Any
    onReady: Any
    onJsHostQuery: Any
    onTitleChange: Any
    onDestroy: Any
    onAudioStatusChanged: Any
    onConsoleMessage: Any
    onChangeAddressBar: Any
    onResized: Any
    onTextureStateChanged: Any
    __urlFailed: Any
    __browserProxy: Any
    def __init__(self, browser):
        ...
    def clear(self):
        ...
    def newNavigation(self):
        ...
    def onChangeCursor(self, cursorType):
        ...
    def onChangeTitle(self, title):
        ...
    def ready(self, success):
        ...
    def destroy(self):
        ...
    def onBeginLoadingFrame(self, frameId, isMainFrame, url):
        ...
    def onFailLoadingFrame(self, frameId, isMainFrame, url, errorCode, errorDesc):
        ...
    def onFinishLoadingFrame(self, frameId, isMainFrame, url, httpStatusCode):
        ...
    def onBrowserLoadingStateChange(self, isLoading):
        ...
    def onDocumentReady(self, url):
        ...
    def onAddConsoleMessage(self, level, message, lineNumber, source, viewId):
        ...
    def onFilterNavigation(self, url):
        ...
    def onResourceLoadRequest(self, method, url):
        ...
    def onResourceLoadComplete(self, method, url):
        ...
    def onResourceLoadError(self, method, url, status, statusStr, error, requestHeaders, responseHeaders):
        ...
    def onWhitelistMiss(self, isMainFrame, failedURL, httpStatusCode=None):
        ...
    def onShowCreatedWebView(self, url, isPopup):
        ...

class WebBrowserManager(object):
    first: Any
    len: Any
    isBackgroundAudioMuted = False
    __browsers: Any
    def __init__(self):
        ...
    def addBrowser(self, browser):
        ...
    def delBrowser(self, browser):
        ...
    def getBrowserPlayingAudioCount(self):
        ...
    def updateGameAudio(self):
        ...
    def handleKeyEvent(self, event):
        ...
    def __muteBackgroundAudio(self, isMute):
        ...
    def __unFocusChanged(self, browser, isFocused):
        ...

class LL_KEYS(object):
    VK_CANCEL = 3
    VK_HELP = 6
    VK_BACK_SPACE = 8
    VK_TAB = 9
    VK_CLEAR = 12
    VK_RETURN = 13
    VK_ENTER = 14
    VK_SHIFT = 16
    VK_CONTROL = 17
    VK_ALT = 18
    VK_PAUSE = 19
    VK_CAPS_LOCK = 20
    VK_ESCAPE = 27
    VK_SPACE = 32
    VK_PAGE_UP = 33
    VK_PAGE_DOWN = 34
    VK_END = 35
    VK_HOME = 36
    VK_LEFT = 37
    VK_UP = 38
    VK_RIGHT = 39
    VK_DOWN = 40
    VK_PRINTSCREEN = 44
    VK_INSERT = 45
    VK_DELETE = 46

class CURSOR_TYPES(object):
    Pointer = 0
    Cross = 1
    Hand = 2
    IBeam = 3
    Wait = 4
    Help = 5
    EastResize = 6
    NorthResize = 7
    NorthEastResize = 8
    NorthWestResize = 9
    SouthResize = 10
    SouthEastResize = 11
    SouthWestResize = 12
    WestResize = 13
    NorthSouthResize = 14
    EastWestResize = 15
    NorthEastSouthWestResize = 16
    NorthWestSouthEastResize = 17
    ColumnResize = 18
    RowResize = 19
    MiddlePanning = 20
    EastPanning = 21
    NorthPanning = 22
    NorthEastPanning = 23
    NorthWestPanning = 24
    SouthPanning = 25
    SouthEastPanning = 26
    SouthWestPanning = 27
    WestPanning = 28
    Move = 29
    VerticalText = 30
    Cell = 31
    ContextMenu = 32
    Alias = 33
    Progress = 34
    NoDrop = 35
    Copy = 36
    CursorNone = 37
    NotAllowed = 38
    ZoomIn = 39
    ZoomOut = 40
    Grab = 41
    Grabbing = 42
    Custom = 43

def initExternalCache():
    ...
def destroyExternalCache():
    ...
def pauseExternalCache(value):
    ...
def getWebCache():
    ...
