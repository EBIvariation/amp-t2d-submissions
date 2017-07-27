#Populate dictionary using dicRepeatedMeasures # u'RepeatedMeasures_info', u'RepeatedMeasures'
def processSheetDic( dicRepeatedMeasures, maxRow, maxCol):

    maxRow += 1
    maxCol += 1

    import pprint

    dicRepeatedMeasuresOut = {}
    dicRepBuild ={}
    listDic = [dicRepeatedMeasures]
    val = 0
    for dic in listDic:
        val += 1
        for i in range(1, maxRow):
            for j in range(1, maxCol):
                try:
                    Subject_ID = str(dicRepeatedMeasures[i, 1])
                    dicRepeatedMeasuresOut[(Subject_ID, j)] = str(dicRepeatedMeasures[i, j])
                except KeyError:
                    dicRepeatedMeasuresOut[(Subject_ID, j)] = "    "

#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(dicRepBuild)

    return (dicRepeatedMeasuresOut)

