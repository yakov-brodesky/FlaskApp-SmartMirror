zemanimDictHeb ={"alotHaShachar":"עלות השחר"
,"chatzot":"חצות היום"                     
,"chatzotNight":"חצות הלילה"               
,"dawn":"Dawn"                             
,"dusk":"Dusk"                             
,"minchaGedola":"מנחה גדולה"               
,"minchaKetana":"מנחה קטנה"                
,"misheyakir":"משיכיר"                     
,"misheyakirMachmir":"משיכיר (מחמיר) "     
,"plagHaMincha":"פלג המנחה"                
,"sofZmanShma":"סוף זמן שמע (גרא) "        
,"sofZmanShmaMGA":"Sof Zman Shma (MGA)"    
,"sofZmanTfilla":"סוף זמן תפילה (גר'א)"   
,"sofZmanTfillaMGA":"Sof Zman Tfilla (MGA)"
,"sunrise":"זריחה"                       
,"sunset":"שקיעה"                         
,"tzeit42min":"Tzeit42min"                 
,"tzeit50min":"Tzeit50min"                 
,"tzeit7083deg":"צאת הכוכבים"             
,"tzeit72min":"Tzeit72min"                 
,"tzeit85deg":"Tzeit85deg"}

zemaninDictEn ={"alotHaShachar":"Alot HaShachar"
,"chatzot":"Chatzot"				
,"chatzotNight":"Chatzot (Night)"
,"dawn":	"Dawn"					
,"dusk":	"Dusk"			
,"minchaGedola":"Mincha Gedola"			
,"minchaKetana":"Mincha Ketana"
,"misheyakir":"Misheyakir"			
,"misheyakirMachmir":"misheyakirMachmir"
,"plagHaMincha":"Plag HaMincha"			
,"sofZmanShma":"Sof Zman Shma (Gra)"			
,"sofZmanShmaMGA":"Sof Zman Shma (MGA)"		
,"sofZmanTfilla":"Sof Zman Tfilla (Gra)"		
,"sofZmanTfillaMGA":"Sof Zman Tfilla (MGA)"		
,"sunrise":"Sunrise"
,"sunset":"Sunset"				
,"tzeit42min":"Tzeit42min"			
,"tzeit50min":"Tzeit50min"			
,"tzeit7083deg":"Tzeit Ha'Kochavim"
,"tzeit72min":"Tzeit72min"			
,"tzeit85deg":"Tzeit85deg"}

zmnToShow =["alotHaShachar","chatzot","minchaGedola","sofZmanShma","sofZmanTfilla","sunrise","sunset","tzeit7083deg"]


#y_squares = {1:1,2:4,3:9,4:16,5:25}
#my_cubes = {key: value*key for (key, value) in my_squares.items()}
res =[(zmn , zmnVal) for (zmn,zmnVal) in zemaninDictEn.items() if zmn in zmnToShow]
res2 =[{zmn,zmnVal} for (zmn,zmnVal) in zemaninDictEn.items() if zmn in zmnToShow]
res3 =[{zmn:zmnVal} for (zmn,zmnVal) in zemaninDictEn.items() if zmn in zmnToShow]
