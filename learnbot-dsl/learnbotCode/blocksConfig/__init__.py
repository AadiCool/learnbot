import inspect
import os
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

from blocks import pathBlocks

from parserConfigBlock import *
__all__ = ["configBlocks", "pathImgBlocks"]

functions = parserConfigBlock(path+"/configFuntions")
functions += parserConfigBlock(path+"/configControl")
functions += parserConfigBlock(path+"/configPerceptual")
functions += parserConfigBlock(path+"/configPropiopercetive")
functions += parserConfigBlock(path+"/configOperators")

for f in functions:
    for i in range(len(f[1]["img"])):
        f[1]["img"][i] = pathBlocks + "/" +f[1]["img"][i]

configBlocks = functions
pathImgBlocks = pathBlocks