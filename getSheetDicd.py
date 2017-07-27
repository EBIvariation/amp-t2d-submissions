#Module to populate dict from the worksheet in xlsx file
def processFile( sheet ):
    import pprint
    max_column = sheet.max_column
    max_column += 1
    max_row = sheet.max_row
    max_row += 1

    dicFile = {}

    rowCount = 0
    colCount = 0


    for i in range(1, max_row):
        for j in range(1, max_column):
            if sheet.cell(row=i, column=j).value is not None:
                rowCount = i
                list1 = (i, j, sheet.cell(row=i, column=j).value)
                dicFile[(i, j)] = sheet.cell(row=i, column=j).value
                if i == 1:
                    colCount = j

#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(dicFile)

    return (dicFile, rowCount, colCount)
