# -*- coding: utf-8 -*-

from tqdm import tqdm
from pyquery import PyQuery as pq
import urllib
import csv
import re
from Core import Core


import sys
reload(sys)
sys.setdefaultencoding('utf8')


class ItemDownload:

    table = {
        ord(u'Ą'): u'A',
        ord(u'ą'): u'a',
        ord(u'Č'): u'C',
        ord(u'č'): u'c',
        ord(u'Ę'): u'E',
        ord(u'ę'): u'e',
        ord(u'Ė'): u'E',
        ord(u'ė'): u'e',
        ord(u'Į'): u'I',
        ord(u'į'): u'i',
        ord(u'Š'): u'S',
        ord(u'š'): u's',
        ord(u'Ų'): u'U',
        ord(u'ų'): u'u',
        ord(u'Ū'): u'U',
        ord(u'ū'): u'u',
        ord(u'Ž'): u'Z',
        ord(u'ž'): u'z'
    }

    fieldnames = ['ID', 'Kodas', 'Aktyvus', 'Pavadinimas', 'Kategorija', 'Kaina su PVM', 'Gamintojas', 'Aprašymas',
              'Paveiksliukas', 'Ištrinti egzistuojantį paveiksliuką', 'Savybė']

    uniqueCode = ''

    index = 300

    def __init__(self, outputFolder, outputFile, withFeatures):
        self.outputAFolder = outputFolder
        self.outputFile = outputFile
        self.withFeatures = withFeatures


    def run(self, productUrl):
        d = pq(url=productUrl)
        d('[itemprop="description"]')
        with open(self.outputAFolder + '\prekes.csv', 'ab') as csvfile:
            fieldnames = ['ID', 'Nuotrauka', 'Pavadinimas', 'Kodas', 'Kategorija', 'Bazinė kaina', 'Galutinė kaina', 'Kiekis', 'Būsena']
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
            #writer = csv.writer(fp, delimiter=';')
            data = {}
            data['ID'] = '1'
            data['Nuotrauka'] = '1'
            data['Pavadinimas'] = '1'
            data['Kodas'] = '1'
            data['Kategorija'] = '1'
            data['Bazinė kaina'] = '1'
            data['Galutinė kaina'] = '1'
            data['Kiekis'] = '1'
            data['Būsena'] = '1'
            writer.writerow(data)
            writer.writerow(data)

    def importSuppliers(self):
        # get all supplier urls
        d = pq(url='http://zoofast.lt/acana-m-25.html')
        anchors = d('#left-search a')
        index = 1
        for anchor in tqdm(anchors):
            href = anchor.attrib['href']
            supplierWeb = pq(url=href)
            with open(self.outputAFolder + '\supplier.csv', 'ab') as csvfile:
                fieldnames = ['ID', 'Aktyvus (0/1)', 'Pavadinimas', 'Aprašymas', 'Trumpas aprašymas']
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
                data = {}
                if len(supplierWeb('.manufacturer_info').contents()) < 1:
                    continue
                data['ID'] = index
                index += 1
                data['Aktyvus (0/1)'] = '1'
                data['Pavadinimas'] = anchor.attrib['title'].encode('utf-8')
                data['Aprašymas'] = supplierWeb('.manufacturer_info').contents()[4].encode('utf-8')
                data['Trumpas aprašymas'] = supplierWeb('.manufacturer_info').contents()[1].text.encode('utf-8')
                writer.writerow(data)
            image = supplierWeb('.manufacturer_info img')
            urllib.urlretrieve(image.attr['src'], self.outputAFolder + '\images\\' + data['Pavadinimas'] + ".jpg")



    def saveSingleProduct(self, anchor, category):
        href = 'http://zoofast.lt' + anchor['anchor'].attr('title')
        if 'Puslapis' in href:
            href = 'http://zoofast.lt' + anchor['anchor'].attr('title')
        productPage = pq(url=href)

        if productPage('.zoomImg').attr['src'] is None:     # page not exist
            return

        image = productPage('.zoomImg').attr['src'].replace('x=190&y=190', 'x=380&y=380')
        productName = re.sub(r' \d(.*)', '', productPage('[itemprop="name"]').contents()[0])
        productNameNoSpace = productName.replace(' ', '_').replace(',', '').replace('"', '')\
            .replace('/', '_').decode('utf8').translate(self.table)
        urllib.urlretrieve('http://zoofast.lt//' + image, self.outputAFolder + '\ProductImages\\' + productNameNoSpace + ".jpg")

        # self.fieldnames
        data = {}
        #data['ID'] = index
        data['Aktyvus'] = '1'
        data['Pavadinimas'] = productName.encode('utf-8')
        data['Kategorija'] = category.encode('utf-8')
        # if ((productPage('[itemprop="price"]').attr['content'])[:-1]).replace('.', '').isdigit():
        #     data['Kaina su PVM'] = (productPage('[itemprop="price"]').attr['content'])[:-1].encode('utf-8')
        # else:
        #     data['Kaina su PVM'] = '0'
        data['Gamintojas'] = productPage('[itemprop="manufacturer"] a').contents()[0].encode('utf-8')
        data['Aprašymas'] = productPage('[itemprop="description"]').html().encode('utf-8').replace('\n', '')
        data['Paveiksliukas'] = 'http://localhost/prestashop/images/' + productNameNoSpace + '.jpg'
        data['Ištrinti egzistuojantį paveiksliuką'] = '1'
        #data['Savybė'] = anchor['attribute']

        pavadinimas = data['Pavadinimas']
        if self.withFeatures:
            self.saveCombinationSeparately(data, productPage, pavadinimas, anchor)
        else:
            self.saveAllCombination(data, productPage, pavadinimas, anchor)

    def saveAllCombination(self, data, productPage, pavadinimas, anchor):
        combinations = productPage('.products-list .products')
        for combination in combinations:
            realWeight = productPage(combination).find('li').text()
            if '2x' in realWeight:
                continue
            if '0,' in realWeight:
                realWeight = realWeight.replace('0,', '')
                if (len(realWeight) < 5):
                    if len(realWeight) < 4:
                        realWeight = realWeight.replace('kg', '00 g')
                    else:
                        realWeight = realWeight.replace('kg', '0 g')
                else:
                    realWeight = realWeight.replace('kg', ' kg')

            data['Pavadinimas'] = pavadinimas + ' ' + realWeight
            # Check name
            if Core.AlreadyContainsRepeatingName(self.outputAFolder, self.outputFile, data['Pavadinimas']):
                return
            realPrice = productPage(combination).find('.price').text().replace(' ', '')
            realPrice = realPrice.partition(':')[-1].rpartition('(')[0]
            self.index += 1
            data['ID'] = self.index
            data['Kaina su PVM'] = realPrice
            data['Savybė'] = anchor['attribute']
            data['Savybė'] = data['Savybė'] + ',' + Core.getAttributesString({'Svoris': realWeight})
            data['Kodas'] = self.uniqueCode + '_' + data['ID']
            Core.writeToCsvFile(self.outputAFolder, self.outputFile, data, self.fieldnames)

    def saveCombinationSeparately(self, data, productPage, pavadinimas, anchor):
        data['Pavadinimas'] = pavadinimas
        if Core.AlreadyContainsRepeatingName(self.outputAFolder, self.outputFile, data['Pavadinimas']):
            return
        self.index += 1
        data['ID'] = self.index
        data['Kaina su PVM'] = anchor['firstPrice']
        data['Savybė'] = anchor['attribute']
        data['Kodas'] = self.uniqueCode + '_' + str(data['ID'])
        Core.writeToCsvFile(self.outputAFolder, self.outputFile, data, self.fieldnames)
        # Write to deriniai
        self.importFeatures(data['Kodas'], productPage)

    def importFeatures(self, productCode, selector):
        fieldnames = ['Prekes kodas', 'Atributas', 'Reiksme', 'Poveikis kainai']
        combinations = selector('.products-list .products')
        for combination in combinations:
            try:
                value = selector(combination).find('li').text()
            except:
                continue
            # if ('0,' in realWeight):
            #     realWeight = realWeight.replace('0,', '')
            #     if (len(realWeight) < 5):
            #         realWeight = realWeight + '0'
            value.replace('kg', ' kg')
            attribute = ''
            if 'kg' in value or '0g' in value:
                attribute = 'Svoris '

            realPrice = selector(combination).find('.price').text().replace(' ', '')
            realPrice = realPrice.partition(':')[-1].rpartition('(')[0]
            data = {}
            data['Prekes kodas'] = productCode
            data['Atributas'] = attribute
            data['Reiksme'] = value
            data['Poveikis kainai'] = realPrice
            Core.writeToCsvFile(self.outputAFolder, self.outputFile.replace('.csv', '') + 'deriniai_visos_prekes.csv', data, fieldnames)

    def importProducts(self, uniqueCode, urlList, category):
        self.uniqueCode = uniqueCode
        anchors = []
        nextpages = []
        for url in urlList:
            d = pq(url=url['url'])
            # for item in d('.item-img span'):
            for item in d('.item.clearfix').items():
                anchors.append({'anchor': item.find('.item-img span'),
                                'attribute': Core.getAttributesString(url['attribute']),
                                'firstPrice': item.find('.item-text.first > .price > strong').text().replace(' ', '')})
            if d('.pager a').length > 0:                         # get next pages
                for item in d('.pager a')[:4]:
                    nextpages.append({'anchors': item, 'attribute': Core.getAttributesString(url['attribute'])})

        for nextpage in nextpages:
            d = pq(url=nextpage['anchors'].attrib['href'])
            for item in d('.item.clearfix').items():
                anchors.append({'anchor': item('.item-img span'),
                                'attribute': nextpage['attribute'],
                                'firstPrice': item.find('.item-text.first > .price > strong').text().replace(' ', '')})

        for anchor in tqdm(anchors):
            self.saveSingleProduct(anchor, category)
