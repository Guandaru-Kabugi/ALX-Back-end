class Replit:
    def execute(self):
        print("compiling")
        print("running") 
        print("check errors")
class VsCode:
    def execute (self):
        print("compiling")
        print("running")

class Laptop:
    
    def code (self, ide):
        ide.execute()
ide = Replit()
lap1 = Laptop()
lap1.code(ide)