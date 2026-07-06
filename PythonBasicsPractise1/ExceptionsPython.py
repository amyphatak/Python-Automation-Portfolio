Itemsincart = 0
# 2 items will be added to cart

if Itemsincart != 2:
   # raise Exception("products cart count not matching")
    pass
assert(Itemsincart==0)

#try , catch
try:
    with open('filelog.txt','r') as reader:
        reader.read()

except:
    print("somehoe i reached this block because there is failure in try block")