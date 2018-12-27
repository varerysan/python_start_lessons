class Foo:
    def __getitem__(self, pos):
        print("--- try get pos=", pos)
        err = False
        try:
            res =  range(0, 30, 10)[pos]
            print("for pos=", pos, " we get res=", res)
            return res
        except IndexError:
            print("=== Except IndexError")
            err = True

        if err:
            raise IndexError


f = Foo()

for i in f:
    print("i=", i)

if 20 in f:
    print("20 in f")


if 15 in f:
    print("15 in f")
else:
    print("15 not in f")

