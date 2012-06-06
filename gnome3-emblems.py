import os
from gi.repository import Gtk, GdkPixbuf, Nautilus, GObject


class Emblems(GObject.GObject, Nautilus.PropertyPageProvider):
    def __init__(self):
        pass

    def get_property_pages(self, files):
        self.files = files
        actual_emblems = self.get_actual_emblems(files)
        property_page = self.create_property_page()
        self.fill_emblems(actual_emblems)
        self.connect_signals()
        return property_page

    def create_property_page(self):
        property_label = Gtk.Label('Emblems')
        property_label.show()

        # Save the icon, name & full-name
        self.list_store = Gtk.ListStore(GdkPixbuf.Pixbuf, str, str)

        self.icon_view = Gtk.IconView()
        self.icon_view.set_model(self.list_store)
        self.icon_view.set_pixbuf_column(0)
        self.icon_view.set_text_column(1)
        #self.icon_view.set_selection_mode(Gtk.SelectionMode.MULTIPLE)
        self.icon_view.show()

        scroll = Gtk.ScrolledWindow()
        scroll.add(self.icon_view)
        scroll.show()

        return Nautilus.PropertyPage(name="NautilusPython::emblems",
                                     label=property_label,
                                     page=scroll),

    def connect_signals(self):
        self.icon_view.connect('selection-changed', self.on_selection_changed)

    def on_selection_changed(self, widget):
        for file in self.files:
            partial_cmd = 'gvfs-set-attribute "%s" -t' % file.get_uri()
            # Clear previous emblems
            os.system('%s unset metadata::emblems' % partial_cmd)
            # Add new emblems
            emblem = ''.join([widget.get_model()[item][2]
                              for item in widget.get_selected_items()])
            os.system('%s stringv metadata::emblems %s' % (partial_cmd, emblem))
            # The add_emblem is called too to see the emblem just in the
            # moment, if not, a nautilus refresh will be needed
            file.add_emblem(emblem)

    def get_actual_emblems(self, files):
        return []

    @staticmethod
    def get_icon_name(name):
        '''Returns the name human readable.

        >>> Emblems.get_icon_name('emblem-test-name-emblem')
        Test name
        '''
        name = name.replace('-emblem', '')
        name = name.replace('emblem-', '')
        name = name.replace('-', ' ')
        return name[0].upper() + name[1:]

    def fill_emblems(self, actual_emblems):
        '''Fill the listore with the proper icons.
        '''
        theme = Gtk.IconTheme.get_default()
        icons = theme.list_icons(None)
        for icon in icons:
            if 'emblem' in icon:
                pixbuf = theme.load_icon(icon, 48, 0)
                self.list_store.append([pixbuf, self.get_icon_name(icon), icon])
