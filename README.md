# Task Bands

## Installation

`Python` is already pre-installed on Linux. Windows users must visit official
site [download page](https://www.python.org/downloads/) to download python.

## Setup

Requirements installation:

    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt

---
**NOTE**

On Linux you also need `python3-venv` and `python3-pip` installed.

On Ubuntu you can install them with:

    sudo apt-get install python3-venv python3-pip

---

## Run

Start Django server:

    source ./venv/bin/activate
    python manage.py runserver


## Usage

```json
{
  "salary": 52000,
  "detailed": "yes"
}
```

`salary` - annual salary;
`detailed` - in case you need a detailed info for each tax band.

Response example:

```json
{
  "total_tax": 8300,
  "details": {
    "0.0 -> 12500.0": 0,
    "12501.0 -> 50000.0": 7500,
    "50001.0 -> 150000.0": 800,
    "150001.0 -> inf": 0
  }
}
```
