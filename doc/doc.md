# Documentation

## Charsets

A charset file is a JSON file that contains a few info about itself, along with the characters and their weights. Located in the `charsets` folder, you can create your own charset file or modify an existing one to change the character set used by the application.

Currently, the application uses a single charset file, which has been defined statically. However, you can change the charset used by tweaking directly the `basic_french` JSON file in the `charsets` folder.

### Structure
```bash
cat charsets/default_english.json
```

```json
{
  "name": "English",
  "description": "Default English charset",
  "suggested": ["2112(w|2)?", "w1h", "th100?"],
  "charsets": [
    {
        "a": 12,
        "e": 16,
        "i": 4
    },
    {
        "b": 2,
        "w": 14,
    }
  ]
}
```

The file name is used as an unique identifier for the charset. The `name` and `description` fields are used to display information about the charset in the UI. The `suggested` field is used to display a few interesting examples of patterns that can be generated using the charset.

The `charsets` field is an array of objects, each object containing the characters and their weights.

## Language files

Although not being currently used, the application plans to support multiple languages. The language files are located in the `lang` folder and are JSON files.

Each string is identified by a unique key and is used to display the application in the selected language. To be able to use a new language, you will have to create a new JSON file in the `lang` folder and fill it with the translations.

Any string that is not found in the language file 

### Current keys supported

- `language_name` : The name of the language in its own language

## Pattern

The pattern is a string that contains characters and digits. Any character that is not a digit are used as is, while the digits are replaced by a character from the corresponding charset.

A character weight determines the probability of a character to be chosen among the charset.

For example, if using the charset above `default_english.json`, the pattern `1` will be replaced by :
- `a` 12 times out of 32
- `e` 16 times out of 32
- `i` 4 times out of 32

The special digit `0` means that the charset choice is random, before replacing the digit by a character.

### Regex, quantifiers and groups

Once the digits has been translated to chars, the pattern can use regex-like characters, such as `?`, `*`, `+`, `|`, `(` and `)`. The application uses the third-party library [exrex](https://github.com/asciimoo/exrex) to parse the pattern and generate a word from it.