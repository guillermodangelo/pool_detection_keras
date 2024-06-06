FROM tensorflow/tensorflow:latest-gpu-jupyter

RUN python -m pip install --upgrade pip
RUN pip install pandas rasterio geopandas