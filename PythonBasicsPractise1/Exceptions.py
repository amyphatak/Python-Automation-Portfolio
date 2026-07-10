from logging import raiseExceptions

itemsInCart = 0

if itemsInCart != 2:
  #  raise Exception("product does not match ")
    pass
assert(itemsInCart==0)

#try ,  catch
try:
 with open('Testfeee.txt', 'r') as reader:
        reader.read()
except:
    print( "Somehow i reached this block")


try:
 with open('Testrfrf.txt', 'r') as reader:
        reader.read()
except Exception as e: # when you want to know what exact message has been thrown by try
    print(e)
finally:
    print( "cleaning up")
