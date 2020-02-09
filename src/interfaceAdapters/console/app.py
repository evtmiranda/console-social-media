from src.interfaceAdapters.file import csvReaderAdapter
from src.applicationBusinessRules.useCases import fileReader, twitterResearcher
from config.settings import CSV_FILE_PATH
import sys
sys.path.append("../")

def process():
    filePath = CSV_FILE_PATH

    newsApplication = __getNewsApplicationWithMostReviews(filePath)
    bookApplications = __getTenBookApplicationsWithMostReviews(filePath)
    musicApplications = __getTenMusicApplicationsWithMostReviews(filePath)

    print(newsApplication)
    print(bookApplications)
    print(musicApplications)


def __getNewsApplicationWithMoreReviews(filePath):
    options = {
            'filterField': 'prime_genre',
            'filterValue': 'news',
            'maxResults': 1,
            'orderBy': 'rating_count_tot'
        }

    applications = __getApplicationWithMostReviews(filePath, options)

    return applications


def __getTenBookApplicationsWithMoreReviews(filePath):
    options = {
            'filterField': 'prime_genre',
            'filterValue': 'book',
            'maxResults': 10,
            'orderBy': 'rating_count_tot'
        }

    applications = __getApplicationWithMostReviews(filePath, options)

    return applications


def __getTenMusicApplicationsWithMoreReviews(filePath):
    options = {
            'filterField': 'prime_genre',
            'filterValue': 'music',
            'maxResults': 10,
            'orderBy': 'rating_count_tot'
        }

    applications = __getApplicationWithMostReviews(filePath, options)

    return applications


def __getApplicationWithMoreReviews(filePath, options):
    applications = fileReader.readAndFilter(filePath, options, csvReaderAdapter)

    return applications


def __getApplicationsWithMoreCitationsOnTwitter(applications):
    applicationsWithMoreCitations = twitterResearcher.getApplicationsWithMoreCitations(applications)

    return applicationsWithMoreCitations
