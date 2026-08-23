# ui.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerMenu, MDNavigationDrawerItem
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.metrics import dp, sp
from kivy.core.window import Window
from config import COLORS

Window.size = (360, 780) # Mobile size simulation

class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = COLORS["bg_dark"]
        self.add_widget(self.build_dashboard())

    def build_dashboard(self):
        layout = MDBoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Header
        header = MDFloatLayout(size_hint_y=0.1)
        header.add_widget(MDLabel(text="Sonryan AI Trading", font_style="H5", theme_text_color="Custom", text_color=COLORS["text_primary"], pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        layout.add_widget(header)

        # KSE-100 Card
        kse_card = MDCard(size_hint_y=0.25, radius=[dp(15)], md_bg_color=COLORS["card_dark"])
        kse_layout = MDBoxLayout(orientation='vertical', padding=dp(15))
        kse_layout.add_widget(MDLabel(text="KSE-100 INDEX", font_style="Caption", theme_text_color="Custom", text_color=COLORS["text_secondary"]))
        kse_layout.add_widget(MDLabel(text="113,256.74", font_style="H4", theme_text_color="Custom", text_color=COLORS["text_primary"]))
        kse_layout.add_widget(MDLabel(text="+612.35 (+0.54%) ▲", font_style="H6", theme_text_color="Custom", text_color=COLORS["green"]))
        kse_card.add_widget(kse_layout)
        layout.add_widget(kse_card)

        # Strategy Cards (Intraday, Swing, Long-Term, 5X)
        strategy_grid = MDGridLayout(cols=2, size_hint_y=0.4, spacing=dp(10))
        strategies = [
            ("INTRADAY", "Top 5 Opportunities", COLORS["green"]),
            ("SWING", "Top 5 Opportunities", COLORS["blue"]),
            ("LONG-TERM", "Top 5 Opportunities", COLORS["purple"]),
            ("5X WATCH", "High Conviction", COLORS["orange"])
        ]
        for title, sub, color in strategies:
            card = MDCard(radius=[dp(10)], md_bg_color=COLORS["card_dark"])
            card_layout = MDBoxLayout(orientation='vertical', padding=dp(10))
            card_layout.add_widget(MDLabel(text=title, font_style="Caption", theme_text_color="Custom", text_color=color))
            card_layout.add_widget(MDLabel(text=sub, font_style="Caption", theme_text_color="Custom", text_color=COLORS["text_secondary"]))
            # Mock Data Table
            card_layout.add_widget(MDLabel(text="1. LUCK  445.20  +7.65% ▲", font_style="Caption", theme_text_color="Custom", text_color=COLORS["text_primary"]))
            card_layout.add_widget(MDLabel(text="2. ATRL  940.05  +6.12% ▲", font_style="Caption", theme_text_color="Custom", text_color=COLORS["text_primary"]))
            card.add_widget(card_layout)
            strategy_grid.add_widget(card)
        layout.add_widget(strategy_grid)

        # Bottom Navigation
        bottom_nav = MDBottomNavigation()
        items = [
            ("Scanners", "radar"), ("Watchlist", "star"), ("Alerts", "bell"),
            ("News & Macro", "newspaper"), ("Portfolio", "briefcase"), ("AI Insights", "brain")
        ]
        for text, icon in items:
            item = MDBottomNavigationItem(text=text, icon=icon)
            item.add_widget(MDLabel(text=f"{text} Screen", halign="center"))
            bottom_nav.add_widget(item)
        layout.add_widget(bottom_nav)

        return layout

class MarketOverviewScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = COLORS["bg_dark"]
        self.add_widget(MDLabel(text="Market Overview", pos_hint={'center_x': 0.5, 'center_y': 0.9}, font_style="H5", theme_text_color="Custom", text_color=COLORS["text_primary"]))

class SidebarContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical')
        menu = MDNavigationDrawerMenu()
        items = ["Market Overview", "Watchlist", "Portfolio", "News & Research", "Sectors & Industries", "Strategy Builder", "AI Insights", "Reports", "Settings", "Help & Support"]
        for item in items:
            menu.add_widget(MDNavigationDrawerItem(text=item, icon="menu"))
        self.add_widget(menu)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        
        self.sm = MDScreenManager()
        self.sm.add_widget(DashboardScreen(name='dashboard'))
        self.sm.add_widget(MarketOverviewScreen(name='market_overview'))
        
        # Navigation Drawer
        self.nav_drawer = MDNavigationDrawer()
        self.nav_drawer.add_widget(SidebarContent())
        
        return self.sm

if __name__ == '__main__':
    MainApp().run()