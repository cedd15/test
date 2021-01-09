class Nums:
    def __iter__(self):
        self.a = 1
        return self

    @property
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myclass = Nums()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
