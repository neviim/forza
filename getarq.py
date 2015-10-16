#!/usr/bin env python3
# -*- coding: utf-8 -*-

import os
import csv

import json
import pymongo
from pymongo import MongoClient

# mongodb
def get_db():
    client = MongoClient('localhost:27017')
    db = client.forza6db
    return db

def add_dados(db, data):
    db.countries.insert(data)

def get_country(db, colecao):
    return db.get_collection(colecao).find({}).count()
# ---

# gera arquivo csv
def gera_csv(localFilePath):
    #verifica se tem arquivo com estencao .csv
    if (os.path.isfile(localFilePath) and localFilePath.endswith(".csv")):
        # gera arquivo csv
        with open(localFilePath, 'r', encoding='utf-8') as csvfile:
            #sniff
            fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            #cria um CSV
            myReader = csv.reader(csvfile, dialect=fileDialect)

            for row in myReader:
                print(row)


# gera arquivo json
def gera_json(localFilePath):
    if (os.path.isfile(localFilePath) and localFilePath.endswith(".csv")):

        # abre banco forza
        db = get_db()

        # gera arquivo json
        with open(localFilePath, 'r', encoding='utf-8') as csvfile:
            #sniff para encontrar o formato
            fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            #le o arquivo CSV do diretorio.
            dictReader = csv.DictReader(csvfile, dialect=fileDialect)

            for row in dictReader:
                # para coleção de carros
                if get_country(db, 'carros') == 0:
                    db.carros.insert(row)
                    #print(row)

    return


# le os arquivos
def leArquivos(filePath):
    #get all files in the given folder
    fileListing = os.listdir(filePath)
    for myFile in fileListing:
        #le a path do arquivo
        localFilePath = os.path.join(filePath, myFile)

        gera_json(localFilePath)

    return


# inicializar...
if __name__ == '__main__':
    currentPath = os.path.dirname(__file__)
    filePath = os.path.abspath(os.path.join(currentPath, os.pardir,os.pardir,'_github/forza/csv'))

    leArquivos(filePath)


