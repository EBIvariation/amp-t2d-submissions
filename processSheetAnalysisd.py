#Populate dictionary using dicAnalysis  # u'Analysis_info', u'Analysis',
def processSheetDic( dicAnalysis, maxRow, maxCol):

    maxRow += 1
    maxCol += 1

    import pprint

    dicAnalysisOut = {}

    listDic = [dicAnalysis]
    val = 0
    for dic in listDic:
        val += 1
        for i in range(1, maxRow):
            for j in range(1, maxCol):
                try:
                    Analysis_alias = str(dicAnalysis[i, 2])
                    dicAnalysisOut[(Analysis_alias, j)] = str(dicAnalysis[i, j])
                except KeyError:
                    dicAnalysisOut[(Analysis_alias, j)] = "    "

#    pp = pprint.PrettyPrinter(indent=4)  # wkd
#    pp.pprint(dicAnalysisOut)

    return (dicAnalysisOut)
