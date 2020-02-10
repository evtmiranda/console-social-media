from src.interfaceAdapters.file import csvReaderAdapter, jsonWriterAdapter, csvWriterAdapter
from src.interfaceAdapters.twitter import twitterApi
from src.applicationBusinessRules.useCases import fileReader, fileWriter, twitterResearcher
from config.settings import APPLE_STORE_FILE_PATH
import datetime
import sys

sys.path.append("../")


def process():
    appleStoreFilePath = APPLE_STORE_FILE_PATH

    newsApplication = __getNewsApplicationWithMoreReviews(appleStoreFilePath)
    bookApplications = __getTenBookApplicationsWithMoreReviews(appleStoreFilePath)
    musicApplications = __getTenMusicApplicationsWithMoreReviews(appleStoreFilePath)

    applications = []
    [applications.append(row["track_name"]) for row in bookApplications]
    [applications.append(row["track_name"]) for row in musicApplications]

    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)

    fromDate = yesterday.strftime("%Y%m%d2355")
    toDate = yesterday.strftime("%Y%m%d2359")

    result = [
        {
            "id": "302584613",
            "track_name": "Kindle – Read eBooks, Magazines & Textbooks",
            "n_citacoes": 32,
            "size_bytes": "169747456",
            "price": "0",
            "prime_genre": "Book",
        },
        {
            "id": "379693831",
            "track_name": "Audible – audio books, original series & podcasts",
            "n_citacoes": 5,
            "size_bytes": "81558528",
            "price": "0",
            "prime_genre": "Book",
        },
        {
            "id": "1031002863",
            "track_name": "Color Therapy Adult Coloring Book for Adults",
            "n_citacoes": 4,
            "size_bytes": "135236608",
            "price": "0",
            "prime_genre": "Book",
        },
        {
            "id": "366869252",
            "track_name": "OverDrive – Library eBooks and Audiobooks",
            "n_citacoes": 0,
            "size_bytes": "39844864",
            "price": "0",
            "prime_genre": "Book",
        },
        {
            "id": "1024818709",
            "track_name": "HOOKED - Chat Stories",
            "n_citacoes": 0,
            "size_bytes": "94545920",
            "price": "0",
            "prime_genre": "Book",
        },
        {
            "id": "476508724",
            "track_name": "A Charlie Brown Christmas + iMessage Sticker Pack!",
            "n_citacoes": 3,
            "size_bytes": "121874432",
            "price": "5.99",
            "prime_genre": "Book",
        },
        {
            "id": "876336838",
            "track_name": "喜马拉雅FM（听书社区）电台有声小说相声英语",
            "n_citacoes": 0,
            "size_bytes": "130731008",
            "price": "0",
            "prime_genre": "Book",
        },
        {
            "id": "444553118",
            "track_name": "Jesus Calling Devotional by Sarah Young",
            "n_citacoes": 19,
            "size_bytes": "125770752",
            "price": "9.99",
            "prime_genre": "Book",
        },
        {
            "id": "906936224",
            "track_name": "快看漫画",
            "n_citacoes": 0,
            "size_bytes": "63058944",
            "price": "0",
            "prime_genre": "Book",
        },
        {
            "id": "1061132313",
            "track_name": "CHOMP by Christoph Niemann",
            "n_citacoes": 0,
            "size_bytes": "49474560",
            "price": "1.99",
            "prime_genre": "Book",
        },
        {
            "id": "284035177",
            "track_name": "Pandora - Music & Radio",
            "n_citacoes": 0,
            "size_bytes": "130242560",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "324684580",
            "track_name": "Spotify Music",
            "n_citacoes": 18,
            "size_bytes": "132510720",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "284993459",
            "track_name": "Shazam - Discover music, artists, videos & lyrics",
            "n_citacoes": 0,
            "size_bytes": "147093504",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "290638154",
            "track_name": "iHeartRadio – Free Music & Radio Stations",
            "n_citacoes": 6,
            "size_bytes": "116443136",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "336353151",
            "track_name": "SoundCloud - Music & Audio",
            "n_citacoes": 61,
            "size_bytes": "105009152",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "421254504",
            "track_name": "Magic Piano by Smule",
            "n_citacoes": 7,
            "size_bytes": "55030784",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "509993510",
            "track_name": "Smule Sing!",
            "n_citacoes": 3,
            "size_bytes": "109940736",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "418987775",
            "track_name": "TuneIn Radio - MLB NBA Audiobooks Podcasts Music",
            "n_citacoes": 4,
            "size_bytes": "101735424",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "510855668",
            "track_name": "Amazon Music",
            "n_citacoes": 45,
            "size_bytes": "77778944",
            "price": "0",
            "prime_genre": "Music",
        },
        {
            "id": "355554941",
            "track_name": "SoundHound Song Search & Music Player",
            "n_citacoes": 2,
            "size_bytes": "70516736",
            "price": "0",
            "prime_genre": "Music",
        },
    ]
    
    # applicationsWithMoreCitationsOnTwitter = __getApplicationsWithMoreCitationsOnTwitter(
    #     applications, fromDate, toDate
    # )

    # finalResult = __createFinalResultObject(
    #     bookApplications, musicApplications, applicationsWithMoreCitationsOnTwitter
    # )

    __saveJsonResult(result)
    __saveCsvResult(result)
    # __saveDatabaseResult(result)


    print(result)


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
