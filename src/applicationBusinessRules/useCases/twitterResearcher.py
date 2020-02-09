def getApplicationsWithMoreCitations(applications, fromDate, toDate, twitterApi):
    hashtags = " OR #".join(applications)

    twitterApplications = twitterApi.search(hashtags, fromDate, toDate)

    return twitterApplications