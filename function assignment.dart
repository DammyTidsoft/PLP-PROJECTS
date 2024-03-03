//this is addition function 
void add(int num1, int num2){
  int sum = num1 + num2;
   print("The sum is $sum");
}

//This is subtraction function
void subtract(int num1, int num2){
  int sub = num1 - num2;
   print("The sub is $sub");
}

//This is multiply function 
void multiply(int num1, int num2){
  int mul = num1 * num2;
   print("The multiply is $mul");
}

//This is division function 
void division(num num1, num num2){
  num div = num1 / num2;
   print("The Division is $div");
}

void stringLenght(String name){
  int count = name.length;
   print("The StringLenght is $count");
}


void main(){
  add(10, 20);
  subtract(40, 20);
  multiply(10, 20);
  division(100, 20);
  stringLenght("Welcome");
 }