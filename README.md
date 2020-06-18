# 4lang
Esoteric programming language based on 4chan slang, translate "4lang" to C or C++.

compiler is python3 class, so you need a python3 program, that you run and it translate given file to c/c++ file

example of code

``` python3
import .compiler

comp = compiler(sourcef="test.4lang", debug=True) # Create a "comp" called compiler object
comp.readfile() # Read file you have given as argument in compiler object
comp.translate() # Translate the test.4lang sourcecode to C/C++
comp.writefile("test.c") # create file test.c and write source in c to it
```

only thing you need to do to run this code is adding compiler.py file to directory you want to compile in and add relative import.

This kind of translation has a lot of limitstions and translates without context, for example if you use "/b" in string (char array pointer) the result will be "main" instead of "/b", because it translates headlessly, just like google translator so have that limitations in mind, when writing code. This will be fixed in future by adding some advanced parser. 
