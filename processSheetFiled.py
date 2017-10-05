#Populate dictionary using dicFile ## u'File_info ', u'File'
def processSheetDic( dicFile, maxRow, maxCol):

    maxRow += 1
    maxCol += 1

    import pprint

    dicFileOut = {}

    listDic = [dicFile]
    val = 0
    for dic in listDic:
        val += 1
        for i in range(1, maxRow):
            for j in range(1, maxCol):
                try:
                    Analysis_alias = str(dicFile[i, 3])
                    dicFileOut[(Analysis_alias, j)] = str(dicFile[i, j])
                except KeyError:
                    dicFileOut[(Analysis_alias , j)] = "    "

    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(dicFileOut)
    return (dicFileOut)
