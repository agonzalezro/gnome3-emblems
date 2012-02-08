Introduction
------------

After update to GNOME 3 and Nautilus 3.x I've realized that one of the
functions that I was using was not there! The emblems were dissapear!
How can I mark my series as viewed?

![fuuuuuu](http://playstationeu.i.lithium.com/t5/image/serverpage/image-id/261315i16953D1D03261049/image-size/original?v=mpbl-1&px=-1)

No problem, this nautilus script is here to help you.


What's this?
------------

This extension will brings to you a new property page:

![screenshot](https://p.twimg.com/AlKL6fPCEAA_g0_.pnga)


Installation
------------

As ``root`` user copy the .py file in /usr/share/nautilus-python/extensions/


Bugs
----

This is a work in progress in a very early state, things that must be done
(ordered by preference order):

1. When a new emblem is selected remove the old one without the need of refresh the
   nautilus view.
2. Transform the icon view on selection multiple (problems settings the emblems on
   this case).
3. Select the emblems that are being used:
    - This selection must be the intersection between all the selected files.
    - If some of the emblems is changed, all the files will have the same
      emblems.
4. Create a instalation script.
