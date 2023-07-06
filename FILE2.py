class FileHandling:
    def main():
        x=str(input("Enter a file name"))
        y=str(input("Enter a text in file"))
        b=open(x,"w")
        b.write(y)
        b.close()
        print(x,"\nFile created successfully")
        print("\n\t\t----Reading File Contents---")
        z=open(x,"r")
        print("\n")
        print(z.read())
FileHandling.main()        
             