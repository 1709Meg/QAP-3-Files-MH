# Description: Honest Harry (Used Car Lot)
# Author: Megan Hickey
# Date(s): November 15th


# Define required libraries.

import FormatValues as FV
import datetime

# Define program constants.

LICENCE_FEE_STAND = 75.00 
LICENSE_FEE_LUX = 165.00
TRANSFER_FEE = .01
LUX_TAX = .016
HST_RATE = .15
TODAY = datetime.datetime.now()

# Define program functions.


def CalcLicenceFee(SellingPrice):
    LicenceFee = 0
    if SellingPrice <= 15000:
        LicenceFee = LICENCE_FEE_STAND
    else:
        LicenceFee = LICENSE_FEE_LUX
    
    return LicenceFee

def CalcTransferFee(SellingPrice):
    TransferFee = 0

    if SellingPrice <= 20000:
        TransferFee = TRANSFER_FEE * SellingPrice
    else: 
        TransferFee = (TRANSFER_FEE * SellingPrice) + (LUX_TAX * SellingPrice)
    
    return TransferFee

def ValidateSellingPrice():
    while True: 
        try:
            SellingPrice = float(input("Enter the selling price:                  "))
            if SellingPrice > 50000:
                print("** Data Entry Error - Selling Price Cannot Exceed 50,000 **")
            else:
                return SellingPrice
        except:
            print("** Data Entry Error - Invalid Number **")
     
def ValidateTradeIn(SellingPrice):
    while True: 
        try:
            TradeIn = float(input("Enter the trade in price:                 "))
            if TradeIn > SellingPrice:
                print("** Data Entry Error - Trade In Price Cannot Exceed Selling Price **")
            else:
                return TradeIn
        except:
            print("** Data Entry Error - Invalid Number **")



# Main program starts here.

while True:
    
    # Gather user inputs.

    print()
    print()
    print("Honest Harry Car Sales")
    print("Please enter the following")
    print()

    CustFName = FV.ValidateFName()

    if CustFName.upper() == "END":
        break

    CustLName = FV.ValidateLName()

    CustPhone = FV.ValidatePhone()
    print()
    PlateNum =  FV.ValidatePlate()

    CarMake = input("Enter the car make:                       ").title()

    CarModel = input("Enter the car model:                      ").title()
    
    CarYear = input("Enter the year the car was made:          ")
    print()

    SellingPrice = ValidateSellingPrice()

    TradeIn = ValidateTradeIn(SellingPrice)
    print()
    SalesName = FV.ValidateSalesName()
    print()


    # Formatting values.
    
    InvDate = TODAY.strftime("%b-%d-%Y")

    CustName = CustFName[0] + "." + " " + CustLName

    PhoneNum = "(" + CustPhone[0:3] + ")" + CustPhone [3:6] + "-" + CustPhone [6:]

    CarDetails = CarYear + " " + CarMake + " " + CarModel

    RecID = CustFName[0]+ CustLName[0] + "-" + PlateNum[3:] + "-" + CustPhone[6:]

    # Further calculations.

    PriceAfterTrade = SellingPrice - TradeIn

    LicenceFee = CalcLicenceFee(SellingPrice)

    TransferFee = CalcTransferFee(SellingPrice)

    Subtotal = PriceAfterTrade + LicenceFee + TransferFee

    HSTCost = HST_RATE * Subtotal

    TotalPrice = Subtotal + HSTCost

    FullName = CustFName + " " + CustLName

    # Financing loop

    Year = TODAY.year
    Month = TODAY.month
    Day = TODAY.day

    if Day >= 25:
        Month+= 2
    else:
        Month += 1

    if Month > 12:
        Month -= 12
        Year += 1

    FirstPayDate = datetime.date( Year, Month, 1)
    FirstPayDate = datetime.datetime.strftime(FirstPayDate, "%d-%b-%y")
    
    # Display results.


    print()
    print()
    print(f"Honest Harry Car Sales:                       Invoice Date:      {InvDate:>15s}")
    print(f"Used Car Sale and Receipt:                    Receipt No:        {RecID:>15s}")
    print()
    print(f"                                        Sale Price:                   {FV.FDollar2(SellingPrice):>10s} ")
    print(f"Sold to:                                Trade Allowance:              {FV.FDollar2(TradeIn):>10s}")
    print(f"                                        ----------------------------------------")
    print(f"      {CustName:<20s}              Price after Trade:            {FV.FDollar2(PriceAfterTrade):>10s}")
    print(f"      {PhoneNum:<10s}                     License fee:                  {FV.FDollar2(LicenceFee):>10s}")
    print(f"                                        Transfer fee:                 {FV.FDollar2(TransferFee):>10s}")
    print(f"                                        ----------------------------------------")
    print(f"Car Details:                            Subtotal:                     {FV.FDollar2(Subtotal):>10s}     ")
    print(f"                                        HST:                          {FV.FDollar2(HSTCost):>10s}")
    print(f"      {CarDetails:<30s}    ----------------------------------------")
    print(f"                                        Total sales price:            {FV.FDollar2(TotalPrice):>10s}")
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"                                     Financing     Total      Monthly")
    print(f"            # Years    # Payments      Fee         Price      Payment ")
    print(f"            ---------------------------------------------------------           ")
    for Years in range(1,5):
        NumPay = Years * 12
        FinanceFee = 39.99 * Years
        TotalCost = TotalPrice + FinanceFee
        MonthPay = TotalCost / NumPay
        print(f"               {Years:<2d}          {NumPay:<2d}         {FV.FDollar2(FinanceFee):^7s}   {FV.FDollar2(TotalCost):>10s}  {FV.FDollar2(MonthPay):>9s}    ")
    print(f"            ----------------------------------------------------------            ")
    print(f"            First payment date: {FirstPayDate}")
    print(f"--------------------------------------------------------------------------------")
    print(f"                        Best used cars at the best price!                       ")
    print()

    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.