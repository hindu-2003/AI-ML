#Program for Obtaining List of  special symbols from Given Line of Alpha Special Values
#FilterFunsEx7.py
Given_list = 'p$yth!on i^s a%n oo@p l&ang'
Exepected_list = ['$','!','^', '%', '@', '&']
spl = list(lambda val: val.isalnum(),Given_list )
print(spl)