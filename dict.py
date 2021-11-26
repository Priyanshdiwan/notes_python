
dic1 = {}
print(type(dic1))
dic2 = {"jord":"godfood", "blacky":"dosa", "sikh":"chicken", "balla":{"b":"fo", "L":"roti"}}
print(dic2["balla"]["b"])

dic2["nidhi"]= "vegan"#add into dictionary
print(dic2)

del dic2["nidhi"] # delete from dictionary
print(dic2)

# dic3 = dic2.copy; creates same dictionary d3 as d2  
dic3 = dic2 # if we don't use the copy function snd delete something from
#d3 it will also be deleted in d2
del dic3["blacky"]

print(dic2)

dic2.update({"nidhi":"vegan"}) #aise bhi update kar sakte hai
print(dic2)#ya line9 wale code se bhi update kar sakte hai

print(dic2.items())
print(dic2.keys())


dict={"apple":"its a fruit", "lock":"taala", "up":"upar", "down":"neeche" }

print("search for a word")
x=input()
print(dict[x])
