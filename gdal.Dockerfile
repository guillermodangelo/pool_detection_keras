FROM andrejreznik/python-gdal:stable

RUN python -m pip install --upgrade pip
RUN pip install splitraster geotile
RUN pip install jupyter

# Run Jupyter Notebook when the container launches
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]