# C2Rust

A conversion tool to translate C code into Rust.

## USAGE

> $ python3 ./c2rust.sh [CFileIn] [fileOutName]

## NOTICE

Since development is not completed, please check the tests/testFile.c to see the extent of what the program can process

---

## DEVELOPMENT PROGRESS

**Currently Supports:**

* Functions
* Function Parameters
* Calling of functions
* Conversion to Snake Casing
* Variables (constants and mutable)
* Basic C functions
  1. printf()
  2. gets()
* While loops
* For loops
* Pointers (primitive use cases)

**TODO:**

* BUG: when declaring variables for the first time, they must have a value
* BUG: global comments do not carry over
* BUG: some C constants are being incorrectly labeled as mutable
* NOT GOOD: Code quality
* NOT GOOD: Using the rust string type `std::string::String` is proving difficult to work with
* ADD: support for more basic C functions
* ADD: ability to import C libraries where there is no direct alternative
* ADD: ability to convert entire directories/projects at once
* ADD: support for #define
