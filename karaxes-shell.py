
#!/usr/bin/env python3

import datetime
import platform
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib, Gdk

CSS = """
window {
    background: #090a0e;
    color: #eeeeF2;
}
.topbar {
    background: #12151b;
    padding: 14px 20px;
    border-bottom: 1px solid #383d48;
}
.brand {
    font-weight: 900;
    letter-spacing: 4px;
    font-size: 20px;
}
.red {
    color: #d02b3d;
    font-weight: 900;
}
.muted {
    color: #a3a8b2;
}
.card {
    background: #171b23;
    border: 1px solid #363c48;
    border-radius: 14px;
    padding: 20px;
}
.card-title {
    font-size: 18px;
    font-weight: 800;
}
button {
    background: #222833;
    color: #f2f2f4;
    border: 1px solid #444b59;
    border-radius: 10px;
    padding: 12px;
}
button:hover {
    background: #343c49;
    border-color: #c52c3c;
}
"""

class KaraxesApp(Gtk.Application):

    def __init__(self):
        super().__init__(
            application_id="org.karaxes.shell"
        )

    def do_activate(self):

        provider = Gtk.CssProvider()
        provider.load_from_data(CSS.encode())

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.window = Gtk.ApplicationWindow(
            application=self,
            title="KARAXES OS X6"
        )

        self.window.set_default_size(1200, 760)

        root = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=0
        )

        self.window.set_child(root)

        bar = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=12
        )

        bar.add_css_class("topbar")

        logo = Gtk.Label(label="KARAXES")
        logo.add_css_class("brand")

        version = Gtk.Label(label="X6")
        version.add_css_class("red")

        bar.append(logo)
        bar.append(version)

        spacer = Gtk.Box()
        spacer.set_hexpand(True)
        bar.append(spacer)

        self.clock = Gtk.Label()
        bar.append(self.clock)

        root.append(bar)

        GLib.timeout_add_seconds(1, self.update_clock)
        self.update_clock()

        main = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=20
        )

        main.set_margin_top(22)
        main.set_margin_bottom(22)
        main.set_margin_start(22)
        main.set_margin_end(22)

        root.append(main)

        dock = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12
        )

        dock.set_size_request(75, -1)

        for symbol, name in [
            ("⌂", "Home"),
            ("▦", "Applications"),
            ("⚙", "Control Center"),
            ("ⓘ", "System Information")
        ]:

            button = Gtk.Button(label=symbol)
            button.set_size_request(58, 58)
            button.set_tooltip_text(name)
            button.connect(
                "clicked",
                self.show_notice,
                name
            )

            dock.append(button)

        main.append(dock)

        page = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=18
        )

        page.set_hexpand(True)
        main.append(page)

        heading = Gtk.Label(
            label="Բարի գալուստ KARAXES"
        )

        heading.set_xalign(0)
        heading.add_css_class("card-title")
        page.append(heading)

        subtitle = Gtk.Label(
            label="YOUR SYSTEM. YOUR POWER."
        )

        subtitle.set_xalign(0)
        subtitle.add_css_class("muted")
        page.append(subtitle)

        grid = Gtk.Grid(
            column_spacing=16,
            row_spacing=16
        )

        grid.set_column_homogeneous(True)
        page.append(grid)

        self.add_card(
            grid,
            "CONTROL CENTER",
            "Hardware Manager\n"
            "Driver Manager\n"
            "Performance Manager\n"
            "Network & Wi-Fi\n"
            "Display & Sound",
            0, 0
        )

        self.add_card(
            grid,
            "SYSTEM MONITOR",
            f"System: {platform.system()}\n"
            f"Version: {platform.release()}\n"
            f"Architecture: {platform.machine()}",
            1, 0
        )

        self.add_card(
            grid,
            "QUICK SETTINGS",
            "Network control: Pending integration\n"
            "Audio control: Pending integration\n"
            "Display control: Pending integration",
            0, 1
        )

        self.add_card(
            grid,
            "GAME CENTER",
            "Game library\n"
            "Installation manager\n"
            "Compatibility information\n"
            "Save backup system",
            1, 1
        )

        self.window.present()

    def update_clock(self):

        self.clock.set_text(
            datetime.datetime.now().strftime(
                "%d.%m.%Y   %H:%M:%S"
            )
        )

        return GLib.SOURCE_CONTINUE

    def add_card(self, grid, title, body, col, row):

        card = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=14
        )

        card.add_css_class("card")

        title_label = Gtk.Label(label=title)
        title_label.set_xalign(0)
        title_label.add_css_class("card-title")

        body_label = Gtk.Label(label=body)
        body_label.set_xalign(0)
        body_label.set_wrap(True)
        body_label.add_css_class("muted")

        card.append(title_label)
        card.append(body_label)

        grid.attach(card, col, row, 1, 1)

    def show_notice(self, button, name):

        dialog = Gtk.AlertDialog()
        dialog.set_message(name)
        dialog.set_detail(
            "KARAXES X6 module. "
            "System integration is pending."
        )

        dialog.show(self.window)


if __name__ == "__main__":

    KaraxesApp().run()
