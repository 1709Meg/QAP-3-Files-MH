# Library of functions for formatting numbers and dates.

import datetime

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to #,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to #,###.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to ####.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to ####.#.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to ####.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr


def ValidateEmpty(Prompt, ErrorMsg):
    # Function will validate empty string.

    while True: 

        StringValue = input(Prompt)

        if StringValue == "":
            print(ErrorMsg)
        else:
            break

    return StringValue
        

def ValidateFName():
    CustFName = ValidateEmpty("Enter first name (END to quit):           ",
                              " ** Data Entry Error - Customer first name cannot be blank **")
    return CustFName.title()
            

def ValidateLName():
    CustLName = ValidateEmpty("Enter last name:                          ",
                              " ** Data Entry Error - Customer last name cannot be blank **")
    return CustLName.title()

def ValidatePhone():
    while True:
        CustPhone = ValidateEmpty("Enter phone number:                       ",
                              " ** Data Entry Error - Customer phone number cannot be blank **")
        if len(CustPhone)  != 10:
            print("** Data Entry Error - Phone number must be 10 digits **")
        else:
            break

    return CustPhone 

def ValidatePlate():
    while True: 
        PlateNum = ValidateEmpty("Enter licence plate number:               ",
                              " ** Data Entry Error - Licence Plate Cannot Be Blank **")
        if len(PlateNum) != 6:
            print("** Data Entry Error - Licence plate must be 6 characters **")
        elif (PlateNum [0:3].isalpha() == False) or (PlateNum [3:].isdigit() == False):
            print("** Data Entry Error - Licence plate must be entered in format XXX999 **")
        else:
            break
    return PlateNum.upper()
    
def ValidateSalesName():
    SalesName = ValidateEmpty("Enter sales person name:                  ",
                              " ** Data Entry Error - Sales person name cannot be blank **")
    return SalesName.title()






