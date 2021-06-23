'''
FilePath (muse exist)

DirectoryPath (must exist)

EmailStr (validates given str for email automatically)

NameEmail (accepts <fred.bloggs@example.com> type of emails)

PyObject (expects a string and checks if given python object is importable at the dotted path: `requests.get`),

AnyUrl

AnyHttpUrl

HttpUrl (stricter than AnyHttpUrl)

PaymentCardNumber

UUID1-5

IPvAnyAddress

Negative/Positive Int/Float
'''