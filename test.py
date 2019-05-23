#!/usr/bin/python
# -*- coding: UTF-8 -*-

import nibabel as nib
import numpy as np

filename = "test.nii"
data = nib.load(filename).get_fdata()
print(data.shape)
