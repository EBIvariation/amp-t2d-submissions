from lxml import etree
from xls2xml import XLSReader
from xls2xml import utils

def test_validate_xls():
    validation_schema = '../T2D_xlsx.schema'
    xls_reader = XLSReader('data/example_AMP_T2D_Submission_form_V2_DB_12_03_18.xlsx',
                           '../T2D_xlsx.conf')
    assert xls_reader.is_valid()
    assert utils.validate_file(xls_reader, validation_schema)

def test_xls2xml_analysis():
    xls_reader = XLSReader('data/example_AMP_T2D_Submission_form_V2_DB_12_03_18.xlsx',
                           '../T2D_xlsx.conf')
    conf_keys = ['Analysis', 'File', 'Sample']
    xls_readers = [ (key, xls_reader) for key in conf_keys ]
    output_xml = utils.multiple_objects_to_xml(xls_readers, '../T2D_xlsx.schema',
                                               '../T2D_xls2xml.xslt')
    with open('data/example_analysis.xml', 'r') as analysis_example:
        assert analysis_example.readline()
        assert etree.tostring(output_xml, pretty_print=True) == analysis_example.read()

def test_xls2xml_sample():
    xls_reader = XLSReader('data/example_AMP_T2D_Submission_form_V2_DB_12_03_18.xlsx',
                           '../T2D_xlsx.conf')
    conf_keys = ['Sample', 'Cohort']
    xls_readers = [ (key, xls_reader) for key in conf_keys ]
    output_xml = utils.multiple_objects_to_xml(xls_readers, '../T2D_xlsx.schema',
                                               '../T2D_xls2xml.xslt')
    with open('data/example_sample.xml', 'r') as sample_example:
        assert sample_example.readline()
        assert etree.tostring(output_xml, pretty_print=True) == sample_example.read()

def test_xls2xml_study():
    xls_reader = XLSReader('data/example_AMP_T2D_Submission_form_V2_DB_12_03_18.xlsx',
                           '../T2D_xlsx.conf')
    xls_readers = [ ('Project', xls_reader) ]
    output_xml = utils.multiple_objects_to_xml(xls_readers, '../T2D_xlsx.schema',
                                              '../T2D_xls2xml.xslt')
    with open('data/example_study.xml', 'r') as study_example:
        assert study_example.readline()
        assert etree.tostring(output_xml, pretty_print=True) == study_example.read()
