FROM tensorflow/tensorflow:2.2.2-gpu-py3-jupyter
RUN python -m pip install --upgrade pip
RUN pip install pandas rasterio