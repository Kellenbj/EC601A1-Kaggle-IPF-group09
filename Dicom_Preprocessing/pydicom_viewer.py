import pydicom as dicom

import matplotlib.pyplot as plt
filename = "C:\\Users\\Poras\\Desktop\\dicom_image_set\\dicom images for testing\\1-051.dcm"
dataset=dicom.read_file(filename)

print(dataset)

print(dataset.pixel_array)
print("Rows",dataset.Rows)
print("Columns",dataset.Columns)

