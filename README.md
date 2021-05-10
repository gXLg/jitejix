![logo](https://user-images.githubusercontent.com/65429873/117552007-36988b00-b049-11eb-963b-df0d485c1838.png)

# jitejix
An esolang created for fun.

Pronounciated as `[d zh i t e d zh i k s]`.

Inspired by Brainfuck.

Probably not turing complete, who knows.

The name was chosen while randomly typing letters.

Extensions: `.jj`, `.j`, none.

# Concept
Only 256 cells, wrap around.

Cell values 0-255, wrap around.


At beginning: all cells with the value of their index:

[0,1,2,3,4,5,...254,255].


There is stack = 0, acts like a cell.


Can access stdout, not stdin.


# Instructions

`+` - increase, but increases twe two neighbour cells

`-` - the same with decrease

`&` - swap two neighbour cells

`/` - add value of current cell to stack

`\` - copy value from stack to cell

`*` - multiplies values of neighbour cells
    and adds to current cell

`%` - restore original value of current cell

`_` - set cell to zero

`?` - proof boolean of current cell and skip to next `:` if false

`#` - proof boolean of stack

`!` - print char

`>` - move one cell right

`<` - same to left

`^` - move so much to the right, as much the value is in stack

`@` - move to cell with index of current value

`~` - decrease stack

`$` - jump to last `?` or `#`

All other chars are ignored completely.

# Hello World

"Hello World!\n" - example written in jitejix that shows its functionality:
```
>>>_*@*@>!
////^<<<!
>>>>>>>!!
>>>!
_\!
_+<%>++*@>>>>>>>!
^_\*@<%!
->!
<<<<!
<<<<<<<<!
_\@>!
_@>>>@>>!
```
Sure can be written shorter.

# Interpreter
Currently an interpreter available for my language, written in python and javascript.

To use it, do:
```
 $ python3 jitejix.py <filename>
```
or
```
 $ node jitejix.js <filename>
```
