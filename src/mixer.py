"""Mixer Module (FL Studio built-in)

Allows you to control and interact with the FL Studio Mixer, and with
effects tracks.

NOTES:
 * Mixer tracks are zero-indexed
"""

def trackNumber() -> int:
    """Returns the index of the first currently selected mixer track.

    Returns:
     * `int`: selected mixer track
    
    Included since API version 1
    """

def getTrackInfo(mode: int) -> int:
    """Returns the index of a special mixer track depending on `mode`.
    
    This function can serve to help potentially future-proof scripts by ensuring
    that they continue to use the correct indexes for mixer tracks

    Args:
     * `mode` (`int`): Determined the type of information provided:
            * `TN_Master` (`0`): Index of master track
            * `TN_FirstIns` (`1`): Index of first insert track
            * `TN_LastIns` (`2`): Index of last insert track
            * `TN_Sel` (`3`): Index of the "current" track (the one with the
              large peak meter docked to the left).

    Returns:
     * `int`: requested track index
    
    Included since API version 1
    """

def setTrackNumber(trackNumber: int, flags:int=[]) -> None:
    """Select the mixer track at `trackNumber`.
    
    NOTE: All functionality except for scrolling flag can be replicated more
    easily using `mixer.selectTrack()`.

    Args:
     * `trackNumber` (`int`): the track index to select
     * `flags` (`int`, optional): Options to do with new track selection.
            * `curfxScrollToMakeVisible` (`1`): Scroll to make the 
              newly-selected track visible.
            * `curfxCancelSmoothing` (`2`): Effect unknown
            * `curfxNoDeselectAll` (`4`): Prevent the deselection of other
              selected tracks??? Doesn't seem to work.
            * `curfxMinimalLatencyUpdate` (`8`): Effect unknown
            Defaults to `[]`.
    
    Included since API version 1
    """

def trackCount() -> int:
    """Returns the number of tracks available on the mixer.
    Tracks range = `0 - (trackCount()-1)`. Includes master and "current track"
    tracks.

    Returns:
     * `int`: number of tracks
        
    Included since API version 1
    """

def getTrackName(index: int) -> str:
    """Returns the name of the track at `index`.

    Args:
     * `index` (`int`): track index

    Returns:
     * `str`: name of track.
    """
