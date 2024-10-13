import pyperclip,re
from itertools import zip_longest
arr3=[]
phoneNumber=re.compile(r'\d\d\d-\d\d\d\d-\d\d\d')
inputText=str(pyperclip.paste())
arr1=phoneNumber.findall(inputText)

mail=re.compile(r'''(
\S+
.com
)''',re.VERBOSE)
arr2=mail.findall(inputText)

for item1, item2 in zip_longest(arr1, arr2):
        if item1 is not None:
            arr3.append(item1)
        if item2 is not None:
            arr3.append(item2)


if(len(arr3)>0):
    pyperclip.copy('\n'.join(arr3))
    print("copied to clipboard")
    print("\n".join(arr3))
else:
    print("no phone number or email address found")

    