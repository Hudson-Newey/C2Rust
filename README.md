# C2Rust
A conversion tool to translate C code into Rust.

##### USAGE
> $ python3 ./main.py <CFileIn> (fileOutName)

#### NOTICE
_Since development is not completed, please check the testFile.c to see the extent of what the program can process_

---

### DEVELOPMENT PROGRESS
Currently Supports:
* Functions
* _Function Parameters_
* Calling of functions
* Conversion to Snake Casing
* Variables (constants and mutable)
* Basic C functions
	1. printf()
	2. gets()

TODO:
* BUG: when declaring variables for the first time, they must have a value
* BUG: at the current time, functions can only have one parameter
* ADD: support for more basic C functions
* ADD: ability to import C libraries where there is no direct alternative
* ADD: ability to convert entire directories/projects at once