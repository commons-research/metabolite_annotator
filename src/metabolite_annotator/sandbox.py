import pystow


# Get a directory (as a pathlib.Path) for ~/.data/indra/database.tsv
indra_database_path = pystow.join('indra', 'database', name='database.tsv')


url = 'https://raw.githubusercontent.com/pykeen/pykeen/master/src/pykeen/datasets/nations/test.txt'

path = pystow.ensure('pykeen', 'datasets', 'nations', url=url)


metabolite_annotator_module = pystow.module("metabolite_annotator")
METABOLITE_ANNOTATOR_HOME = metabolite_annotator_module.base


def get_config(key):
    pystow.get_config("metabolite_annotator", key)
    
get_config('db')

test = pystow.get_config("metabolite_annotator", 'db')

METABOLITE_ANNOTATOR_DB = get_config('metabolite_annotator','db',raise_on_missing=True)


