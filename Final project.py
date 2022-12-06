
from breezypythongui import EasyFrame

class Final (EasyFrame): #creates windows

    def __init__ (self):
        EasyFrame.__init__(self)
        self.addLabel(text="UserName",row=0 ,column=0 )
        self.UserInput =self.addTextField( "",row=0, column=1, columnspan = 2,
                                    width = 20,)

        self.addLabel(text="Password",row=1 ,column=0 )
        self.UserInput =self.addTextField( "",row=1, column=1, columnspan = 2,
                                    width = 20,)

        self.addLabel(text="",row=2 ,column=0 )
        self.UserInput =self.addTextField( "",row=2, column=1, columnspan = 2,
                                    width = 20,)

        self.addLabel(text="",row=3 ,column=0 )
        self.UserInput =self.addTextField( "",row=3, column=1, columnspan = 2,
                                    width = 20,)
     
        self.addLabel(text="Result",row=4 ,column=0 )
        self.UserOutput =self.addTextField(value=0, row=, column=1)
    

def main():
    Final().mainloop()

if __name__ =="__main__":
    main()

