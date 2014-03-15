from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"
ctrl = "control"
shift = "shift"

keys = [
    # Commands for MonadTall
    Key([mod],          "k",        lazy.layout.down()),
    Key([mod],          "j",        lazy.layout.up()),
    Key([mod, shift],   "k",        lazy.layout.shuffle_down()),
    Key([mod, shift],   "j",        lazy.layout.shuffle_up()),
    Key([mod],          "h",        lazy.layout.grow()),
    Key([mod],          "l",        lazy.layout.shrink()),
    Key([mod],          "n",        lazy.layout.normalize()),
    Key([mod],          "o",        lazy.layout.maximize()),
    Key([mod, shift],   "space",    lazy.layout.flip()),

    # Commands for Matrix
    Key([mod, shift],   "h",        lazy.layout.add()),
    Key([mod, shift],   "l",        lazy.layout.delete()),

    Key([mod],          "Return",   lazy.spawn("termite")),
    Key([mod],          "y",        lazy.spawn("ydcv-notify.sh")),
    Key([mod],          "w",        lazy.spawn(wallpaper_cmd)),

    # Toggle between different layouts as defined below
    Key([mod],          "space",    lazy.nextlayout()),
    Key([mod, shift],   "c",        lazy.window.kill()),

    Key([mod, ctrl],    "r",        lazy.restart()),
    Key([mod],          "r",        lazy.spawncmd()),
    Key([mod, shift],   "q",        lazy.shutdown()),
    Key([mod],          "f",        lazy.window.toggle_fullscreen()),
    Key([mod, shift],   "f",        lazy.window.toggle_floating()),
    Key([mod],          "comma",    lazy.window.down_opacity()),
    Key([mod],          "period",   lazy.window.up_opacity()),
]
