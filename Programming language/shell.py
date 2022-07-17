from cgitb import text
import basic

while True:
    text = input("basic > ")
    #text = "d * 1"
    result, error = basic.run("<stdin>", text)

    if error: print(error.as_string())
    else: print(result)