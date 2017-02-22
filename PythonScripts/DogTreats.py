# -*- coding: utf-8 -*-
import DownloadImage
from Core import Core
import csv


if __name__ == "__main__":

    # Skanestai
    itemDownloader = DownloadImage.ItemDownload("C:\Users\AGNIUS\Desktop\prestashop\Prekes",
                                                "prekes_sunys_visos_prekes.csv", withFeatures=True)
    # itemDownloader.importProducts(uniqueCode='dog_treats',
    # urlList=[
    #     {'url': 'http://zoofast.lt/sunys-skanestaisunims-c-23_76.html', 'attribute': {'': ''}},
    #     {'url': 'http://zoofast.lt/-c-23_76.html?page=6', 'attribute': {'': ''}},
    #     {'url': 'http://zoofast.lt/-c-23_76.html?page=11', 'attribute': {'': ''}}
    #     ],
    # category='Šunys,Maistas,Skanėstai'
    # )

    # Vitaminai ir papildai
    itemDownloader.importProducts(uniqueCode='dog_vitamins',
    urlList=[
        {'url': 'http://zoofast.lt/sunys-vitaminai-c-23_47.html', 'attribute': {'': ''}},
        {'url': 'http://zoofast.lt/-c-23_47.html?page=6', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Vitaminai ir papildai'
    )

    # Priežiūros priemonės)
    itemDownloader.importProducts(uniqueCode='dog_hygiene',
    urlList=[
        {'url': 'http://zoofast.lt/higienosirprieziurospriemones-sampunaiirkondicionieriai-c-23_49_105.html', 'attribute': {'': ''}},
        {'url': 'http://zoofast.lt/higienosirprieziurospriemonesSampunaiirkondicionieriai-c-23_49_105.html?page=6', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Priežiūros priemonės,Šampūnai ir kondicionieriai'
    )
    itemDownloader.importProducts(uniqueCode='dog_hygiene',
    urlList=[
        {'url': 'http://zoofast.lt/higienosirprieziurospriemones-burnosprieziura-c-23_49_103.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Priežiūros priemonės,Burnos priežiūra'
    )
    itemDownloader.importProducts(uniqueCode='dog_hygiene',
    urlList=[
        {'url': 'http://zoofast.lt/higienosirprieziurospriemones-akiuirausuprieziura-c-23_49_104.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Priežiūros priemonės,Akių ir ausų priežiūra'
    )
    itemDownloader.importProducts(uniqueCode='dog_hygiene',
    urlList=[
        {'url': 'http://zoofast.lt/sunys-preparatainuoparazitu-c-23_61.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Priežiūros priemonės,Antiparazitinės priemonės'
    )
    itemDownloader.importProducts(uniqueCode='dog_hygiene',
    urlList=[
        {'url': 'http://zoofast.lt/priedai-sepeciaiirsukos-c-23_44_93.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Priežiūros priemonės,Šepečiai ir šukos'
    )
    itemDownloader.importProducts(uniqueCode='dog_hygiene',
    urlList=[
        {'url': 'http://zoofast.lt/higienosirprieziurospriemones-kitoshigienosirprieziurospriemones-c-23_49_106.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Priežiūros priemonės,Kitos priemonės'
    )


    # Žaislai
    itemDownloader.importProducts(uniqueCode='dog_toys',
    urlList=[
        {'url': 'http://zoofast.lt/sunys-zaislai-c-23_95.html', 'attribute': {'': ''}},
        {'url': 'http://zoofast.lt/SunysZaislai-c-23_95.html?page=6', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Žaislai'
    )

    # Kiti produktai
    itemDownloader.importProducts(uniqueCode='dog_other',
    urlList=[
        {'url': 'http://zoofast.lt/priedai-dresurospriemones-c-23_44_405.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Kiti produktai,Dresūros priemonės'
    )
    itemDownloader.importProducts(uniqueCode='dog_other',
    urlList=[
        {'url': 'http://zoofast.lt/priedai-dubeneliaiirstovai-c-23_44_131.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Kiti produktai,Dubenėliai'
    )
    itemDownloader.importProducts(uniqueCode='dog_other',
    urlList=[
        {'url': 'http://zoofast.lt/priedai-antsnukiai-c-23_44_146.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Kiti produktai,Atsnukiai'
    )
    itemDownloader.importProducts(uniqueCode='dog_other',
    urlList=[
        {'url': 'http://zoofast.lt/priedai-antkakliai-c-23_44_129.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Kiti produktai,Antkakliai'
    )
    itemDownloader.importProducts(uniqueCode='dog_other',
    urlList=[
        {'url': 'http://zoofast.lt/priedai-pavadeliai-c-23_44_130.html', 'attribute': {'': ''}},
        {'url': 'http://zoofast.lt/priedaipavadeliai-c-23_44_130.html?page=6', 'attribute': {'': ''}},
        {'url': 'http://zoofast.lt/priedai-petnesos-c-23_44_133.html', 'attribute': {'': ''}}
        ],
    category='Šunys,Maistas,Kiti produktai,Pavadėliai'
    )
