# RETEDECON

Development of a monitoring and control system for disinfection, registration and counting of users
Innovative device that speeds up entry to a building, allowing us to:

* Register who enters
* Take your body temperature
* Disinfection of hands and feet
* Counting of users inside the building to avoid overcrowding.

In addition, RETEDECON alerts us to any irregularity, in order to detect possible cases of contagion and guarantee compliance with biosafety protocols.


Disclaimer: this is a work in progress project, stay tuned for updates (*).

## Installation and Usage

### Setup environment

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

Clone repository

```bash
git clone https://github.com/julianVelandia/UI_RETEDECON.git
```

And then install the development dependencies:

```bash
pip install -r requirements.dev.txt
```

### Run unit tests

You can run all the tests with:

```bash
make tests
```

Alternatively, you can run `pytest` yourself.

```bash
pytest
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license.