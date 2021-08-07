from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        empty = NodePath("empty")

      
