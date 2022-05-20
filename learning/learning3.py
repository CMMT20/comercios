for i in range(15):
    print(f'var{i+1} = ""')


var1 = "What i want "
var2 = "is to join these vars "
var3 = "without type all them again.\n"
var4 = "It has a lot of sense, if i have 100 vars, "
var5 = "man i dont want to type 100 vars.\n"
var6 = "I prefer 2 lines of code, of course.\n"
var7 = "Long live for for loops!\n"
var8 = "And this other text only "
var9 = "purpose "
var10 = "is "
var11 = "to make this text longer "
var12 = "to see better my point.\n"
var13 = "I dont want to type 15 vars, "
var14 = "I dont want to type 100 vars.\n"
var15 = "Goodbye."


var0 = ''
for i in range (15):
    var0 += locals()[f"var{str(i+1)}"]

print(var0)
