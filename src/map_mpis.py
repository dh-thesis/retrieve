from pybman import utils

from .utils_paths import BASE_DIR

MPIS_DIR = BASE_DIR + 'mpis/'

all_ous = []
all_fnd = {}

eng_fnd = utils.read_json(MPIS_DIR + "map/ous_fnd_eng.json")

for eng_ou in eng_fnd:
    all_fnd[eng_ou] = eng_fnd[eng_ou]
    all_ous.append(eng_fnd[eng_ou])

deu_fnd = utils.read_json(MPIS_DIR + "map/ous_fnd_deu.json")
deu_ous = list(deu_fnd.values())

for deu_ou in deu_fnd:
    if deu_fnd[deu_ou] not in all_ous:
        all_fnd[deu_ou] = deu_fnd[deu_ou]
        all_ous.append(deu_fnd[deu_ou])

utils.write_json(MPIS_DIR + "map/mpi_ous.json",all_fnd)
