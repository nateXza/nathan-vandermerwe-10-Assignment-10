from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacOSGUIFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

class WindowsButton:
    def render(self):
        print("Rendering a Windows button")

class MacOSButton:
    def render(self):
        print("Rendering a MacOS button")