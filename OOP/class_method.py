class AB:
    a = 100
    b= "hello"
    def printer(self,c): # have to use self
        print(c)

new_ab = AB()
print(new_ab.a)
new_ab.printer(3)