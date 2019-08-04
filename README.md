# Retrieve Publication Data

Set Up:

```
git clone https://github.com/dh-thesis/retrieve.git
cd retrieve/
virtualenv -p python3 --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
deactivate
```

- make sure you have [Gecko Driver](https://github.com/mozilla/geckodriver/releases/) available on your `PATH`
- modify output dir (`BASE_DIR`) in [`./src/utils_path.py`](./src/utils_path.py) (optional)
- finally start the retrieval:

```
./main
```

## Scripts

```
start retrieval!
```

#### Entity and Item Records

The following scripts are used to retrieve informations about entities from [MPG.PuRe](https://pure.mpg.de) and its named entity service [CoNE](https://pure.mpg.de/cone/) and finally to query the records.

- [`cone_jour.py`](./src/cone_jour.py)

```
100%|████████████████████████████████████████████| 7679/7679 [24:13<00:00,  5.40it/s]
```

- [`cone_lang.py`](./src/cone_lang.py)

```
100%|████████████████████████████████████████████| 8590/8590 [24:02<00:00,  5.74it/s]
```

- [`cone_pers.py`](./src/cone_pers.py)

```
100%|████████████████████████████████████████████| 60007/60007 [3:15:34<00:00,  5.36it/s]
```

- [`pure_ctx.py`](./src/pure_ctx.py)
- [`pure_ous.py`](./src/pure_ous.py)
- [`pure_pub.py`](./src/pure_pub.py)

```
100%|████████████████████████████████████████████| 219/219 [20:42<00:00,  3.14s/it]
```

Requirements: [Pybman](https://pypi.org/project/pybman/)

#### Institutes of the Max Planck Society

The following scripts are used to crawl informations about the current Max Planck Institutes (MPIs), their research domains (`category`) and research areas (`tag`) from the website of the Max Planck Society.

- [`crawl_mpis_eng.py`](./src/crawl_mpis_eng.py)
- [`crawl_mpis_deu.py`](./src/crawl_mpis_deu.py)

Requirements: [Selenium](https://pypi.org/project/selenium/), [Firefox](https://www.mozilla.org/en-US/firefox/) and [Gecko Driver](https://github.com/mozilla/geckodriver/releases/)

#### Mapping of MPIs to MPG.PuRe Entities

The following scripts are used to map the crawled MPIs to their corresponding identifiers in MPG.PuRe and to find the associated contexts as well as categories and thematic tags of the institutes.

- [`map_mpis_eng.py`](./src/map_mpis_eng.py)
- [`map_mpis_deu.py`](./src/map_mpis_deu.py)
- [`map_mpis.py`](./src/map_mpis.py)
- [`map_post.py`](./src/map_post.py)

Requirements: [Pybman](https://pypi.org/project/pybman/)
