class DivsionByZeroError(BaseException):pass
while True:
    try:
        a = int(input("Enter First Number:"))
        b = int(input("Enter second Number:"))
        try:
            if b == 0:
                raise DivsionByZeroError
            res = a/b
            print(res)
            break
        except DivsionByZeroError as e:
            print("\t\tDont Enter Zero",{repr(e)})
    except ValueError:
        print("\t Accept only Numbers")