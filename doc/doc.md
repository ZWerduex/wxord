# Documentation

## Word Generation

### Charset files

A charset is a representation of an alphabet and how often each character is used. It is a JSON file that contains a few info about itself, along with the characters and their weights. It is located in the `charsets` folder and you can create your own charset file or modify an existing one to change the character set used by the application.

Currently, the application uses a single charset file, which has been defined statically. However, you can change the charset used by tweaking directly the `basic_french` JSON file in the `charsets` folder.

Below is an example of a charset file, further used as a reference in the documentation.

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

The `charsets` field is an array of objects, each object being a set of key-value pairs. The key is a character and the value is the weight of the character. The weight is used to determine the probability of a character to be chosen when generating a word from a pattern.

### Pattern

The pattern is a string that contains characters, digits and reserved symbols. Any character that is not a digit is used as is, while digits are replaced by a character from the corresponding charset.

#### Digits

A digit shows the charset to be used to replace it. `1` implies that the first charset will be used and the same logic goes for `2` and `3`. The special digit `0` means that the charset choice is uniformly random. A zero will be evaluated to a digit from `1` to `3` and the character will be then chosen from the corresponding charset as described below.

The weight of a character is used to determine its probability to be chosen. All the weigths in a charset are summed up, and a given character has a probability of `weight / sum_of_weights` to be chosen. For example, if using the charset file above called `default_english.json`, the digit `1` will be replaced by :
- `a` 12 times out of 32
- `e` 16 times out of 32
- `i` 4 times out of 32

#### Characters

Characters are anything that are not digits nor reserved symbols. They are used as is and are not replaced by anything. It is useful to force a character to be present in the generated word at a specific position. Interesting use cases include :
- Specific sounds, like `th` in english or `ch` in french
- Spaces, to generate sentences or expressions rather than words
  - You can then use articles before words, like `the` in english or `des` in french
- Special characters that can occur, like `'` or `-`
- Enforce plural form of a word by adding an `s` at the end of the pattern

#### Reserved symbols

Reserved symbols are used in the pattern to specify a generation behavior. Those symbols are :

- Quantifiers
  - `?` : The token before the `?` is optional. It can be present or not in the generated word
  - `*` : The token before the `*` can be present any number of times, including 0
  - `+` : The token before the `+` can be present any number of times, but at least once
- Parenthesis
  - `(` and `)` : The tokens between the parentesis are grouped together. Possible quantifiers are applied to the whole group
- Operators
  - `|` : Evaluated to a logical OR. One of the two tokens before and after the `|` will be chosen to be present in the generated word

## Language files

Although not able to be changed while the application is running, this one plans to support multiple languages. The language files are located in the `lang` folder and are JSON files.

Each string is identified by a unique key and is used to display the application in the selected language. To be able to use a new language, you will have to create a new JSON file in the `lang` folder and fill it with the translations for each required key.

Any string with a given key that is not found in the language file is evaluated to the key itself. This is useful to identify missing translations in the language file.

Some strings take parameters into account. They must include in themselves the name of each parameter surronded by brackets, so they can be formatted later using the `format` method of `str` Python class.

The example below shows a string with a parameter named `nb`.
```json
"Status_GeneratedWords": "Generated {nb} words"
```

In the next subsection, documentation indicates a list of required parameters for a given string if there is any.

### Current keys supported

#### Header section
- `language_name` : Name of the language in its own language
- `HeaderAuthor_text`: Expression indicating who is the author
  - `author` : the author of the application (`Z-WX`)

#### Generation panel
- `PatternInput_placeholder` : Placeholder of the input used to enter the pattern
- `MaxLengthInput_label` : Label of the combobox used to choose the maximum length of the generated words
- `BatchSizeInput_label` : Label of the combobox used to choose the amount of words to generate
- `GenerateButton_text` : Text of the button used to generate a word

#### Charsets panel
- `SuggestedPatterns_placeholder` : Placeholder of the combobox used to choose a suggested pattern
- `OrderByCharButton_text` : Text of the button used to order a charset in alphabetical order
- `OrderByWeightButton_text` : Text of the button used to order a charset by weight

#### Footer section
- `Status` : Used as the title for the status bar in the footer
- `Status_GeneratedWord` : Status message to indicate how much words were generated
  - `nb` : amount of generated words (`0` or `1`)
- `Status_GeneratedWords` : Plural form of `Status_GeneratedWord`
  - `nb` : amount of generated words (`2` or more)
- `Status_PatternIsEmptyNoWordGenerated` : Status message indicating that the pattern is empty and no word can be generated
- `Status_WordSentToPatternInput` : Status message indicating that a word is used as the pattern
  - `word` : word used as the new pattern
- `Status_WordSentToClipboard` : Status message indicating that a word has been copied, sent to the clipboard
  - `word` : the copied word
- `Status_LanguageChanged` : Status message indicating that language changed
  - `lang` : the new language name as specified in the language file by the `language_name` key

## Ressources

- [League Spartan font](https://www.theleagueofmoveabletype.com/league-spartan) : Used for the application logo
- [Montserrat font](https://fonts.google.com/specimen/Montserrat) : Used for the application UI
- [WordGen website](https://www.wordgen.eu/#!en/generator/from-letters) : Inspired the application idea
- [ANTLR4](https://www.antlr.org/) : Used to parse the pattern and generate words