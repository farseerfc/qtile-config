from libqtile.config import Key, Screen, Group, Click, Drag
from libqtile.command import lazy
from libqtile import layout, bar, widget

terminal = "termite"

wallpaper_path = "~/Dropbox/Photos/wallpaper/"
wallpaper_cmd = "feh -z --bg-fill " + wallpaper_path


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

    Key([mod],          "Return",   lazy.spawn(terminal)),
    Key([mod],          "y",        lazy.spawn("ydcv-notify.sh")),
    Key([mod],          "w",        lazy.spawn(wallpaper_cmd)),

    # Toggle between different layouts as defined below
    Key([mod],          "space",    lazy.nextlayout()),
    Key([mod, shift],   "c",        lazy.window.kill()),

    Key([mod, ctrl],    "r",        lazy.restart()),
    # Key([mod],          "r",        lazy.spawncmd()),
    Key([mod],          "r",        lazy.spawn("dmenu_run")),
    Key([mod, shift],   "q",        lazy.shutdown()),
    Key([mod],          "f",        lazy.window.toggle_fullscreen()),
    Key([mod, shift],   "f",        lazy.window.toggle_floating()),
    Key([mod],          "comma",    lazy.window.down_opacity()),
    Key([mod],          "period",   lazy.window.up_opacity()),
]

groups = [Group(chr(ord("1") + i)) for i in range(9)]
for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([mod, shift], i.name, lazy.window.togroup(i.name)))

keys.append(Key([mod], "Left", lazy.group.prevgroup()))
keys.append(Key([mod], "Right", lazy.group.nextgroup()))

dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.MonadTall(border_width=1, name="Tall"),
    layout.Slice('left', 200, role="buddy_list", name="Pidgin",
                 fallback=layout.Matrix()),
    layout.Matrix(),
    layout.Max(),
    layout.TreeTab(),
    layout.Zoomy(),
    layout.Floating()
]

fontsize = 18

screens = [
    Screen(
        # top=bar.Bar(
        #     [
        #         widget.GroupBox(),
        #         # widget.Prompt(),
        #         widget.WindowTabs(fontsize=fontsize,
        #                           separator=' | ',
        #                           selected=("{", "}")),
        #         widget.CPUGraph(graph_color="00ff00"),
        #         widget.MemoryGraph(),
        #         widget.CurrentLayout(fontsize=fontsize),
        #         widget.Systray(),
        #         widget.Clock('%m/%d(%a)%H:%M', fontsize=fontsize),
        #     ],
        #     30,
        # ),
    ),
    Screen()
]
mouse = [
    Drag(
        [mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

import hooks

main = None
follow_mouse_focus = False
cursor_warp = False
floating_layout = layout.Floating(auto_float_types=set([
    'notification', 'splash', 'toolbar', 'utility', 'dialog']))
auto_fullscreen = True
widget_defaults = {}
