# Author JRI 1/17/22

print('Enter the net sales for')

try:
    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))
    change = (current - previous) * 100 / previous
    
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'
    print(result)
except ValueError:
    print("Invalid input, enter numerical values for prior and current periods.")
except ZeroDivisionError:
    print("Invalid input, enter a value that is not zero.")
finally:
    print("Thank you for using my program!")