from src.interfaceAdapters.file import (
    csvReaderAdapter,
    jsonWriterAdapter,
    csvWriterAdapter,
)
from src.interfaceAdapters.twitter import twitterApi
from src.interfaceAdapters.database import sqlite3Adapter
from src.applicationBusinessRules.useCases import (
    fileReader,
    fileWriter,
    twitterResearcher,
    databaseWriter,
)
from config.settings import APPLE_STORE_FILE_PATH
import datetime
import sys

sys.path.append("../")


def process():
    try:
        appleStoreFilePath = APPLE_STORE_FILE_PATH

        print("Obtendo as aplicações da categoria News com mais avaliações...")
        newsApplication = __getNewsApplicationWithMoreReviews(appleStoreFilePath)

        print("Obtendo as aplicações da categoria Book com mais avaliações...")
        bookApplications = __getTenBookApplicationsWithMoreReviews(appleStoreFilePath)

        print("Obtendo as aplicações da categoria Music com mais avaliações...")
        musicApplications = __getTenMusicApplicationsWithMoreReviews(appleStoreFilePath)

        print("Criando variáveis para pesquisar as citações das aplicações no twitter...")
        applications = []
        [applications.append(row["track_name"]) for row in bookApplications]
        [applications.append(row["track_name"]) for row in musicApplications]

        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(days=1)

        fromDate = yesterday.strftime("%Y%m%d2355")
        toDate = yesterday.strftime("%Y%m%d2359")

        print("Pesquisando as citações das aplicações no twitter...")
        applicationsWithMoreCitationsOnTwitter = __getApplicationsWithMoreCitationsOnTwitter(
            applications, fromDate, toDate
        )

        print("Criando o objeto com os dados finais...")
        result = __createFinalResultObject(
            bookApplications, musicApplications, applicationsWithMoreCitationsOnTwitter
        )

        print("Salvando os dados no arquivo .json...")
        __saveJsonResult(result)

        print("Salvando os dados no arquivo .csv...")
        __saveCsvResult(result)

        print("Salvando os dados no banco de dados .csv...")
        __saveDatabaseResult(result)

        print("Processo concluído.")

    except Exception as ex:
        print("Ocorreu um erro:" + str(ex))


def __getNewsApplicationWithMoreReviews(filePath):
    options = {
        "filterField": "prime_genre",
        "filterValue": "news",
        "maxResults": 1,
        "orderBy": "rating_count_tot",
    }

    applications = __getApplicationWithMoreReviews(filePath, options)

    return applications


def __getTenBookApplicationsWithMoreReviews(filePath):
    options = {
        "filterField": "prime_genre",
        "filterValue": "book",
        "maxResults": 10,
        "orderBy": "rating_count_tot",
    }

    applications = __getApplicationWithMoreReviews(filePath, options)

    return applications


def __getTenMusicApplicationsWithMoreReviews(filePath):
    options = {
        "filterField": "prime_genre",
        "filterValue": "music",
        "maxResults": 10,
        "orderBy": "rating_count_tot",
    }

    applications = __getApplicationWithMoreReviews(filePath, options)

    return applications


def __getApplicationWithMoreReviews(filePath, options):
    applications = fileReader.readAndFilter(filePath, options, csvReaderAdapter)

    return applications


def __getApplicationsWithMoreCitationsOnTwitter(applications, fromDate, toDate):
    numberCitationsOfApplications = []

    for application in applications:
        numberCitationsOfApplications.append(
            twitterResearcher.getNumberCitationsOfApplication(
                application, fromDate, toDate, twitterApi
            )
        )

    return numberCitationsOfApplications


def __createFinalResultObject(
    bookApplications, musicApplications, applicationsWithMoreCitationsOnTwitter
):
    finalResult = []

    for applicationRow in bookApplications:
        applicationObject = __createApplicationObject(
            applicationRow, applicationsWithMoreCitationsOnTwitter
        )
        finalResult.append(applicationObject)

    for applicationRow in musicApplications:
        applicationObject = __createApplicationObject(
            applicationRow, applicationsWithMoreCitationsOnTwitter
        )
        finalResult.append(applicationObject)

    return finalResult


def __createApplicationObject(application, applicationsWithMoreCitationsOnTwitter):
    citationsNumber = [
        row["citations"]
        for row in applicationsWithMoreCitationsOnTwitter
        if row["application"] == application["track_name"].split(" ")[0]
    ]

    applicationObject = {
        "id": application["id"],
        "track_name": application["track_name"],
        "n_citacoes": citationsNumber[0],
        "size_bytes": application["size_bytes"],
        "price": application["price"],
        "prime_genre": application["prime_genre"],
    }

    return applicationObject


def __saveJsonResult(result):
    fileWriter.write(result, jsonWriterAdapter)


def __saveCsvResult(result):
    fileWriter.write(result, csvWriterAdapter)


def __saveDatabaseResult(result):
    databaseWriter.write(result, sqlite3Adapter)
