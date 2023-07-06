class FileRead:
    def main():
        a=open("sample.txt","r")
        print(a.read())
    def main_2():
        b=open("text.txt","w")
        b.write("Google")
        print("File created successfully")
        b.close()
FileRead.main()
FileRead.main_2()
         
             
    