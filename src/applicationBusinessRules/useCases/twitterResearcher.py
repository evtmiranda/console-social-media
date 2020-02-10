def getNumberCitationsOfApplication(application, fromDate, toDate, twitterApi):
    application = application.split(" ")[0]
    hashtag = "#" + application

    tweets = twitterApi.search(hashtag, fromDate, toDate)

    numberCitationsOfApplication = {
        "application": application,
        "citations": len(tweets['results']),
    }

    return numberCitationsOfApplication
