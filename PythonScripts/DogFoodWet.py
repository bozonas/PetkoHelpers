# -*- coding: utf-8 -*-
import DownloadImage
from Core import Core
import csv


if __name__ == "__main__":

    itemDownloader = DownloadImage.ItemDownload("C:\Users\AGNIUS\Desktop\prestashop\Prekes",
                                                "prekes_sunys_slapias_maistas.csv", withFeatures=True)

    itemDownloader.importProducts(uniqueCode='dog_wet_food',
    urlList=[
        {'url': 'http://zoofast.lt/slapiasmaistas-suniukai-c-23_201_203_266_267.html', 'attribute': {'Sudėtis': ''}}
        ],
    category='Šunys,Maistas,Konservai,Jauniems šuniukams'
    )
    itemDownloader.importProducts(uniqueCode='dog_wet_food',
    urlList=[
        {'url': 'http://zoofast.lt/slapiasmaistas-suaugesunys-c-23_201_203_266_268.html', 'attribute': {'Sudėtis': ''}},
        {'url': 'http://zoofast.lt/-c-23_201_203_266_268.html?page=6', 'attribute': {'Sudėtis': ''}},
        {'url': 'http://zoofast.lt/-c-23_201_203_266_268.html?page=11', 'attribute': {'Sudėtis': ''}}
        ],
    category='Šunys,Maistas,Konservai,Suaugusiems šunims'
    )
    itemDownloader.importProducts(uniqueCode='dog_wet_food',
    urlList=[
        {'url': 'http://zoofast.lt/slapiasmaistas-senyvoamziaussunys-c-23_201_203_266_269.html', 'attribute': {'Sudėtis': ''}}
        ],
    category='Šunys,Maistas,Konservai,Vyresnio amžiaus šunims'
    )