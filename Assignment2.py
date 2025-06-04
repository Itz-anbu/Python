class Multiple_function():
    def subfields():
        Subfield =['Subfields in AI are:', "Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print(*Subfield, sep = '\n')
    def oddeven():
            Number = int(input("Enter:"))
            if Number%2==0:
                print(Number, 'is Even Number')
            else:
                print (Number, 'is Odd Number')
    def marr_eligible():
            Gender=input('Your Gender:')
            Age = int(input ('Your age:'))
            if Gender == 'Male' and Age>20:
                print('ELIGIBLE')
            elif Gender == 'Female' and Age>18:
                 print('ELIGIBLE')
            else:
                print ('NOT ELIGIBLE')
    def Percentage(a,b,c,d,e):
        print('Subject1=', a)
        print('Subject2=', b)
        print('Subject3=', c)
        print('Subject4=', d)
        print('Subject5=', e)
        Total= a+b+c+d+e
        Percentage = Total/5
        print('Total=', Total)
        print('Percentage =', Percentage) 
    def Triangle(H,B,A,C):
        print("Height of triangle =", H)
        print("Base of triangle =", B)
        print("Area Formula = (Height*Base)/2)")
        print ("Area of the given triangle =", (H*B)/2)
        print("Side of a triangle=", A)
        print("Other side of a triangle =", C)
        print ("Perimeter Formula = Base+Side1+Side2")
        print('Perimeter of the given triangle=', A+B+C)        
        