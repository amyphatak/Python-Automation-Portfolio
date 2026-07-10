ItemsInCart= 0
if ItemsInCart!=2:
    raise Exception ("products cart count not matching")

try:
    with open('filelog.txt', 'r') as reader:
     reader.read()

except:
    print("somehow i reached this block beacuse there is failure in try block")
