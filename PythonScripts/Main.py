# -*- coding: utf-8 -*-
import DownloadImage
from Core import Core
import csv


if __name__ == "__main__":

    itemDownloader = DownloadImage.ItemDownload("C:\Users\AGNIUS\Desktop\prestashop\Prekes", "prekes.csv")
    Core.removeDublicate("C:\Users\AGNIUS\Desktop\prestashop\Prekes\prekes.csv",
                         "C:\Users\AGNIUS\Desktop\prestashop\Prekes\prekes_filtered.csv")








    ############################## Template ###################################
    # itemDownloader.importProducts(
    #     urlList=[
    #         {'url': 'http://zoofast.lt/mazuveisliusuniukai-maistassuvistiena-c-23_201_202_205_206_215.html',
    #          'attribute': {'Sudėtis': 'Kitokių skonių maistas'}}
    #         ],
    #     category='Šunys,Maistas,Sausas maistas,Mažų veislių šunims,Jauniems šuniukams'
    # )
    ##########################################################################

    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/mazuveisliusuniukai-kituskoniumaistas-c-23_201_202_205_206_217.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/mazuveisliusuniukai-maistassuerienairryziais-c-23_201_202_205_206_216.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/mazuveisliusuniukai-maistassuvistiena-c-23_201_202_205_206_215.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Mažų veislių šunims,Jauniems šuniukams'
    # )
    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/mazuveisliusuaugesunys-maistasnutukusiemssunimslight-c-23_201_202_205_209_227.html', 'attribute': {'Specializuota mityba': 'Maistas nutukusiems'}},
    #     {'url': 'http://zoofast.lt/mazuveisliusuaugesunys-energetinismaistas-c-23_201_202_205_209_228.html', 'attribute': {'Specializuota mityba': 'Energetinis maistas'}},
    #     {'url': 'http://zoofast.lt/mazuveisliusuaugesunys-kituskoniumaistas-c-23_201_202_205_209_226.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/mazuveisliusuaugesunys-maistassuerienairryziais-c-23_201_202_205_209_225.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/mazuveisliusuaugesunys-maistassuvistiena-c-23_201_202_205_209_224.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Mažų veislių šunims,Suaugusiems šunims'
    # )
    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/mazuveisliuvyresnioamziaussunys-maistasnutukusiemssunimslight-c-23_201_202_205_212_242.html', 'attribute': {'Specializuota mityba': 'Maistas nutukusiems'}},
    #     {'url': 'http://zoofast.lt/mazuveisliuvyresnioamziaussunys-kituskoniumaistas-c-23_201_202_205_212_241.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/mazuveisliuvyresnioamziaussunys-maistassueriena-c-23_201_202_205_212_240.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/mazuveisliuvyresnioamziaussunys-maistassuvistiena-c-23_201_202_205_212_239.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Mažų veislių šunims,Vyresniems šunims'
    # )



    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuniukai-kituskoniumaistas-c-23_201_202_205_207_220.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuniukai-maistassuerienairryziais-c-23_201_202_205_207_219.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuniukai-maistassuvistiena-c-23_201_202_205_207_218.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Vidutinių veislių šunims,Jauniems šuniukams'
    # )
    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuaugesunys-maistasnutukusiemssunimslight-c-23_201_202_205_210_232.html', 'attribute': {'Specializuota mityba': 'Maistas nutukusiems'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuaugesunys-maistassterilizuotiemssunims-c-23_201_202_205_210_422.html', 'attribute': {'Specializuota mityba': 'Sterilizuotiems/kastruotiems'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuaugesunys-energetinismaistas-c-23_201_202_205_210_233.html', 'attribute': {'Specializuota mityba': 'Energetinis maistas'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuaugesunys-kituskoniumaistas-c-23_201_202_205_210_231.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuaugesunys-maistassueriena-c-23_201_202_205_210_230.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliusuaugesunys-maistassuvistiena-c-23_201_202_205_210_229.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Vidutinių veislių šunims,Suaugusiems šunims'
    # )
    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/vidutiniuveisliuvyresnioamziaussunys-maistasnutukusiemssunimslight-c-23_201_202_205_213_246.html', 'attribute': {'Specializuota mityba': 'Maistas nutukusiems'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliuvyresnioamziaussunys-kituskoniumaistas-c-23_201_202_205_213_245.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliuvyresnioamziaussunys-maistassueriena-c-23_201_202_205_213_244.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/vidutiniuveisliuvyresnioamziaussunys-maistassuvistiena-c-23_201_202_205_213_243.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Vidutinių veislių šunims,Vyresniems šunims'
    # )


    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusuniukai-kituskoniumaistas-c-23_201_202_205_208_223.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusuniukai-maistassuerienairryziais-c-23_201_202_205_208_222.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusuniukai-maistassuvistiena-c-23_201_202_205_208_221.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Didelių veislių šunims,Jauniems šuniukams'
    # )
    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusubrendesunys-maistasnutukusiemssunimslight-c-23_201_202_205_211_237.html', 'attribute': {'Specializuota mityba': 'Maistas nutukusiems'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusubrendesunys-maistassterilizuotiemssunims-c-23_201_202_205_211_423.html', 'attribute': {'Specializuota mityba': 'Sterilizuotiems/kastruotiems'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusubrendesunys-energetinismaistas-c-23_201_202_205_211_238.html', 'attribute': {'Specializuota mityba': 'Energetinis maistas'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusubrendesunys-kituskoniumaistas-c-23_201_202_205_211_236.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusubrendesunys-maistassueriena-c-23_201_202_205_211_235.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliusubrendesunys-maistassuvistiena-c-23_201_202_205_211_234.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Didelių veislių šunims,Suaugusiems šunims'
    # )
    # itemDownloader.importProducts(
    # urlList=[
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliuvyresnioamiaussunys-maistasnutukusiemssunimslight-c-23_201_202_205_214_250.html', 'attribute': {'Specializuota mityba': 'Maistas nutukusiems'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliuvyresnioamiaussunys-kituskoniumaistas-c-23_201_202_205_214_249.html', 'attribute': {'Sudėtis': 'Kitokio skonio'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliuvyresnioamiaussunys-maistassueriena-c-23_201_202_205_214_248.html', 'attribute': {'Sudėtis': 'Ėriena'}},
    #     {'url': 'http://zoofast.lt/dideliuirlabaidideliuveisliuvyresnioamiaussunys-maistassuvistiena-c-23_201_202_205_214_247.html', 'attribute': {'Sudėtis': 'Paukštiena'}}
    #     ],
    # category='Šunys,Maistas,Sausas maistas,Didelių veislių šunims,Vyresniems šunims'
    # )



