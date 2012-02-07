from gi.repository import Gtk, GdkPixbuf, Nautilus, GObject

class Emblems(GObject.GObject, Nautilus.PropertyPageProvider):
    def __init__(self):
        pass

    def get_property_pages(self, files):
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
        self.icon_view.set_selection_mode(Gtk.SelectionMode.MULTIPLE)
        self.icon_view.show()

        scroll = Gtk.ScrolledWindow()
        scroll.add(self.icon_view)
        scroll.show()

        return Nautilus.PropertyPage(name="NautilusPython::emblems",
                                     label=property_label,
                                     page=scroll),

    def connect_signals(self):
        self.icon_view.connect('activate-cursor-item', self.test)
        self.icon_view.connect('item-activated', self.test)
        self.icon_view.connect('move-cursor', self.test)
        self.icon_view.connect('select-cursor-item', self.test)
        self.icon_view.connect('selection-changed', self.test)
        self.icon_view.connect('toggle-cursor-item', self.test)
        self.icon_view.connect('unselect-all', self.test)

    def test(self, *args, **kwargs):
        print 'crap'

    def on_emblem_selected(self, widget, item):
        print self.icon_view.get_model()[item][2]

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
