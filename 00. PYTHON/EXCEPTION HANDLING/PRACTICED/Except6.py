try:
    print("Hello world..1")
    try:
        print("Hello world..1.1")
    except:
        print("Hello inner hit ")
    finally:
        print("Final inner 1")
except:
    print("Main except hit ")
finally:
    print("Main outer Final ")





