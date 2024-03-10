import 'dart:io';

// Interface definition
abstract class Animal {
  void makeSound();
}

// Base class
class Mammal implements Animal {
  @override
  void makeSound() {
    print('Mammal makes a sound');
  }
}

// Inherited class
class Cat extends Mammal {
  @override
  void makeSound() {
    print('Cat meows');
  }
}

// Class that initializes data from a file
class Person {
  String name;

  Person(this.name);

  void sayHello() {
    print('Hello, my name is $name');
  }
}

void main() {
  // Object of inherited class
  var cat = Cat();
  cat.makeSound();

  // Object of class implementing an interface
  var person = Person('John Doe');
  person.sayHello();

  // Read data from a file and initialize object
  var file = File('data.txt');
  var data = file.readAsStringSync();
  var personFromFile = Person(data);
  personFromFile.sayHello();

  // Method demonstrating the use of a loop
  for (var i = 1; i <= 5; i++) {
    print('Iteration $i');
  }
}