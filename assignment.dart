//This is my Assigment 

void main(){
//using int
int num1 = 100; 
print("Num 1 is $num1");

//using double
double num2 = 130.2; // with decimal point.
print("Num 2 is $num2"); 

//using string
String firstname = "Adewale";
String lastname = "Adetokunbo";
print("Welcome $firstname $lastname");

//using list
List<String> students = ["Sade", "Bayo", "Bunmi"];
print("Value of names is $students");
print("Value of names[0] is ${students[0]}"); // index 0
print("Value of names[1] is ${students[1]}"); // index 1
print("Value of names[2] is ${students[2]}"); // index 2

//Map
Map<String, double> kilogram = {'Fish': 3.5,
'Turkey': 2.5,
'Chicken': 3.5,
};
print("Ages of students: $kilogram");

}
