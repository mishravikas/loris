# -*- coding: utf-8 -*-
import os
from django.db import models

def get_path(self,filename):
	# print filename
	ext=filename.split('.')[1]
	ext='input_'+ext
	return os.path.join(ext,filename)

class Document(models.Model):
    docfile = models.FileField(upload_to=get_path)
