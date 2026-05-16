import random
import time
while True:
 print(" Easy ")
 print(" Medium")
 print(" Hard")
 print("Choose difficulty level (Easy/Medium/Hard): ")
 e=input().lower()
 if e=="easy":
   question=[
    {"Ques": "what is 12 + 15", "Ans": "27"},
    {"Ques": "what is 144 / 12", "Ans": "12"},
    {"Ques": "what is square root of 81", "Ans": "9"},
    {"Ques": "what is 7 * 8", "Ans": "56"},
    {"Ques": "what is 100 - 45", "Ans": "55"},

    {"Ques": "value of pi (approx)", "Ans": "3.14"},
    {"Ques": "what is 2 power 5", "Ans": "32"},
    {"Ques": "what is LCM of 4 and 6", "Ans": "12"},
    {"Ques": "what is HCF of 8 and 12", "Ans": "4"},
    {"Ques": "area of square with side 4", "Ans": "16"},

    {"Ques": "unit of force", "Ans": "newton"},
    {"Ques": "unit of current", "Ans": "ampere"},
    {"Ques": "speed = distance / ?", "Ans": "time"},
    {"Ques": "chemical symbol of oxygen", "Ans": "o"},
    {"Ques": "pH value of neutral solution", "Ans": "7"},

    {"Ques": "planet known as red planet", "Ans": "mars"},
    {"Ques": "largest planet in solar system", "Ans": "jupiter"},
    {"Ques": "sun is a", "Ans": "star"},
    {"Ques": "process of water cycle evaporation + condensation + ?", "Ans": "precipitation"},
    {"Ques": "gas used by plants in photosynthesis", "Ans": "carbon dioxide"},

    {"Ques": "full form of CPU", "Ans": "central processing unit"},
    {"Ques": "full form of RAM", "Ans": "random access memory"},
    {"Ques": "which is brain of computer", "Ans": "cpu"},
    {"Ques": "which language is used for web structure", "Ans": "html"},
    {"Ques": "which language is used for styling", "Ans": "css"},

    {"Ques": "python is interpreted or compiled", "Ans": "interpreted"},
    {"Ques": "keyword to define function in python", "Ans": "def"},
    {"Ques": "what is output of 5 % 2", "Ans": "1"},
    {"Ques": "what is output of 10 // 3", "Ans": "3"},
    {"Ques": "list is mutable or immutable", "Ans": "mutable"},

    {"Ques": "tuple is mutable or immutable", "Ans": "immutable"},
    {"Ques": "index starts from in python", "Ans": "0"},
    {"Ques": "loop for fixed iteration", "Ans": "for"},
    {"Ques": "loop for condition based", "Ans": "while"},
    {"Ques": "boolean values", "Ans": "true false"},

    {"Ques": "who invented computer", "Ans": "charles babbage"},
    {"Ques": "father of c language", "Ans": "dennis ritchie"},
    {"Ques": "national animal of india", "Ans": "tiger"},
    {"Ques": "national bird of india", "Ans": "peacock"},
    {"Ques": "capital of india", "Ans": "delhi"},

    {"Ques": "who wrote national anthem of india", "Ans": "rabindranath tagore"},
    {"Ques": "independence year of india", "Ans": "1947"},
    {"Ques": "largest ocean", "Ans": "pacific"},
    {"Ques": "smallest prime number", "Ans": "2"},
    {"Ques": "next prime after 7", "Ans": "11"},

    {"Ques": "what is 15 percent of 100", "Ans": "15"},
    {"Ques": "simple interest formula symbol", "Ans": "p r t"},
    {"Ques": "area of rectangle formula", "Ans": "l b"},
    {"Ques": "perimeter of square formula", "Ans": "4 a"},
    {"Ques": "what is 3/4 as decimal", "Ans": "0.75"}
   ]
   p=0
   m=0
   try:
      print("How many questions would you like to attempt  (enter only integer vlue)?") 
      o=int(input()) 
      selectedquestions=random.sample(question,k=o)
      start=time.perf_counter()
      for i in selectedquestions :
        print(i["Ques"])
        userans=input("enter the answer ....")
        if i["Ans"].lower()== userans.lower():
          print(" ✔️Score is 1 point...")
          p=p+1
        else:
          print(" ❌  Wrong answer.....")
          print("                    Correct Answer is...",i["Ans"])
          m=m+1
        print()
      end=time.perf_counter()
      print("Enter your name")
      user=input()
      print()
      print("Final Score Card:")
      print(" Name           :",user)
      print(" Total correct  :",p)
      print(" Total wrong    :",m)
      print(" Percentage     :",(p*100)/o,"%")
      print(" Total  time    :",(end-start))
      print()
      print(" can you play game again...(enter only yes/no)" )
      h=input ()
      print() 
      if h.lower()=="yes":
        continue
      else :
           print(f"Game Over!  Thanks for playing {user}")
           break
   except Exception as e: 
      print(" Invalid input  enter only Integer:")
      print()
      print("Restart now ...")
      print()  
      continue
 elif e=="medium":
   question=[
    {"Ques": "what is square root of 625", "Ans": "25"},
    {"Ques": "what is 15 * 12", "Ans": "180"},
    {"Ques": "what is value of 2^6", "Ans": "64"},
    {"Ques": "what is 121 / 11", "Ans": "11"},
    {"Ques": "what is 45 percent of 200", "Ans": "90"},

    {"Ques": "what is formula of area of circle", "Ans": "pi r square"},
    {"Ques": "what is value of pi upto 2 decimal", "Ans": "3.14"},
    {"Ques": "what is LCM of 12 and 18", "Ans": "36"},
    {"Ques": "what is HCF of 18 and 24", "Ans": "6"},
    {"Ques": "what is next number in series 2 4 8 16 ?", "Ans": "32"},

    {"Ques": "unit of power", "Ans": "watt"},
    {"Ques": "unit of voltage", "Ans": "volt"},
    {"Ques": "formula of force", "Ans": "mass acceleration"},
    {"Ques": "speed of light in vacuum (approx km/s)", "Ans": "300000"},
    {"Ques": "ohm law formula", "Ans": "v i r"},

    {"Ques": "chemical symbol of potassium", "Ans": "k"},
    {"Ques": "chemical formula of carbon dioxide", "Ans": "co2"},
    {"Ques": "atomic number of hydrogen", "Ans": "1"},
    {"Ques": "gas used in respiration", "Ans": "oxygen"},
    {"Ques": "acid in lemon", "Ans": "citric acid"},

    {"Ques": "who discovered gravity", "Ans": "newton"},
    {"Ques": "largest gland in human body", "Ans": "liver"},
    {"Ques": "human heart has how many chambers", "Ans": "4"},
    {"Ques": "which planet has rings", "Ans": "saturn"},
    {"Ques": "nearest star to earth", "Ans": "sun"},

    {"Ques": "full form of URL", "Ans": "uniform resource locator"},
    {"Ques": "full form of IP", "Ans": "internet protocol"},
    {"Ques": "which device stores data permanently", "Ans": "hard disk"},
    {"Ques": "which language is used for backend", "Ans": "python"},
    {"Ques": "which symbol is used for comments in python", "Ans": "#"},

    {"Ques": "output of 2 + 3 * 4", "Ans": "14"},
    {"Ques": "output of 10 % 4", "Ans": "2"},
    {"Ques": "output of 5 // 2", "Ans": "2"},
    {"Ques": "what is data type of 5.5", "Ans": "float"},
    {"Ques": "what is data type of true", "Ans": "boolean"},

    {"Ques": "who is father of java", "Ans": "james gosling"},
    {"Ques": "who is father of python", "Ans": "guido van rossum"},
    {"Ques": "national sport of india (officially none)", "Ans": "none"},
    {"Ques": "largest continent", "Ans": "asia"},
    {"Ques": "longest river in world", "Ans": "nile"},

    {"Ques": "value of sin 90 degree", "Ans": "1"},
    {"Ques": "value of cos 0 degree", "Ans": "1"},
    {"Ques": "value of tan 45 degree", "Ans": "1"},
    {"Ques": "what is 0 factorial", "Ans": "1"},
    {"Ques": "what is log10 100", "Ans": "2"},

    {"Ques": "what is derivative of x^2", "Ans": "2x"},
    {"Ques": "what is integration of 1 dx", "Ans": "x"},
    {"Ques": "what is binary of 10", "Ans": "1010"},
    {"Ques": "decimal of 101", "Ans": "5"},
    {"Ques": "what is 1 byte in bits", "Ans": "8"}
   ]
   p=0
   m=0
   try:
      print("How many questions would you like to attempt  (enter only integer vlue)?") 

      o=int(input()) 
      selectedquestions=random.sample(question,k=o)
      start=time.perf_counter()
      for i in selectedquestions :
        print(i["Ques"])
        userans=input("enter the answer ....")
        if i["Ans"].lower()== userans.lower():
          print(" ✔️Score is 1 point...")
          p=p+1
        else:
          print(" ❌  Wrong answer.....")
          print("                    Correct Answer is...",i["Ans"])
          m=m+1
        print()
      end=time.perf_counter()
      print("Enter your name")
      user=input()
      print()
      print("Final Score Card:")
      print(" Name           :",user)
      print(" Total correct  :",p)
      print(" Total wrong    :",m)
      print(" Percentage     :",(p*100)/o,"%")
      print(" Total  time    :",(end-start))
      print()
      print(" can you play game again...(enter only yes/no)" )
      h=input ()
      print() 
      if h.lower()=="yes":
        continue
      else :
           print(f"Game Over!  Thanks for playing {user}")
           break
   except Exception as e: 
      print(" Invalid input  enter only Integer:")
      print()
      print("Restart now ...")
      print()  
      continue    
     
 elif e=="hard":
   question=[
    {"Ques": "what is derivative of sin x", "Ans": "cos x"},
    {"Ques": "what is derivative of ln x", "Ans": "1/x"},
    {"Ques": "integration of x dx", "Ans": "x square by 2"},
    {"Ques": "value of limit x->0 (sin x)/x", "Ans": "1"},
    {"Ques": "what is determinant of identity matrix", "Ans": "1"},

    {"Ques": "what is eigenvalue of identity matrix", "Ans": "1"},
    {"Ques": "what is rank of identity matrix 3x3", "Ans": "3"},
    {"Ques": "what is formula of binomial theorem", "Ans": "ncr"},
    {"Ques": "what is 5 factorial", "Ans": "120"},
    {"Ques": "what is value of log e base e", "Ans": "1"},

    {"Ques": "newton second law formula", "Ans": "f m a"},
    {"Ques": "unit of electric field", "Ans": "newton per coulomb"},
    {"Ques": "formula of kinetic energy", "Ans": "half m v square"},
    {"Ques": "formula of potential energy", "Ans": "m g h"},
    {"Ques": "what is escape velocity depends on", "Ans": "mass radius"},

    {"Ques": "what is coulomb law formula", "Ans": "k q1 q2 r square"},
    {"Ques": "what is ohm law formula", "Ans": "v i r"},
    {"Ques": "what is power formula in electricity", "Ans": "v i"},
    {"Ques": "unit of capacitance", "Ans": "farad"},
    {"Ques": "unit of resistance", "Ans": "ohm"},

    {"Ques": "hybridization in methane", "Ans": "sp3"},
    {"Ques": "ph of strong acid approx", "Ans": "1"},
    {"Ques": "ph of strong base approx", "Ans": "14"},
    {"Ques": "avogadro number approx", "Ans": "6.022e23"},
    {"Ques": "molar mass of h2o", "Ans": "18"},

    {"Ques": "time complexity of binary search", "Ans": "log n"},
    {"Ques": "time complexity of linear search", "Ans": "n"},
    {"Ques": "time complexity of bubble sort worst", "Ans": "n square"},
    {"Ques": "stack follows which principle", "Ans": "lifo"},
    {"Ques": "queue follows which principle", "Ans": "fifo"},

    {"Ques": "what is output of 2**3**2", "Ans": "512"},
    {"Ques": "what is output of len([1,2,3,4])", "Ans": "4"},
    {"Ques": "what is data type of {1,2,3}", "Ans": "set"},
    {"Ques": "what is slicing [1,2,3,4][1:3]", "Ans": "2 3"},
    {"Ques": "what is keyword to handle exception", "Ans": "try"},

    {"Ques": "who developed relativity theory", "Ans": "einstein"},
    {"Ques": "planck constant symbol", "Ans": "h"},
    {"Ques": "speed of light in m/s", "Ans": "3e8"},
    {"Ques": "which particle has no charge", "Ans": "neutron"},
    {"Ques": "which particle is negative", "Ans": "electron"},

    {"Ques": "sql command to retrieve data", "Ans": "select"},
    {"Ques": "sql command to delete data", "Ans": "delete"},
    {"Ques": "primary key is unique or not", "Ans": "unique"},
    {"Ques": "foreign key used for", "Ans": "relation"},
    {"Ques": "normalization used for", "Ans": "reduce redundancy"},

    {"Ques": "what is 2 complement of 1", "Ans": "1"},
    {"Ques": "what is 1s complement of 0", "Ans": "1"},
    {"Ques": "what is ascii of A", "Ans": "65"},
    {"Ques": "what is boolean algebra 1+1", "Ans": "1"},
    {"Ques": "what is boolean algebra 1.0", "Ans": "0"}
   ]
   p=0
   m=0
   try:
      print("How many questions would you like to attempt  (enter only integer vlue)?") 

      o=int(input()) 
      selectedquestions=random.sample(question,k=o)
      start=time.perf_counter()
      for i in selectedquestions :
        print(i["Ques"])
        userans=input("enter the answer ....")
        if i["Ans"].lower()== userans.lower():
          print(" ✔️Score is 1 point...")
          p=p+1
        else:
          print(" ❌  Wrong answer.....")
          print("                    Correct Answer is...",i["Ans"])
          m=m+1
        print()
      end=time.perf_counter()
      print("Enter your name")
      user=input()
      print()
      print("Final Score Card:")
      print(" Name           :",user)
      print(" Total correct  :",p)
      print(" Total wrong    :",m)
      print(" Percentage     :",(p*100)/o,"%")
      print(" Total  time    :",(end-start))
      print()
      print(" can you play game again...(enter only yes/no)" )
      h=input ()
      print()   
      if h.lower()=="yes":
        continue
      else :
           print(f"Game Over!  Thanks for playing {user}")
           break
   except Exception as e: 
      print(" Invalid input  enter only Integer:")
      print()
      print("Restart now ...")
      print()  
      continue
 else :
         print("Enter valid input (Easy/Medium/Hard):")
         print() 
         continue

