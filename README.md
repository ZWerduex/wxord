# Wxord

## Presentation

Wxord is a pretty basic application that allows you to create words from a pattern along with three (at the moment) weighted sets of characters.

I have created this application because I'm interested in the concept of creating words from a pattern and I wanted to see if I could create a simple application that could do this. I was highly inspired by the [WordGen website](https://www.wordgen.eu/#!en/generator/from-letters) and its idea of using a pattern to structure generated words. While I can add some enhancements of my taste, it is a good way to learn how to use ANTLR4 with Python and how to translate a simple application into multiple languages.

## Features

### Current features

- Create words from a pattern
- Three weighted sets of characters
- Use a generated word as a pattern by clicking on it in the list

### Planned features

- Customizable character sets using the UI
- Export and import sets of characters (yours or shared ones)
- Export and import UI language files
- Make a cool UI
- Add the possibility to save generated words (like `Séodès` or `Talledra`, I like those words)

Actually, you can change the charset used by tweaking directly the JSON file in the `charsets` folder. More information about this in the [documentation](doc/doc.md).

## Installation

No release has been made yet, so you will have to run the application from sources. You will need [Python 3.12.0](https://www.python.org/downloads/release/python-3120/) before cloning the repository.

Creating a virtual environment is recommended to install requirements.

```bash
cd wxord
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You're now ready to run the application.

```bash
py src/main.py
```

## Documentation

See the [documentation](doc/doc.md) for more detailed information about the application.

## Issues

If you find any issue, please report it in the [issues tab](https://github.com/ZWerduex/wxord/issues), and include the log file generated at the root of the application.

### Known issues

- Using quantifiers after tokens including digits in pattern such as `(1|2)*` or `(12|3)+` does not produce a truly random sequence of characters. This is due to the fact that digits are replaced by their corresponding character set before the quantifier is applied. `Fixed with the ANTLR4 update in version 0.2.0`