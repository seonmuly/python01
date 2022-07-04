tupleFruits=("apple", "banana", "cherry") #Tuple
listFruits = ["apple", "banana", "cherry"] #List
print("original tuple:", tupleFruits)
print("original list: ",listFruits)
#เปลี่ยนค่าในtuple
x=list(tupleFruits)#แปลงเป็นlistแล้วเก็บในตัวแปรX
x[1]="blueberry"
tupleFruits=tuple(x)
print("launtuple: ", tupleFruits)
#เพิ่มค่าในtuple
x=list(tupleFruits)
x.append("melon")
tupleFruits=tuple(x)
print("เพิ่มค่าtuple: ", tupleFruits)
#ลบtuple
x=list(tupleFruits)
x.remove("cherry")
tupleFruits=tuple(x)
print("Antuple:", tupleFruits)
#join tuple
vage=("tomato","cucumber","onion")
fruitVege=tupleFruits+vage
print("join tuple:",fruitVege)
x = range(3,6)#จะหยุดก่อนค่าstop
for n in x:
    print("range x:",n)
y = range (3,20,2)
for m in y:
    print("range x:",m)
#ชื่อ น.ส.ขวัญหทัย สนิทกลาง เลขที่ 35