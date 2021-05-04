Strange Stars
=============

I trust I don't need to point out the main inspiration for this game
once you get it to run. If you can't, please come back in a while, this
thing is in suuuch an early state...


TODO
----

* EVERYTHING!
* Re-read `bin/make_star_field.py` and update the other `bin/make_*`
  equivalently.
* Antialiasing may cause weird rendering errors on my potato, but looks
  good for others, so maybe reactivate it. To quote
  `bin/make_ship_arrowhead.py`:

      nodepath.set_antialias(AntialiasAttrib.MLine | AntialiasAttrib.MBetter)

  Also there's now two lines to set relevant settings before `ShowBase`
  is instantiated. Of course the RIGHT wolution would be to have an
  ingame menu that lets you set AA on the fly, and exchanges the
  relevant buffers.
