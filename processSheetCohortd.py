#Populate dictionary using dicCohort  u'Cohort_info', u'Cohort',
def processSheetDic( dicCohort, maxRow, maxCol):

    maxRow += 1
    maxCol += 1

    import pprint

    dicCohortOut = {}

    listDic = [dicCohort]
    val = 0
    for dic in listDic:
        val += 1
        for i in range(1, maxRow):
            for j in range(1, maxCol):
                try:
                    Cohort_ID = str(dicCohort[i, 1])
                    dicCohortOut[(Cohort_ID, j)] = str(dicCohort[i, j])
                except KeyError:
                    dicCohortOut[(Cohort_ID, j)] = "    "

#    pp = pprint.PrettyPrinter(indent=4)  # wkd
#    pp.pprint(dicCohortOut)
    return (dicCohortOut)

