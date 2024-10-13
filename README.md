<readme>
  <title>ContactPaserAPI</title>
  
  <description>
    This Python script extracts phone numbers and email addresses from clipboard content using regular expressions. 
    It merges the results from both lists (phone numbers and emails) alternately and copies them back to the clipboard. 
    The script supports cases where either list may be empty.
  </description>
  
  <features>
    <feature>Regex-based pattern detection:</feature>
    <feature>Extracts phone numbers in the format XXX-XXXX-XXX.</feature>
    <feature>Extracts email addresses ending with .com.</feature>
    <feature>Merges lists alternatively: Uses the itertools.zip_longest() function to handle merging of phone numbers and emails, even if the lists are of unequal length.</feature>
    <feature>Clipboard integration: Uses pyperclip to automatically copy the extracted phone numbers and email addresses back to the clipboard.</feature>
  </features>
  
  <requirements>
    <requirement>Python 3.x</requirement>
    <requirement>pyperclip library: Install it using pip: <code>pip install pyperclip</code></requirement>
  </requirements>
  
  <usage>
    <step>1. Copy some text to your clipboard containing phone numbers and/or email addresses.</step>
    <step>2. Run the script: <code>python extract.py</code></step>
    <step>3. If phone numbers or email addresses are found, they will be printed in the terminal and copied to your clipboard for easy access.</step>
  </usage>
  
  <codeExplanation>
    <section>
      <header>Phone number and email extraction:</header>
      <content>The script uses regular expressions to detect phone numbers in the XXX-XXXX-XXX format and emails ending in .com.</content>
    </section>
    <section>
      <header>Merging lists:</header>
      <content>The zip_longest() function from itertools is used to merge the two lists (phone numbers and emails) alternately. It handles cases where one list may be longer than the other, and if one list is empty, the other list is still processed.</content>
    </section>
    <section>
      <header>Clipboard operations:</header>
      <content>The script uses the pyperclip library to fetch content from the clipboard, process it, and then copy the results back to the clipboard.</content>
    </section>
  </codeExplanation>
  
  <example>
    <clipboardContent>
      John's number is 123-4567-890. You can email him at john@example.com.
    </clipboardContent>
    <extractedResult>
      123-4567-890
      john@example.com
    </extractedResult>
  </example>
  
  <futurePlans>
    <plan>Convert this script into a REST API using Flask for broader use in web applications.</plan>
  </futurePlans>
  
  <license>
    This project is licensed under the MIT License - see the LICENSE file for details.
  </license>
</readme>
