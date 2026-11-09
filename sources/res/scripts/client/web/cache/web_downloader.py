# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/cache/web_downloader.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/cache/web_downloader.py
from __future__ import absolute_import
import time
from functools import partial
from helpers import threads
from gui.shared.RemoteDataDownloader import _HttpOpenUrlJob
from helpers.web.downloader import IDownloader
from shared_utils import nextTick

class WebDownloader(IDownloader):

    def __init__(self, workersLimit, queueLimit=threads.INFINITE_QUEUE_SIZE):
        self.__worker = threads.ThreadPool(workersLimit, queueLimit)
        self.__worker.start()
        self.__paused = False

    @property
    def stopped(self):
        return self.__worker is None

    def close(self):
        if self.__worker:
            self.__worker.stop()
            self.__worker = None
        return

    def downloadLowPriority(self, url, callback):
        self.__worker.putLowPriorityJob(_HttpOpenUrlJob(url, None, partial(self.__onDownload, url, callback)))
        return

    def download(self, url, callback):
        self.__worker.putJob(_HttpOpenUrlJob(url, None, partial(self.__onDownload, url, callback)))
        return

    def setPause(self, value):
        self.__paused = value

    def __onDownload(self, url, callback, data, lastModified, expires):
        while self.__paused:
            time.sleep(1)

        nextTick(partial(callback, url, data))()
