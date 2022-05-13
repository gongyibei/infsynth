from pynput import keyboard

from .module import Module


class KeyboardSource(Module):

    def __init__(self, key):
        Module.__init__(self)
        self.key = keyboard.KeyCode.from_char(key)
        self._init_keyboard()
        self.gate = 0

    def _init_keyboard(self):
        keyboard.Listener(on_press=self._on_press,
                          on_release=self._on_release).start()

    def _on_press(self, key):
        if key == self.key:
            # print('Alphanumeric key pressed: {0} '.format( key.char))
            self.gate = 1

    def _on_release(self, key):
        if key == self.key:
            # print('Key released: {0}'.format(key))
            self.gate = 0

    def forward(self):
        return self.gate