# -*- coding: utf-8 -*-
# See github page to report issues or to contribute:
# https://github.com/Arthaey/anki-custom-keyboard-shortcuts
#
# Also available for Anki at https://ankiweb.net/shared/info/1483821271

from aqt.qt import QMainWindow
from aqt.main import AnkiQt

################################################################################
#
# USER-MODIFABLE SETTINGS. CHANGE THINGS HERE TO THE SETTINGS YOU WANT.
#
################################################################################

# CUSTOMIZE THESE SHORTCUT KEYS.
GLOBAL_DECKS_SHORTCUT    = "d"
GLOBAL_OVERVIEW_SHORTCUT = "s"
GLOBAL_ADD_SHORTCUT      = "a"
GLOBAL_BROWSE_SHORTCUT   = "b"
GLOBAL_STATS_SHORTCUT    = "S"
GLOBAL_SYNC_SHORTCUT     = "y"

# TO DISABLE A SHORTCUT ENTIRELY, DELETE THE '#' IN FRONT OF IT.
DISABLED_SHORTCUTS = [
    #GLOBAL_DECKS_SHORTCUT,
    #GLOBAL_OVERVIEW_SHORTCUT,
    #GLOBAL_ADD_SHORTCUT,
    #GLOBAL_BROWSE_SHORTCUT,
    #GLOBAL_STATS_SHORTCUT,
    #GLOBAL_SYNC_SHORTCUT,
]

################################################################################
#
# DO NOT CHANGE ANYTHING BELOW HERE UNLESS YOU KNOW WHAT YOU'RE DOING. :)
#
################################################################################

# Copy-pasted from aqt/main.py
def _keyPressEvent(self, evt):
    # do we have a delegate?
    if self.keyHandler:
        # did it eat the key?
        if self.keyHandler(evt):
            return
    # run standard handler
    QMainWindow.keyPressEvent(self, evt)
    # check global keys
    key = unicode(evt.text())

    if key in DISABLED_SHORTCUTS:
        return

    if key == GLOBAL_DECKS_SHORTCUT:
        self.moveToState("deckBrowser")
    elif key == GLOBAL_OVERVIEW_SHORTCUT:
        if self.state == "overview":
            self.col.startTimebox()
            self.moveToState("review")
        else:
            self.moveToState("overview")
    elif key == GLOBAL_ADD_SHORTCUT:
        self.onAddCard()
    elif key == GLOBAL_BROWSE_SHORTCUT:
        self.onBrowse()
    elif key == GLOBAL_STATS_SHORTCUT:
        self.onStats()
    elif key == GLOBAL_SYNC_SHORTCUT:
        self.onSync()

# Replaces the method entirely; wrapping would cause the customized shortcuts to
# run *in addition to* the original shortcuts.
AnkiQt.keyPressEvent = _keyPressEvent
