class cat:
    def age(self):
        print(self.name)


cat1 = cat()
cat1.name = 'ssr'
cat1.age()


# 在类封装的方法内部，self.就表示当前调用方法的对象自己
# 结果：ssr
#-----------------------------------------------------------------------------------------
#这个 初始化方法 就是 init 方法， init 是对象的内置方法
class dog:
    def __init__(self):
        print("初始化")

    def cat(self):
        print(self.name)


tom = dog()
tom.name='tom'
tom.cat()
#结果：初始化<br>tom
#-----------------------------------------------------------------------------------------
#改造初始化方法——初始化的同时设置初始值
class dog:
    def __init__(self,name):
        print('初始化,{0}'.format(name))


tom = dog('XXOO')
#结果：初始化，XXOO