from fl_model.decorators import keyEchoes, since


def getVisible(index: int, /) -> bool:
    """Returns whether an FL Studio window is visible.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    ## Returns:
     * `bool`: whether it is visible

    Included since API version 1
    """
    return False


def showWindow(index: int, /) -> None:
    """Shows an FL Studio window specified by `index`.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    Included since API version 1
    """


@since(5)
def hideWindow(index: int, /) -> None:
    """Hides an FL Studio window specified by `index`.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    Included since API version 5
    """


def getFocused(index: int, /) -> bool:
    """Returns whether an FL Studio window is focused (meaning it is the
    currently selected Window in FL Studio).

    ## NOTE:
    * this doesn't necessarily mean that it is the currently selected window
      in the host operating system, so functions that rely on keypress emulation
      (such as [`ui.copy()`][ui.copy]) may not work as intended, even if this
      returns `True`.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

          * `widPlugin` (`5`): Plugin Window (note that this constant is only
            usable in this particular function).

          * `widPluginEffect` (`6`): Effect Plugin Window.

          * `widPluginGenerator` (`7`): Generator Plugin Window.

    ## Returns:
     * `bool`: whether it is visible

    Included since API version 1
    """
    return False


@since(2)
def setFocused(index: int, /) -> None:
    """Sets which FL Studio window should be focused (meaning it is the
    currently selected Window in FL Studio).

    ## NOTE:
    * This doesn't necessarily mean that it will be the currently selected
      window in the host operating system, so functions that rely on keypress
      emulation (such as `ui.copy()`) may not work as intended, even after calling
      this function.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    Included since API version 2
    """


def getFocusedFormCaption() -> str:
    """Returns the caption (title) of the focused FL Studio window. This isn't
    necessarily the same as the plugin's name.

    ## Returns:
     * `str`: window title

    Included since API version 1
    """
    return ""


@since(13)
def getFocusedFormID() -> int:
    """Returns ID of the focused window.

    Used to get the channel rack index or mixer plugin ID for plugins

    ## WARNING:
    * This can crash FL Studio's API if a plugin window is in the process of
      closing (until API v21).

    ## NOTE:
    * The official documentation says that this function returns a string,
      which is incorrect.

    ## Returns:
    * `int`: form ID:
          * Index in channel rack (zero indexed)

          * Plugin ID in mixer (track number * 4194304 + slot index * 65536,
            all zero indexed)

          * Window ID for mixer, channel rack, playlist, etc

          * `-1` for invalid plugin (eg. script output or settings window)

    Included since API version 13
    """
    return 0


@since(5)
def getFocusedPluginName() -> str:
    """Returns the plugin name for the active window if it is a plugin,
    otherwise an empty string.

    ## Returns:
     * `str`: plugin name

    Included since API version 5
    """
    return ""


@since(13)
def scrollWindow(index: int, value: int, directionFlag: int = 0, /) -> None:
    """Scrolls on the window specified by `index`. Value is index for whatever
    is contained on that window (eg channels for the Channel Rack or tracks for
    the Mixer).

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

     * `value` (`int`): index to scroll to:
          * on mixer: track number

          * on channel rack: channel number

          * on playlist: playlist track number

          * on playlist: bar number (when `directionFlag` is set to `1`)

    Included since API version 13
    """


def nextWindow() -> int:
    """Switch to the next window

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


@keyEchoes()
def selectWindow(shift: bool, /) -> int:
    """Switch to the next window by pressing the `Tab` key. If `shift` is
    `True`, switch to the previous window by pressing `Shift` and `Tab`.

    ## WARNING:
    * This function echoes the tab key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Args:
     * `shift` (`bool`): whether the shift key is pressed.

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0
