FROM tensorflow/tensorflow:latest-gpu-jupyter

RUN apt-get update && apt-get install libgl1 -y

RUN python -m pip install --upgrade pip
RUN pip install pandas rasterio geopandas scikit-learn albumentations opencv-python
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]