# DFF -- An Open Source Digital Forensics Framework
# Copyright (C) 2009-2011 ArxSys
# This program is free software, distributed under the terms of
# the GNU General Public License Version 2. See the LICENSE file
# at the top of the source tree.
#  
# See http://www.digital-forensic.org for more information about this
# project. Please do not directly contact any of the maintainers of
# DFF for assistance; the project provides a web site, mailing lists
# and IRC channels for your use.
# 
# Author(s):
#  Frederic Baguelin <fba@digital-forensic.org>

__dff_module_cat_version__ = "1.0.0"

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget, QImage, QHBoxLayout, QLabel, QPixmap

import popplerqt4

from api.module.module import Module
from api.module.script import Script
from api.types.libtypes import Argument, typeId


class PDF(QWidget, Script):
  def __init__(self):
    Script.__init__(self, "pdf")
    self.type = "pdfviewer"
    
  def updateWidget(self):
    pass
  
  def start(self, args):
    self.args = args
    try:
      self.node = args["file"].value()
      f = self.node.open()
      buff = f.read()
      f.close()
      self.document = popplerqt4.Poppler.Document.loadFromData(buff)
    except:
      pass

  def g_display(self):
    QWidget.__init__(self)
    self.hbox = QHBoxLayout()
    self.hbox.setContentsMargins(0, 0, 0, 0)
    pdfPage = self.document.page(1)
    image = pdfPage.renderToImage()
    label = QLabel()
    label.setPixmap(QPixmap.fromImage(image))
    self.hbox.addWidget(label)
    self.setLayout(self.hbox)
      


class pdf(Module):
  """Show first page of a pdf file"""
  def __init__(self):
    Module.__init__(self, "pdf", PDF)
    self.conf.addArgument({"name": "file",
                           "description": "Pdf file to display",
                           "input": Argument.Required|Argument.Single|typeId.Node})
    self.conf.addConstant({"name": "mime-type", 
 	                   "type": typeId.String,
 	                   "description": "managed mime type",
 	                   "values": ["PDF"]})
    self.tags = "Viewers"
    self.flags = ["gui"]
    self.icon = ":text"	
