import pytest
import os.path

def test_model_file():
    flag = False
    for root, dir, files in os.walk("C:"):
        if "model.hdf5" in files:
            flag = True
    assert flag == True, "model.hdf5 file is not found"

def test_labels_file():
    flag = False
    for root, dir, files in os.walk("C:"):
        if "labels.dat" in files:
            flag = True
    assert flag == True, "labels.dat file is not found"