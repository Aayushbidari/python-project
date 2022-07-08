import Funcutions
def main():
    while(True):
        print("===" * 30)
        print("Hello and Welcome to library management system".center(100))
        print("===" * 30+ "\n\n")
        Funcutions.Books()
        print("Enter 1 to Borrow a Book")
        print("Enter 2 to Return a book")
        print("Enter 3 to Terminate")
        
        try:
            number = int(input("Please enter a number: "))
        
            print()
            if(number==1):
                print("===" * 30)
                print("You will now borrow a book")
                print("===" * 30+ "\n\n")
                Funcutions.borrowBook()
                
            elif(number==2):
                print("===" * 30)
                print("You will now reuturn a Book")
                print("===" * 30+ "\n\n")
                Funcutions.ruturn_books()
            elif(number==3):
                print("---"* 30)
                print("\n Thank you for using Library management system\n".center(100))
                print("---"* 30)
                break
            else:
                print("++" *30)
                print("Invalid Input!!\n Please enter 1, 2 or 3")
                print("++" *30+ "\n\n")
        except:
            print("Enter number(intiger only..)")


main()



