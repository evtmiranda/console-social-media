def readAndFilter(filePath, options, fileReader):

    rows = fileReader.read(filePath)

    if("filterField" in options):
        rowsOfCategory = [row for row in rows if row[options["filterField"]].lower()
                  == options["filterValue"].lower()]

        orderedRows = sorted(rowsOfCategory,
                       key=lambda k: int(k[options["orderBy"]]), reverse=True)

    else:
        orderedRows = sorted(rows,
                       key=lambda k: int(k[options["orderBy"]]), reverse=True)

    filteredRows = [row for row in orderedRows[:int(options["maxResults"])]]

    for i in range(len(filteredRows)):
        del filteredRows[i][""]

    return filteredRows
