# def Name_printer(a,b,c,d):
#     print(a,b,c,d)
# Name_printer("priyansh","yogesh","nidhi","yash","yukti")
#  error dega expected 4 arguemnt getting 5 kar ke ab ya to mai abcd ke baad e add kar du
# per jab apan millions of users ka data handle karte hai to aisa kaam to chalega nhoi na
#  there fore we use args

Name=["priyansh","yogesh","nidhi","yash","yukti"]
name_discription={"priyansh":"jord","yogesh":"airtel","nidhi":"teacher"}


def noiceagrs(title,*args,**kwargs):
 print(title)
 for ch in args:
    print(ch)
 for elemnt in name_discription.items():
     print(elemnt)
noiceagrs("the name is",*Name,**name_discription)
# vo args aur kwargsvo kuch bhi likh sakte ho per args ek general convention haoi
# hamesha normal argument ko args se pehle dena chahiye aur args ke baaad kwargs 
#  like even if you write argss and kwargs and dont give them a command tab bhi error throw nhi hoga

