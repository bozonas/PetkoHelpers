# -*- coding: utf-8 -*-
import csv


class Core:

    fieldnames = ['ID', 'Aktyvus (0/1)', 'Pavadinimas', 'Aprašymas', 'Trumpas aprašymas']

    @staticmethod
    def AlreadyContainsRepeatingName(outputFolder, outputFile, name):
        with open(outputFolder + '\\' + outputFile, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if row[2] == name:
                    return True
        return False

    @staticmethod
    def writeToCsvFile(outputFolder, outputFile, data, fieldnames):
        with open(outputFolder + '\\' + outputFile, 'ab+') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
            writer.writerow(data)

    @staticmethod
    def getAttributesString(attributesDic):
        return attributesDic.__str__().replace('{', '').replace('}', '')\
            .replace("'", '').replace(': ', ':').replace(', ', ',')


    @staticmethod
    def removeDublicate(inputFile, outputFile):
        fieldnames = ['ID', 'Aktyvus', 'Pavadinimas', 'Kategorija', 'Kaina su PVM', 'Gamintojas', 'Aprašymas',
                      'Paveiksliukas', 'Ištrinti egzistuojantį paveiksliuką', 'Savybė']

        with open(inputFile, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            # allNames = [item for sublist in reader for item in sublist]
            # allNames = [item[2] for item in reader]
            temp = []
            for row in reader:
                # if any(row[2] in i in)
                if any(row[2] == item[2] for item in temp):
                    continue
                temp.append(row)
            # temp = [row for row in reader if row[2] in allNames]

        with open(outputFile, 'ab') as csvfile:
            for item in temp:
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
                data = {}
                data[fieldnames[1]] = item[1]
                data[fieldnames[2]] = item[2]
                data[fieldnames[2]] = item[2]
                data[fieldnames[3]] = item[3]
                data[fieldnames[4]] = item[4]
                data[fieldnames[5]] = item[5]
                data[fieldnames[6]] = item[6]
                data[fieldnames[7]] = item[7]
                data[fieldnames[8]] = item[8]
                data[fieldnames[9]] = item[9]
                writer.writerow(data)
