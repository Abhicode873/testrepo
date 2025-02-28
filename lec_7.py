##READING A FILE
f = open("demo.txt","r")
# data = f.read()
data = f.read(6)
print(data)
print(type(data))
f.close()

f = open("demo.txt","r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

print(type(line1))
f.close()

##WRITING A FILE 
#USING THE "w" CHAR
f = open("demo.txt","w")
f.write("I 4 to learn the good things from the world it wanted to teach me")
f.close()

#USING THE "a" CHAR  ###APPEND
f = open("demo.txt","a")
f.write("\nI 4 to travel the ancient palces and the architecure of that monument")
f.close()

##PYTHON CREATES THE FILE IF DOES NOT EXIST
f = open("hello.txt","a")
f.close()

#""r+""" open for reading and writing. the stream is positioned at the 
#beginning of the file ( which act like a pointer)
f = open("demo.txt","r+")
f.write("abc") #it overwrite the sentence from start
print(f.read()) #it reads the sentence from where the pointer will start
f.close()

#""w+"" which will truncate first and then it will write the sentence 
f = open("demo.txt","w+")
print(f.read()) 
f.write("abc")
f.close()

#""WITH"" syntax
with open("demo.txt","r") as f:
    data = f.read()
    print(data)        #here we are not using f.close() bcz with itself 
                    #be automatic f.close()

with open("demo.txt","w") as f:
     f.write("new data")

#DELETING THE FILE
import os

os.remove("hello.txt")

#PRACTICE QS
#Create a new file "practice.txt" using python.
# f = open("practice.txt","r")
# # data = f.read()
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#the approch should be 
with open("practice.txt","w") as f:
     f.write("Hi everyone\nwe are learning File I/O\n")
     f.write("using Java.\nI like programming in Java.")


#WAF that replace all occurences of "Java" with "python" inabove file
with open("practice.txt","r") as f:   
    data = f.read()

new_data = data.replace("Java","Python") #it replace the java by python
print(new_data)

with open("practice.txt","w") as f: #after overwriting we rewrite in the file
     f.write(new_data)


#SEarch if the word learning exists in the file or not.
def check_for_word():
       word ="learning"
       with open("practice.txt","r") as f:
            data= f.read()
            if(data.find(word) != -1): #we can write if(word in data)
              print("Found")
            else:
              print("Not FOund")
check_for_word()

#WAF to find in which line if the file does the word "learning" occurs first
#Print -1 if word not found.
def check_for_line():
    word = "learning"
    data = True 
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())

#From a file containning numbers separated by comma, print the count of even numbers
with open("file.txt","r") as f:
    data = f.read()
    print (data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else :
            num += data[i]




# count = 0
# with open("file.txt","r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#          if int(val) % 2 == 0:
#             count += 1
#          else :ValueError
# print(f"Skipping non-integer value: {val}")

# print(count)

