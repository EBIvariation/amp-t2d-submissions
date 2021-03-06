from xls2xml import TSVReader

def test_get_valid_conf_keys():
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Sample')
    assert set(tsv_reader.get_valid_conf_keys()) == {'Sample'}
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Analysis')
    assert tsv_reader.get_valid_conf_keys() == []

def test_set_current_conf_key():
    # set_current_conf_key() should does nothing
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Sample')
    assert tsv_reader.is_valid()
    assert set(tsv_reader.get_valid_conf_keys()) == {'Sample'}
    tsv_reader.set_current_conf_key('Analysis')
    assert tsv_reader.is_valid()
    assert set(tsv_reader.get_valid_conf_keys()) == {'Sample'}
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Analysis')
    assert not tsv_reader.is_valid()
    assert tsv_reader.get_valid_conf_keys() == []
    tsv_reader.set_current_conf_key('Sample')
    assert not tsv_reader.is_valid()
    assert tsv_reader.get_valid_conf_keys() == []


def test_is_not_valid():
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Analysis')
    assert not tsv_reader.is_valid()

def test_is_valid():
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Sample')
    assert tsv_reader.is_valid()

def test_get_current_headers():
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Sample')
    headers = tsv_reader.get_current_headers()
    assert isinstance(headers, list)
    assert set(headers) == {'Sample_ID', 'Subject_ID', 'Geno_ID', 'Phenotype', 'Gender', 'Analysis_alias', 'Cohort ID',
                            'Ethnicity', 'Ethnicity Description', 'T2D', 'Case_Control', 'Description', 'Center_name',
                            'Hispanic or Latino; of Spanish origin', 'Age', 'Year of Birth', 'Year of first visit',
                            'Cell Type', 'Maternal_id', 'Paternal_id', 'Novel Attributes'}

def test_next():
    tsv_reader = TSVReader('data/example_samples.tsv', 'data/T2D_xls2xml_v1.conf', 'Sample')
    row = tsv_reader.next()
    assert isinstance(row, dict)
    assert 0 == cmp(row, {'Novel Attributes': None, 'Ethnicity Description': None, 'Description': 'Male normal',
                          'Cell Type': 'Blood', 'Maternal_id': 'SAM111113', 'Center_name': 'WTGC cambridge',
                          'Gender': 'male', 'Subject_ID': 'SAM111111', 'Paternal_id': 'SAM111115', 'T2D': 0,
                          'Hispanic or Latino; of Spanish origin': None, 'Cohort ID': 'CO1111', 'Year of Birth': '1986',
                          'Age': '31', 'Analysis_alias': 'AN001', 'Sample_ID': 'SAM111111', 'Geno_ID': None,
                          'Year of first visit': None, 'Case_Control': 'Control', 'Ethnicity': 'EUWH',
                          'Phenotype': 'MeSH:D006262'})
    for row in tsv_reader:
        assert isinstance(row, dict)
