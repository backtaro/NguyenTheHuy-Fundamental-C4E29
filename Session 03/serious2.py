# # 2.1
# sheep = [5, 7, 300, 90, 24, 50, 75]

# print("Hello, my name is Hiep and these are my sheeps size: ",sheep)

# # 2.2
# a = max(sheep)
# print("Now my biggest sheep has size",a,"let's sheer it ")

# # 2.3
# b = sheep.index(a)
# sheep[b]=8
# print("After shearing, here is my flock", sheep)

# # 2.4
# for (i, val) in enumerate(sheep):
#     sheep[i] = val+50
# print("One month has passed, now here is my flock", sheep) 

# # 2.5
# sheep = [5, 7, 300, 90, 24, 50, 75]

# print("Hello, my name is Hiep and here is my flock ",sheep)

# for i in range(3):
#     for (i, val) in enumerate(sheep):
#         sheep[i] = val+50
#     print("One month has passed, now here is my flock", sheep) 

#     x = max(sheep)
#     print("Now my biggest sheep has size",x,"let's sheer it ")

#     y = sheep.index(x)
#     sheep[y]=8
#     print("After shearing, here is my flock", sheep)

# 2.6
sheep = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Hiep and here is my flock ",sheep)

a = max(sheep)
print("Now my biggest sheep has size",a,"let's sheer it ")

b = sheep.index(a)
sheep[b]=8
print("After shearing, here is my flock", sheep)

for i in range(2):
    for (i, val) in enumerate(sheep):
        sheep[i] = val+50
    print("One month has passed, now here is my flock", sheep) 

    x = max(sheep)
    print("Now my biggest sheep has size",x,"let's sheer it ")

    y = sheep.index(x)
    sheep[y]=8
    print("After shearing, here is my flock", sheep)

for (i, val) in enumerate(sheep):
        sheep[i] = val+50
print("One month has passed, now here is my flock", sheep) 

z = sum(sheep)
print("My flock has size in total: ", z)
print("I would get",z,"*$2 = ",z*2)