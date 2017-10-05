#Populate dictionary using dicSample # u'Sample_info', u'Sample',
def processSheetDic( dicSample, maxRow, maxCol):

    maxRow += 1
    maxCol += 1

    import pprint

    dicSampleOut = {}

    listDic = [dicSample]
    val = 0
    for dic in listDic:
        val += 1
        for i in range(1, maxRow):
            for j in range(1, maxCol):
                try:
                    Subject_ID = str(dicSample[i, 2])
                    dicSampleOut[(Subject_ID, j)] = str(dicSample[i, j])
                except KeyError:
                    dicSampleOut[(Subject_ID, j)] = "    "

    return (dicSampleOut)