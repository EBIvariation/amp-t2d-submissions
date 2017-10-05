#https://automatetheboringstuff.com/chapter12/#calibre_link-63
#from openpyxl import load_workbook
import openpyxl
import json
import pprint
import sys

#Module to populate dict from the worksheet in xlsx file
import getSheetDicd

#Worksheets to import from submission xlsx file
#[u'Please Read First',
# u'Project_info', u# 'Project',

# u'Cohort_info', u'Cohort',
import processSheetCohortd #
# u'RepeatedMeasures_info', u'RepeatedMeasures',
import processSheetRepeatedMeasuresd
# u'Sample_info', u'Sample',
import processSheetSampled

# u'Attribute Mapping_info', u'Attribute Mapping',

# u'Analysis_info', u'Analysis',
import processSheetAnalysisd
# u'File_info ', u'File', u'Links_info', u'CVs']
import processSheetFiled
#*####

# u'Links_info', u'CVs']

#Creates output file 'tsv'
import combineDicd


#Open xlsx file

try:
    wb = openpyxl.load_workbook(filename='example_AMP_T2D_Submission_form_V1.xlsx')
except NameError:
    print "Can not open xlsx file"



######################################
###Build dict from worksheet:

#Process Project xlsx worksheet:
#u'Project_info', u# 'Project',

sheetSample = wb.get_sheet_by_name('Project')
(dicProject, maxRow, maxCol )= getSheetDicd.processFile(sheetSample)

#pp = pprint.PrettyPrinter(indent=4)  # wkd
#pp.pprint(sheetSample)
#Process Project xlsx worksheet:#


#Process Sample xlsx worksheet:
#u'Sample_info', u'Sample',

sheetSample = wb.get_sheet_by_name('Sample')
(dicSample, maxRow, maxCol )= getSheetDicd.processFile(sheetSample)
dicSampleOut = processSheetSampled.processSheetDic(dicSample ,maxRow, maxCol)

#pp = pprint.PrettyPrinter(indent=4)  # wkd
#pp.pprint(dicSampleOut)
#Process Sample xlsx worksheet:#


#Process Cohort xlsx worksheet:
#u'Cohort_info', u'Cohort',

sheetCohort = wb.get_sheet_by_name('Cohort')
(dicCohort,  maxRow, maxCol )= getSheetDicd.processFile(sheetCohort)
dicCohortOut = processSheetCohortd.processSheetDic(dicCohort ,maxRow, maxCol)

#pp = pprint.PrettyPrinter(indent=4)  # wkd
#pp.pprint(dicCohortOut)
#Process Cohort xlsx worksheet:#


#Process Attribute Mapping xlsx worksheet:
#u'Attribute Mapping_info', u'Attribute Mapping',

sheetAttributeMapping = wb.get_sheet_by_name('Attribute Mapping')
(dicAttributeMapping, maxRow, maxCol)  = getSheetDicd.processFile(sheetAttributeMapping)

#pp = pprint.PrettyPrinter(indent=4)  # wkd
#pp.pprint(dicAttributeMapping)
#Process Attribute Mapping xlsx worksheet:#


#Process Analysis xlsx worksheet:
#u'Analysis_info', u'Analysis'

sheetAnalysis = wb.get_sheet_by_name('Analysis')
(dicAnalysis, maxRow, maxCol)  = getSheetDicd.processFile(sheetAnalysis)

dicAnalysisOut = processSheetAnalysisd.processSheetDic(dicAnalysis, maxRow, maxCol)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(dicAnalysisOut)
#Process Analysis xlsx worksheet:#


#Process File xlsx worksheet:
#u'File_info ', u'File',

sheetFile = wb.get_sheet_by_name('File')
(dicFile,  maxRow, maxCol)  =  getSheetDicd.processFile(sheetFile)

dicFileOut = processSheetFiled.processSheetDic(dicFile, maxRow, maxCol)

#pp = pprint.PrettyPrinter(indent=4)  # wkd
#pp.pprint(dicFileOut)
#Process File xlsx worksheet:#



#Process RepeatedMeasures xlsx worksheet:
#u'RepeatedMeasures_info', u'RepeatedMeasures',

sheetRepeatedMeasures = wb.get_sheet_by_name('RepeatedMeasures')
(dicRepeatedMeasures,  maxRow, maxCol)  =  getSheetDicd.processFile(sheetRepeatedMeasures)

dicRepeatedMeasuresOut = processSheetRepeatedMeasuresd.processSheetDic(dicRepeatedMeasures,maxRow, maxCol)

#pp = pprint.PrettyPrinter(indent=4)  # wkd
#pp.pprint(dicRepeatedMeasuresOut)
#Process RepeatedMeasures xlsx worksheet:#


######################################
###Build dict from worksheet:#





###Combine dictionary and print ampXlsxSubmission2tsv.tsv:
combineDicd.processDic(dicSampleOut,dicCohortOut,dicRepeatedMeasuresOut,dicAnalysisOut, dicFileOut )
###Combine dictionary and print ampXlsxSubmission2tsv.tsv:#