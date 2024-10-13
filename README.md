# Phone Number and Email Extractor

This Python script extracts phone numbers and email addresses from any text copied to the clipboard and copies them back to the clipboard. It uses regular expressions for pattern matching and `pyperclip` for clipboard operations.

## Features

- **Phone Number Extraction**: Extracts phone numbers in the format `XXX-XXXX-XXX`.
- **Email Extraction**: Extracts email addresses ending with `.com`.
- **Clipboard Integration**: The script automatically reads text from the clipboard and copies the extracted data back to the clipboard.
- **Regex-Based Matching**: Uses regular expressions for efficient and accurate extraction.

## Requirements

- Python 3.x
- The following Python packages:
  - `pyperclip`
  - `re`

Install the required packages by running:

```bash
pip install pyperclip

## Script Explanation

### Regex Patterns

- **Phone Number**: The phone number pattern is `\d\d\d-\d\d\d\d-\d\d\d`, which matches a format like `123-4567-890`.  
  You can modify the pattern to match different formats, such as including parentheses or country codes.

- **Email Address**: The email pattern used is `\S+.com`, which matches any string of characters followed by `.com`. You can enhance this pattern to support other domains or stricter email validation as needed.

### Code Overview

- **Clipboard Handling**: The script uses `pyperclip.paste()` to get the text copied to the clipboard.
- **Regex Search**: It uses Python's `re` module to search for phone numbers and emails in the clipboard text.
- **Data Collection**: The phone numbers and emails are stored in separate lists (`arr1` and `arr2`), and are combined into a single list (`arr3`) using `zip_longest` from the `itertools` module.
- **Clipboard Output**: If any data is found, it is copied back to the clipboard using `pyperclip.copy()`.

## Future Improvements
- **Flask API**: I plan to convert this script into a Flask API soon, allowing for more versatile usage and integration into web applications.
