# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#-----------------------------------------------------------------------------------
#custom imports
import os
import subprocess
from libqtile import hook
from colors import catppuccin_frappe as c_frappe
from unicodes import lower_left_triangle, left_arrow, right_arrow
#-----------------------------------------------------------------------------------

mod = "mod4"
terminal = guess_terminal()

myLauncher = "rofi -show drun"
myFileBrowser = "pcmanfm"
myBrowser = "firefox"
myPowerMenu = "rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu"

#  _  __          _     _           _ _                 
# | |/ /         | |   (_)         | (_)                
# | ' / ___ _   _| |__  _ _ __   __| |_ _ __   __ _ ___ 
# |  < / _ \ | | | '_ \| | '_ \ / _` | | '_ \ / _` / __|
# | . \  __/ |_| | |_) | | | | | (_| | | | | | (_| \__ \
# |_|\_\___|\__, |_.__/|_|_| |_|\__,_|_|_| |_|\__, |___/
#            __/ |                             __/ |    
#           |___/                             |___/     

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

# My changes
    Key([mod], "r", 
		lazy.spawn(myLauncher), 
		desc="Launches Rofi"),

    Key([mod], "e", 
		lazy.spawn(myFileBrowser), 
		desc="Launches Thunar"),

    Key([mod], "b", 
		lazy.spawn(myBrowser), 
		desc="Launches Firefox"),

    Key([mod, "control"], "x", 
		lazy.spawn(myPowerMenu), 
		desc="Launches rofi-power-menu"),

    #Key([], "XF86AudioRaiseVolume", lazy.spwan("pactl -- set-sink-volume 0 +10%"), desc="Increase Vol."),
    #Key([], "XF86AudioRaiseVolume", lazy.spwan("pactl -- set-sink-volume 0 -10%"), desc="Decrease Vol."),
]


#   _____                           
#  / ____|                          
# | |  __ _ __ ___  _   _ _ __  ___ 
# | | |_ | '__/ _ \| | | | '_ \/ __|
# | |__| | | | (_) | |_| | |_) \__ \
#  \_____|_|  \___/ \__,_| .__/|___/
#                        | |        
#                        |_|

#groups = [Group(i) for i in "123456"]

groups = [
        Group("1", label="一"),
        Group("2", label="二"),
        Group("3", label="三"),
        Group("4", label="四"),
        Group("5", label="五"),
        Group("6", label="六"),
        Group("7", label="七"),
        ]


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

#  _                             _       
# | |                           | |      
# | |     __ _ _   _  ___  _   _| |_ ___ 
# | |    / _` | | | |/ _ \| | | | __/ __|
# | |___| (_| | |_| | (_) | |_| | |_\__ \
# |______\__,_|\__, |\___/ \__,_|\__|___/
#               __/ |                    
#              |___/

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"],
	 border_width_focus=2,
	 border_focus = "#8caaee", # "#df8e1d" ← Orange "#8caaee" ← blue
	 border_normal = "#5c5f77", #"#5c5f77" ← dark grey "#7287fd" ←leight grey
	 margin = 3,
	 border_on_single = True,
	 ),
    layout.Max(	 
	 border_width=2,
	 border_focus = "#8caaee",
	 border_normal = "#8caaee",
	 margin = 3,
	 border_on_single = True,
	),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



# __          ___     _            _       
# \ \        / (_)   | |          | |      
#  \ \  /\  / / _  __| | __ _  ___| |_ ___ 
#   \ \/  \/ / | |/ _` |/ _` |/ _ \ __/ __|
#    \  /\  /  | | (_| | (_| |  __/ |_\__ \
#     \/  \/   |_|\__,_|\__, |\___|\__|___/
#                        __/ |             
#                       |___/              

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.GroupBox(
					highlight_color = c_frappe.get("pink"), #["#8839ef","#8839ef"]
					background = c_frappe.get("red"), #bf616a
                    inactive = c_frappe.get("bg"),
                    active = c_frappe.get("dark_red"),
					highlight_method = 'line',
                    block_highlight_text_color=c_frappe.get("bg"),
					disable_drag = True,
				),

                left_arrow(c_frappe.get("red"), c_frappe.get("yellow")),

                widget.CurrentLayout(
                    background=c_frappe.get("yellow"),
                    foreground=c_frappe.get("bg"),
                    font = "bold",
                    ),

                left_arrow(c_frappe.get("yellow"), c_frappe.get("window")),

				widget.Spacer(
					length = 7,
                    background = c_frappe.get("window")
				),
                #widget.Prompt(),
                widget.WindowName(
					background = c_frappe.get("window"), #"#2e3440"
					foreground = c_frappe.get("fg"), #"#b4befe"
                    font = "italic",
				),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                left_arrow(c_frappe.get("window"), c_frappe.get("lavender")),

                widget.Memory(
                    format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                    background=c_frappe.get("lavender"),
                    foreground=c_frappe.get("bg"),
                    ),

                left_arrow(c_frappe.get("lavender"), c_frappe.get("blue")),

                widget.Systray(
                    background = c_frappe.get("blue"), #a3be8c
                    ),
        
                left_arrow(c_frappe.get("blue"), c_frappe.get("green")),

                widget.Clock(
                    background = c_frappe.get("green"), #b48ead
                    foreground = c_frappe.get("bg"),
                    format="🕑 %Y-%m-%d %a %I:%M %p"
                ),
                #widget.QuickExit(),
            ],
            18, # 24 default
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#                _            _             _   
#     /\        | |          | |           | |  
#    /  \  _   _| |_ ___  ___| |_ __ _ _ __| |_ 
#   / /\ \| | | | __/ _ \/ __| __/ _` | '__| __|
#  / ____ \ |_| | || (_) \__ \ || (_| | |  | |_ 
# /_/    \_\__,_|\__\___/|___/\__\__,_|_|   \__|
                                               

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None



# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



