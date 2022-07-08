
def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())

Dictionary_Books = {}
def Books():
    print("---" * 35)
    print("Book_ID".ljust(17), "Book_Name".ljust(30)  + "Author".ljust(20) + "Quantity".ljust(17) + "Price".ljust(15))
    print("---" * 35)

    file = open('books.txt', 'r')
    i = file.readlines()
    for each in i:
        splitList = each.split(',')
        bookID = splitList[0]
        title = splitList[1].ljust(25)
        if len(title) > 25:
            title = title[0:22].ljust(25, '.')
        author = splitList[2].ljust(25)
        quantity = splitList[3].ljust(15)
        price = splitList[4].ljust(15)

        print(bookID.ljust(15) + title + " " * 5 + author + quantity + price)
        Dictionary_Books[int(splitList[0])] = [splitList[1].strip(), splitList[2].strip(), int(splitList[3].strip()), splitList[4].strip()]
        #print("\n",Dictionary_Books)
        print("\n")
    file.close()
borrowedBooks = []
borrowedID = []

# code for borrowing a book
def borrowBook():
    sum = 0
    date = getDate()
    time = getTime()
    bookIDList = []
    for each in Dictionary_Books:
        bookIDList.append(each)
    try:
        bookID = int(input("Enter book id to borrow book: "))
    except:
        print("integir value only...")

    if bookID not in bookIDList:
        print("\n" + "++" * 30 + "\n")
        print("Please provide a valid Book ID !!!".center(50) + "\n" + "++" * 30 + "\n")
        borrowBook()

    if bookID in bookIDList:
        
        borrowedBooks.append(Dictionary_Books[bookID][0])
        borrowedID.append(bookID)
        quantity = Dictionary_Books[bookID][2]
        if quantity == 0:
            print("\n" + "++" * 30 + "\n" + "Book is not available!!!".center(50) + "\n" + "++" * 30 + "\n")
            Main.main()

        else:
            print("\n" + "++" * 30 + "\n" + "Book is available!!!".center(50) + "\n" + "++" * 30 + "\n")
            while(True):
                name = str(input("Enter the Name of person who borrowed book: "))
                if name.isalpha():
                    break
                print("please input alphabet from A-Z")
                
            price = Dictionary_Books[bookID][3]
            print("The price of book is: ",price)
            print("The date is :",date)
            print("The time is :",time)
            
            

            Dictionary_Books[bookID][2]-= 1

            with open('books.txt', 'w') as f:
                for i in range(1, 6):
                    f.write(str(i))
                    f.write(",")
                    for j in range(4):
                        if(j == 3):
                            
                            f.write(str(Dictionary_Books[i][j]))
                        else:
                            f.write(str(Dictionary_Books[i][j]))
                        f.write(", ")
                    f.write("\n")


            print("List after a Borrow: ")
            Books()
            print("Has This Person Borrowed Another Book?")
            AnotherBook = input("If yes then type Y ,if not they type n: ")
            if AnotherBook.lower() == "y":
                #for multiple books burrowing
                moreBooks()
                

            for x in(borrowedID):
                p = Dictionary_Books[x][3]
                price = p[1:]
                sum = sum + float(price)
                print(borrowedBooks)
                sum = "{:.2f}".format(sum)
                print("\n"+"++" * 30)
                print("Customer Bill!!!".center(50)+ "\n" + "++" * 30 + "\n")
                print("Name of Customer: ",name)
                print("Sum is $",sum)
                 
                print("Name of Books Borrowed: ")
                 
                for i in(borrowedBooks):
                    print(i)
                 
                t = "Borrow_"+ name+ ".txt"
                with open(t,"w+") as file:
                     file.write("               Library Management System  \n")
                     file.write("                   Borrowed By: "+name+"\n")
                     file.write("Customer Bill!!!".center(50)+ "\n" + "++" * 30 + "\n")
                     file.write("    Date: " + getDate()+"    Time:"+ getTime()+"\n\n")
                     file.write("Total Price of Books: "+str(sum) +"\n")
                     file.write("Books Borrowed are: "+"\n")
                     
                     for books in (borrowedBooks):
                         file.write(books + "\n")
                    
                 
                file.close()
                borrowedBooks.clear()
                borrowedID.clear()

                print(("+=+=" * 30))
                print("Thanks for burrowing a book")
                print(("+=+=" * 30))

     
     

def moreBooks():   
    
    bookIDList = []
    for each in Dictionary_Books:
        bookIDList.append(each)
    bookID = int(input("Enter ID of another borrowed book: "))

    if bookID not in bookIDList:
        print("\n" + "++" * 30 + "\n")
        print("Please provide a valid Book ID !!!".center(50) + "\n" + "++" * 30 + "\n")
        moreBooks(sum)

    borrowedID.append(bookID)
    borrowedBooks.append(Dictionary_Books[bookID][0])
    price2 = Dictionary_Books[bookID][3]
    print("The price of book is: ",price2 + "\n")
    print("Has This Person Borrowed Another Book?")
    AnotherBook = input("If yes then type Y ,if not they type n: " )
    if AnotherBook.lower() == "y":
        moreBooks()
    else:
        return


def ruturn_books():
    total = 0.0
    bookIDList = []
    for each in Dictionary_Books:
        bookIDList.append(each)
    while(True):
        name = str(input("Enter the Name of person who returned book: "))
        if name.isalpha():
            break
        print("please input alphabet from A-Z")
        
    try:
        bookID = int(input("Enter book id to ruturn book: "))
        if bookID not in bookIDList:
            print("\n" + "++" * 30 + "\n")
            print("Please provide a valid Book ID !!!".center(50) + "\n" + "++" * 30 + "\n")
            
        if bookID in bookIDList:
            borrowedBooks.append(Dictionary_Books[bookID][0])
            borrowedID.append(bookID)
            Dictionary_Books[bookID][2]+=1 

            
        total = total+float(Dictionary_Books[bookID][3])                
        print("\t\t\t\t\t\t\t"+"$"+str(total))
        print("Is the book return date expired?")
        print("Press Y for Yes and N for No")
        b="Return-"+name+".txt"
        stat=input()
        if(stat.upper()=="Y"):
            print("By how many days was the book returned late?")
            day=int(input())
            fine=2*day
            with open(b,"w+")as f:
                f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
            total=total+fine
        print("Final Total: "+ "$"+str(total))
        with open(b,"w+")as f:
            f.write("                Library Management System \n")
            f.write("                   Returned By: "+ name+"\n")
            f.write("    Date: " + getDate()+"    Time:"+ getTime()+"\n\n")
            f.write("The book you returned"+"\n")
            for books in (borrowedBooks):
                f.write(books + "\n")
            f.write("\t\t\t\t\tTotal: $"+ str(total))
            f.close()
            borrowedBooks.clear()
            borrowedID.clear()

        with open('books.txt', 'w') as f:
            for i in range(1, 6):
                f.write(str(i))
                f.write(",")
                for j in range(4):
                    if(j == 3):
                        f.write(str(Dictionary_Books[i][j]))
                    else:
                        f.write(str(Dictionary_Books[i][j]))
                        f.write(", ")
                f.write("\n")
    except:
        print("entrt a intiger i.e. 1,2,3,....")
            
        




