
def non_exception():
    pass

def exception():
    raise FileExistsError

def try_catch_else_finally():
    try:

        try:
            non_exception()
            exception()
            #exception()
        except ZeroDivisionError as cx:
            args = cx.args
            print(args)
        except:
            raise ArithmeticError
        else:
            print("else block")
            return True
        finally:
            return False

    except ZeroDivisionError:
        pass
    except FileExistsError:
        pass
    else:
        return 5
    finally:
        return 10

def try_catch_else_finally2():
    try:
        print("Outer TRY")

        try:
            print("Inner TRY")
            #raise ZeroDivisionError
        except:
            print("Inner EXCEPT")
        else:
            print("Inner ELSE")
            return
        finally:
            print("Inner FINALLY")


    except:
        print("Outer EXCEPT")
    else:
        print("Outer ELSE")
    finally:
        print("Outer FINALLY")

print(try_catch_else_finally2())
