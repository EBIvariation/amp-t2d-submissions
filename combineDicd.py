#Combine worksheet dictionaries and create tsv report
def processDic( dicSampleOut,dicCohortOut,dicRepeatedMeasuresOut,dicAnalysisOut,dicFileOut):
    import pprint
    import re
    from collections import defaultdict
    f= open("ampXlsxSubmission2tsv.tsv","w+")   #Create tsv report

    dicKey = {}
    dicBuild = {}

    keylistdicSampleOut = dicSampleOut.keys()
    keylistdicSampleOut.sort()

    for key in keylistdicSampleOut:
        dicKey[key[0]] = + 1

    buildCount = 0

    for key in dicKey.keys():
        buildCount += 1

#Process dictionary dicSampleOut
        for saMco in range(1, 22):
            samVal = dicSampleOut[(key, saMco)]
            dicBuild.setdefault(key, []).append(samVal)

#Process dictionary dicCohortOut
        for co in range(1, 14):
            cohortVal = dicCohortOut[(dicSampleOut[(key, 7)]), co]
            dicBuild.setdefault(key, []).append(cohortVal)

#Process dictionary dicRepeatedMeasuresOut
        for remeas in range(1, 51):
            matchObject = re.match('Subject_ID', key)
            if matchObject:
                keyNew = "Sample_ID"
                repeatMeasVal = dicRepeatedMeasuresOut[(str(keyNew), remeas)]
            else:
                try:
                    repeatMeasVal = dicRepeatedMeasuresOut[(str(key), remeas)]
                except KeyError:
                    repeatMeasVal = ' '
            dicBuild.setdefault(key, []).append(repeatMeasVal)

#Process dictionary dicAnalysisOut
        for analyco in range(1, 17):
            try:
                analycoVal = dicAnalysisOut[dicSampleOut[(str(key),6)], analyco]
            except KeyError:
                analycoVal = ' '
            dicBuild.setdefault(key, []).append(analycoVal)

#Process dictionary dicFileOut
        for fileco in range(1, 5):
            try:
                filecoVal =  dicFileOut[dicSampleOut[(key,6)], fileco]
            except KeyError:
                filecoVal = ' '
            dicBuild.setdefault(key, []).append(filecoVal)


#Print dicBuild to ampXlsxSubmission2tsv.tsv file

    name = "Subject_ID"
    countSample = 0
    f.write('\t'.join(map(str, dicBuild['Subject_ID'])) + '\n')
    for key in sorted(dicKey.keys()):
            m = re.match('Subject_ID', key)
            if not m:
                countSample += 1
                f.write('\t'.join(map(str, dicBuild[key])) + '\n')