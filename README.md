# SkyWatch Data Sources

[![Build Status](https://travis-ci.org/bruno-source/skywatch-data-sources.svg?branch=master)](https://travis-ci.org/bruno-source/skywatch-data-sources)
[![Coverage Status](https://coveralls.io/repos/github/bruno-source/skywatch-data-sources/badge.svg?branch=master)](https://coveralls.io/github/bruno-source/skywatch-data-sources?branch=master)

A simple Command-line interface to list [SkyWatch's](https://www.skywatch.com/) available data sources.
SkyWatch aggregates Earth observation data from many industry-leading sources into a single plataform.

![](docs/demo.gif)

## Instalation

Download and install the latest version from GitHub:
```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install git+https://github.com/bruno-source/skywatch-data-sources.git@v0.1#egg=skywatch_data_sources
```

## Usage
From the command-line:
```
$ skywatch-data-sources
╒═════════════════════════╤════════════╤══════════════╕
│ Source                  │ Provider   │ Resolution   │
╞═════════════════════════╪════════════╪══════════════╡
│ TripleSat Constellation │ 21AT       │ 80cm         │
├─────────────────────────┼────────────┼──────────────┤
.
.
.


$ skywatch-data-sources --help
Usage: skywatch-data-sources [OPTIONS]

  Parses www.skywatch.com and returns a list of its available data sources
  in a pretty-printed tabular data.

Options:
  --help  Show this message and exit.
```

Python console:
```
>>> from skywatch_data_sources.cli import list_data_sources
>>> list_data_sources()
╒═════════════════════════╤════════════╤══════════════╕
│ Source                  │ Provider   │ Resolution   │
╞═════════════════════════╪════════════╪══════════════╡
│ TripleSat Constellation │ 21AT       │ 80cm         │
├─────────────────────────┼────────────┼──────────────┤
.
.
.
```

```
>>> from skywatch_data_sources.sources import get_data_sources
>>> sources = get_data_sources()
>>> sources
[{'Provider': '21AT', 'Resolution': '80cm', 'Source': 'TripleSat Constellation'}
 .
 .
 .
 {'Provider': 'Urthecast', 'Resolution': '1m', 'Source': 'Deimos-2'}]
```

## Development and Testing

Clone the project, change directory and choose your favorite way to install
```console
$ git clone https://github.com/bruno-source/skywatch-data-sources
$ cd skywatch-data-sources
```

- With Pipenv:

    ```console
    $ pipenv install --dev
    $ pipenv run pytest
    ```

- With Virtualenv:

    ```console
    $ python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ pytest
    ```
