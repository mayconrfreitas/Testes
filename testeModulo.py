# -*- coding: utf-8 -*-

#Criado por Maycon Freitas
#www.linkedin.com/in/maycon-freitas-274a9a83/
#mayconrfreitas@gmail.com
#@ihavebim

#Bibliotecas
import System
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import clr
import os
import webbrowser
import unicodedata
import io
import tempfile
import math
import traceback
import json
import datetime
import hashlib
import collections
import itertools
#from collections import OrderedDict

clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
from Revit.Elements import *
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *

clr.AddReference("System.Drawing")
from System.Drawing import *

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument

#Função de teste 
def HelloWorld():
	TaskDialog.Show("Teste", "Hello World!")
