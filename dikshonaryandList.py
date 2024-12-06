Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dikshonary - {"uhoro":"hello", "waku":"yours", "njamba":"man"}
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dikshonary - {"uhoro":"hello", "waku":"yours", "njamba":"man"}
NameError: name 'dikshonary' is not defined
dikshonary = {"uhoro":"hello", "waku":"yours", "njamba":"man"}
for maritwa in dikshonary:
    print (maritwa+" means "+ dikshonary[maritwa])

    
uhoro means hello
waku means yours
njamba means man
newlist = ["uhoro","waku","njamba"]
for words in newlist:
    print (words + " is a kikuyu word")

    
uhoro is a kikuyu word
waku is a kikuyu word
njamba is a kikuyu word
for words in newlist:
    print(words)

    
uhoro
waku
njamba
mixedLangDict = {"kikuyu":["uhoro","waku","njamba"], "english":["hello","yours","man"]
                 }
for words in mixedLangDict:
    for lists in words:
        print 
KeyboardInterrupt
for lists in mixedLangDict:
    for words in mixedLangDict[lists]:
        print (lists+"words are" +words)

        
kikuyuwords areuhoro
kikuyuwords arewaku
kikuyuwords arenjamba
englishwords arehello
englishwords areyours
englishwords areman
for lists in mixedLangDict:
    