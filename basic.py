Roll_no= {
    '4' : 'Purushotham',
    '5' : 'Dinesh',
    '13' : 'Sekhar',
    '20' : 'venkatesh',
    '22' : 'Sai_Krishna',
    '23' : 'Vara_Prasad',
    '25' : 'Nagendra',
    '29' : 'Srinu_Naik',
}
Number = input('enter your roll number')
print(f"Hello Mr.{Roll_no[Number]}! How are you doing today?")

is_good=False
if is_good:
    print("hello! nice to meat you ")

a=10
def Hello():
    global a
    a=9
    print(a)
    print('inside',id(a))

print(a)

Hello()
print('out side',a)


b=20
def some():
    b=11
    x=globals() ['b']
    print('inside b=',x,id(x))


some()
print('out side b=',b,id(b))
