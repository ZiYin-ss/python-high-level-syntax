"""“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”"""


class Cat(object):
    def say(self):
        print('i am a cat')


class Dog(object):
    def say(self):
        print('i am a dog')


class Duck(object):
    def say(self):
        print('i am a duck')


animal = Cat
animal().say()
Cat().say()

animal_list = [Cat, Dog, Duck]
for i in animal_list:
    i().say()
    # 每个类都有一个共同的方法 叫say 叫多态
    # 所有类 都有一个共同的方法 方法名字也一样 这样这种类就为一种类型 这个就是多态(say做什么又不一样)

a = ["bobby1", "bobby2"]
b = ["bobby2", "bobby1"]
name_tuple = ["bobby3", "bobby4"]
name_set = set()  # 这个就是集合的关键字啊 set() 放这 就代表name_set是一个集合
name_set.add("bobby5")
name_set.add("bobby6")
a.extend(b)
# a继承b 也就是说 a里面有的都会显示 同时也给b里面的元素都加到a里面了 一起显示出来了
# 只要是可迭代的 都是可以传递到a里面去的 都是可以写在 extend(可迭代类型)
# 同时 类要是可以迭代的话 也可以继承 也可以加到a里面去的 extend(可迭代类)
print(a)
print(name_tuple)
print(name_set)

"""
    看上面的注释 应该能理解什么是鸭子类型
        并不是和具体的类型一样 比如 extend函数参数需要的是可迭代对象 也就是说不止是数组 哪怕类可迭代都是可以传递的
        此时 再回到最开始说的那句话  鸟像鸭子就是鸭子  
        也就是说不需要管你这个对象是什么 哪怕是类 函数等等 只要他符合某种特性 那么他就是这个东西
        比如 类符合列表的可迭代 那么在需要可迭代类型的地方 不仅列表是个鸭子(可以传) 这个类也可以认为是个鸭子(也可以)
    
    还有一个说法 是说 定义类时候 只需要定义一个共同的方法 (不好理解)
        每个类共同方法里面展示的不同又叫做多态 
"""
