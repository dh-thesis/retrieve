import sys

from pybman import utils

from .utils_paths import BASE_DIR

print("console output is redirected to map_ṕost.log ...")

stdout = sys.stdout

log = open("log/data_ctx_mpis.log", "w+")
sys.stdout = log

mpis = utils.read_json(BASE_DIR + 'mpis/scrape/all.json')
mpis_mapped = utils.read_json(BASE_DIR + 'mpis/map/mpi_ous.json') # ous.json

m = list(mpis.keys())
n = list(mpis_mapped.keys())

counter = 0
no_map = []

for i in m:
    if i in n:
        counter += 1
        continue
    elif i.split(",")[0] in n:
        # Max Planck Institute for Software Systems, Kaiserslautern site
        # Max Planck Institute for Software Systems, Saarbrücken site
        # Max Planck Institute for Intelligent Systems, Stuttgart site
        # Max Planck Institute for Intelligent Systems, Tübingen site
        counter += 1
        continue
    elif i.split(" (")[0] in n:
        # Max Planck Institute for Gravitational Physics (Hannover)
        # Max Planck Institute for Ornithology (Radolfzell)
        # Max Planck Institute for Plasma Physics (Greifswald)
        counter += 1
        continue
    elif i == 'Research Group Social Neuroscience':
        # part of the Max Planck Institute for Human Cognitive and Brain Sciences
        continue
    else:
        no_map.append(i)

print("")
print(str(counter),"institutes mapped to ous")
if no_map:
    print("")
    print(len(no_map), "institutes could not be mapped to ou")
    print("")
    print("no mapping found for")
    for i in no_map:
        print("    ", i)

########################
### MAP: OUS --> CTX ###
########################

print("")
print("")
print("map: ous --> ctx")
print("")

pure_ctxs = utils.read_json(BASE_DIR + 'pure/ctx/all.json')

collections = {}

for rec in pure_ctxs['records']:
    objectId = rec['data']['objectId']
    maintainers = rec['data']['responsibleAffiliations']
    for maintainer in maintainers:
        maintainer = maintainer['objectId']
        if maintainer in collections:
            collections[maintainer].append(objectId)
        else:
            collections[maintainer] = [objectId]

m = list(mpis_mapped.values())
n = list(collections.keys())

fnd = {}
counter = 0
print("")

for mpi in m:
    if mpi in n:
        fnd[mpi] = collections[mpi]
        counter += 1
    else:
        print(mpi, "has no context")

print("")
print(str(counter),"ous mapped to contexts")
print("")

utils.write_json(BASE_DIR + "mpis/mapped/ous_ctx.json", fnd)

########################
### MAP: CAT --> OUS ###
########################

print("")
print("")
print("map: cat --> ous")
print("")
cats = utils.read_json(BASE_DIR + 'mpis/scrape/categories.json')
print("")

c = list(cats.keys())
n = list(mpis_mapped.keys())

cats_mapped = {}
counter = 0

for cat in cats:
    cats_mapped[cat] = []
    for mpi in cats[cat]:
        if mpi in n:
            # prevent duplicate
            if mpis_mapped[mpi] not in cats_mapped[cat]:
                counter += 1
                cats_mapped[cat].append(mpis_mapped[mpi])
            else:
                continue
        elif mpi.split(",")[0] in n:
            # prevent duplicate
            if mpis_mapped[mpi.split(",")[0]] not in cats_mapped[cat]:
                counter += 1
                cats_mapped[cat].append(mpis_mapped[mpi.split(",")[0]])
            else:
                continue
        elif mpi.split(" (")[0] in n:
            # prevent duplicate
            if mpis_mapped[mpi.split(" (")[0]] not in cats_mapped[cat]:
                counter += 1
                cats_mapped[cat].append(mpis_mapped[mpi.split(" (")[0]])
            else:
                continue
        elif mpi == 'Research Group Social Neuroscience':
            # part of the Max Planck Institute for Human Cognitive and Brain Sciences
            continue
        elif mpi in no_map:
            # mpi has no mapping
            continue
        else:
            print(mpi, "could not be mapped to", cat)


print("found",str(counter),"mappings to categories")
print("")

utils.write_json(BASE_DIR + "mpis/mapped/cat_ous.json", cats_mapped)
print("")

n = list(collections.keys())

ous_cat = {}

for mpi in n:
    for cat in c:
        if mpi in cats_mapped[cat]:
            if mpi in ous_cat:
                ous_cat[mpi].append(cat)
            else:
                ous_cat[mpi] = [cat]
        else:
            continue

print("found",str(len(ous_cat)),"mappings from institutes to categories")
print("")

utils.write_json(BASE_DIR + "mpis/mapped/ous_cat.json", ous_cat)

print("")

# mpis = utils.read_json(BASE_DIR + 'mpis/scrape/all.json')
# mpis_mapped = utils.read_json(BASE_DIR + 'mpis/map/mpi_ous.json')

# no_map = utils.read_plain_clean(BASE_DIR + 'mpis/map/ous_not_fnd.txt')

m = list(mpis.keys())
n = list(mpis_mapped.keys())

all_tags = []
mpis_tags = {}

for mpi in m:
    idx = None
    tags = mpis[mpi]['tags']
    if mpi in n:
        idx = mpis_mapped[mpi]
    elif mpi.split(",")[0] in n:
        idx = mpis_mapped[mpi.split(",")[0]]
    elif mpi.split(" (")[0] in n:
        idx = mpis_mapped[mpi.split(" (")[0]]
    elif mpi == 'Research Group Social Neuroscience':
        # part of the Max Planck Institute for Human Cognitive and Brain Sciences
        pass
    elif mpi in no_map:
        pass
    else:
        print("no idx found for", mpi)
    if idx:
        if idx not in mpis_tags:
            mpis_tags[idx] = tags
        else:
            if tags == mpis_tags[idx]:
                pass
            else:
                for tag in tags:
                    if tag not in mpis_tags[idx]:
                        mpis_tags[idx].append(tag)
    else:
        continue
    for tag in tags:
        if tag not in all_tags:
            all_tags.append(tag)


all_tags.sort()

utils.write_json(BASE_DIR + "mpis/mapped/ous_tags.json", mpis_tags)
utils.write_list(BASE_DIR + "mpis/mapped/ous_tags_all.txt", all_tags)

log.close()
sys.stdout = stdout
