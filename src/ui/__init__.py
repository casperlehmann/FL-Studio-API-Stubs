"""User Interface Module (FL Studio built-in)

Allows you to control and interact with FL Studio's UI.

## WARNING:
* Many of the functions in this module will simply echo a hotkey into whatever
  application is active, meaning that actions can potentially be sent to the
  wrong application. Functions that have this behavior are listed with a short
  warning saying so.

## HELP WANTED:
* What do the return values mean?
"""
from .__browser import (
    navigateBrowser,
    previewBrowserMenuItem,
    selectBrowserMenuItem,
    getFocusedNodeCaption,
    getFocusedNodeFileType,
    isBrowserAutoHide,
    setBrowserAutoHide,
    navigateBrowserTabs,
)
from .__editors import (
    launchAudioEditor,
    openEventEditor,
)
from .__fl_state import (
    isClosing,
    isMetronomeEnabled,
    isStartOnInputEnabled,
    isPrecountEnabled,
    isLoopRecEnabled,
    getSnapMode,
    setSnapMode,
    snapMode,
    snapOnOff,
    getTimeDispMin,
    setTimeDispMin,
    getHintMsg,
    setHintMsg,
    showNotification,
    getHintValue,
    getProgTitle,
    getVersion,
    getStepEditMode,
    setStepEditMode,
)
from .__keyboard import (
    cut,
    copy,
    paste,
    insert,
    delete,
    enter,
    escape,
    yes,
    no,
    up,
    down,
    left,
    right,
)
from .__navigation import (
    jog,
    jog2,
    strip,
    stripJog,
    stripHold,
    previous,
    next,
    moveJog,
    horZoom,
    verZoom,
    isInPopupMenu,
    closeActivePopupMenu,
)
from .__overlays import (
    crDisplayRect,
    miDisplayRect,
    miDisplayDockRect,
)
from .__windows import (
    getVisible,
    showWindow,
    hideWindow,
    getFocused,
    setFocused,
    getFocusedFormCaption,
    getFocusedFormID,
    getFocusedPluginName,
    scrollWindow,
    nextWindow,
    selectWindow,
)

__all__ = [
    'navigateBrowser',
    'navigateBrowserTabs',
    'previewBrowserMenuItem',
    'selectBrowserMenuItem',
    'getFocusedNodeCaption',
    'getFocusedNodeFileType',
    'isBrowserAutoHide',
    'setBrowserAutoHide',
    'launchAudioEditor',
    'openEventEditor',
    'isClosing',
    'isMetronomeEnabled',
    'isStartOnInputEnabled',
    'isPrecountEnabled',
    'isLoopRecEnabled',
    'getSnapMode',
    'setSnapMode',
    'snapMode',
    'snapOnOff',
    'getTimeDispMin',
    'setTimeDispMin',
    'getHintMsg',
    'setHintMsg',
    'showNotification',
    'getHintValue',
    'getProgTitle',
    'getVersion',
    'getStepEditMode',
    'setStepEditMode',
    'cut',
    'copy',
    'paste',
    'insert',
    'delete',
    'enter',
    'escape',
    'yes',
    'no',
    'up',
    'down',
    'left',
    'right',
    'jog',
    'jog2',
    'strip',
    'stripJog',
    'stripHold',
    'previous',
    'next',
    'moveJog',
    'horZoom',
    'verZoom',
    'isInPopupMenu',
    'closeActivePopupMenu',
    'crDisplayRect',
    'miDisplayRect',
    'miDisplayDockRect',
    'getVisible',
    'showWindow',
    'hideWindow',
    'getFocused',
    'setFocused',
    'getFocusedFormCaption',
    'getFocusedFormID',
    'getFocusedPluginName',
    'scrollWindow',
    'nextWindow',
    'selectWindow',
]
