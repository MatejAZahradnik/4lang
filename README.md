# 4lang
Ezoteric programming language based on 4chan slang, translate "4lang" to C or C++.

compiler is python3 class, so you need a python3 program, that you run and it translate given file to c/c++ file

example of code

``` python3
comp = compiler(sourcef="test.4lang", debug=True) # Create a "comp" called compiler object
comp.readfile() # Read file you have given as argument in compiler object
comp.translate() # Translate the test.4lang sourcecode to C/C++
comp.writefile("test.c") # create file test.c and write source in c to it
```
