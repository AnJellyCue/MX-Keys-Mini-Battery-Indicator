#!/usr/bin/env python3

import subprocess
import gi
import os

gi.require_version("Gtk", "3.0")
gi.require_version("AyatanaAppIndicator3", "0.1")

from gi.repository import Gtk, AyatanaAppIndicator3

DEVICE_PATH = "/org/bluez/hci0/dev_D9_42_C6_BE_74_56"
ICON = os.path.expanduser("~/mx-keys-battery/icons/keyboard.svg")


def get_battery():
    try:
        result = subprocess.run(
            [
                "busctl", "get-property",
                "org.bluez",
                DEVICE_PATH,
                "org.bluez.Battery1",
                "Percentage",
            ],
            capture_output=True,
            text=True,
            timeout=3,
        )

        if result.returncode == 0:
            return int(result.stdout.strip().split()[-1])

    except Exception:
        pass

    return None


def update():
    battery = get_battery()

    if battery is None:
        battery_label.set_label("Battery: unavailable")
        indicator.set_label("?", "")
        return

    battery_label.set_label(f"Battery: {battery}%")
    indicator.set_label(str(battery), "")
    indicator.set_icon_full(ICON, "MX Keys Mini")


def refresh(_widget=None):
    update()


indicator = AyatanaAppIndicator3.Indicator.new(
    "mx-keys-mini-battery",
    ICON,
    AyatanaAppIndicator3.IndicatorCategory.HARDWARE,
)

indicator.set_status(
    AyatanaAppIndicator3.IndicatorStatus.ACTIVE
)

indicator.set_title("MX Keys Mini")


menu = Gtk.Menu()

title = Gtk.MenuItem(label="⌨️ MX Keys Mini")
title.set_sensitive(False)
menu.append(title)

battery_label = Gtk.MenuItem(label="Battery: checking…")
battery_label.set_sensitive(False)
menu.append(battery_label)

menu.append(Gtk.SeparatorMenuItem())

refresh_item = Gtk.MenuItem(label="Refresh")
refresh_item.connect("activate", refresh)
menu.append(refresh_item)

quit_item = Gtk.MenuItem(label="Quit")
quit_item.connect("activate", Gtk.main_quit)
menu.append(quit_item)

menu.show_all()

indicator.set_menu(menu)

update()

GLib_TIMEOUT = 60
from gi.repository import GLib
GLib.timeout_add_seconds(GLib_TIMEOUT, update)

Gtk.main()
