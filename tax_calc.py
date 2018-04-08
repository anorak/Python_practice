#!/usr/bin/env python3

tax_code = {"499" : 10,"1499" : 15,"2499" : 20,"2500" : 30}
income = 0
tax = 0
selection = 'y'
run = 1

while run == 1:
    print ('Weekly Average Tax Witholding Calculator')
    print ('======================================== \n')
    income = int(input('Enter your income: $ '))
    
    print ('======================================== \n')

    if income < 500:
        tax = ((income / tax_code["499"]) * 1.00)
        print ('Your income is: \t $',income)
        print ('Your tax rate is: \t', tax_code["499"],'%')
        print ('Your tax is: \t \t $', round(tax,2))
    elif income < 1500:
        tax = ((income / tax_code["1499"]) * 1.00)
        print ('Your income is: \t $',income)
        print ('Your tax rate is: \t', tax_code["1499"],'%')
        print ('Your tax is: \t \t $', round(tax,2))
    elif income < 2500:
        tax = ((income / tax_code["2499"]) * 1.00)
        print ('Your income is: \t $',income)
        print ('Your tax rate is: \t', tax_code["2499"],'%')
        print ('Your tax is: \t \t $', round(tax,2))
    elif income > 2500:
        tax = ((income / tax_code["2500"]) * 1.00) 
        print ('Your income is: \t $',income)
        print ('Your tax rate is: \t', tax_code["2500"],'%')
        print ('Your tax is: \t \t $', round(tax,2))
        
    selection = str(input('\nContinue (y/n)? '))
    if selection == 'y':
        run = 1
    elif selection == 'n':
        print ('\nGoodbye!')
        run = 0