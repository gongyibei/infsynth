from .analog import DC
from .basic import Sin, Square, Saw


def SinMod(freq): return (Sin(freq) + DC(1)) * DC(0.5)
def SquareMod(freq): return (Square(freq) + DC(1)) * DC(0.5)
def SawMod(freq): return (Saw(freq) + DC(1)) * DC(0.5)
