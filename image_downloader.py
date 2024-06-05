import pandas as pd
import requests
import os


def im_image_downloader(
        img_name: str,
        url_base: str = 'https://intgis.montevideo.gub.uy/sit/mapserv/data/fotos_2021/',
        outputpath: str = 'images/') -> None:
    'Download images AOI'

    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    url = f'{url_base}{img_name}.jpg'
    url_ref = f'{url_base}{img_name}.jgw'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    response = requests.get(url, headers=headers)

    if response.ok:
        output_filename = f'{outputpath}{img_name}.jpg'
        with open(output_filename, 'wb') as f:
            f.write(response.content)
    else:
        print(response, img_name)

    response = requests.get(url_ref, headers=headers)

    if response.ok:
        output_filename = f'{outputpath}{img_name}.jgw'
        with open(output_filename, 'wb') as f:
            f.write(response.content)
        print(f'Image {img_name} was downloaded successfully.')
    else:
        print(response, img_name)


def download_images(
        images_csv: str = 'images_aoi.csv',
        outputpath: str = 'images/') -> None:
    'Download images AOI'

    img_list = list(pd.read_csv(images_csv)['HOJA'])
    for img in img_list:
        im_image_downloader(img, outputpath=outputpath)


if __name__ == "__main__":
    download_images()