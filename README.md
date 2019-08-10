# Retrieve Publication Data

Set Up:

```
git clone https://github.com/dh-thesis/retrieve.git
cd retrieve/
virtualenv -p python3 --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
deactivate
./main
```

## Scripts

The following scripts are used to retrieve informations about entities from [MPG.PuRe](https://pure.mpg.de) and its named entity service [CoNE](https://pure.mpg.de/cone/) and finally to query the records.

- [`src/cone_jour.py`](./src/cone_jour.py)

```
100%|████████████████████████████████████████████| 7679/7679 [24:13<00:00,  5.40it/s]
```

- [`src/cone_lang.py`](./src/cone_lang.py)

```
100%|████████████████████████████████████████████| 8590/8590 [24:02<00:00,  5.74it/s]
```

- [`src/cone_pers.py`](./src/cone_pers.py)

```
100%|████████████████████████████████████████████| 60007/60007 [3:15:34<00:00,  5.36it/s]
```

- [`src/pure_ctx.py`](./src/pure_ctx.py)
- [`src/pure_ous.py`](./src/pure_ous.py)
- [`src/pure_pub.py`](./src/pure_pub.py)

```
100%|████████████████████████████████████████████| 219/219 [20:42<00:00,  3.14s/it]
```

Requirements: [Pybman](https://pypi.org/project/pybman/)
