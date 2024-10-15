+++
title = "A deep dive into programming"
date = 2024-07-23
draft = true
+++

Computers are enlightened calculators, nothing more. So how did we manage to use them to power websites, crunch mind-gobbling amounts of scientific data, and even do machine learning? That's what we'll explore here.

<!-- more -->

Let me start with a fact that I find _sublimely_ fascinating: all programming languages are ultimately number-based. But that's absurd, you say! Actually, they _are_. Consider the C language. All of its instructions are numbers, or pointers, which are themselves numbers. C strings are numbers - when we use `const *mystr = "hello"` we are using pointers. All arrays in C are _also_ numbers. The same goes for C-style languages, such as C++, or even more modern systems programming languages like Rust or Zig. The more abstract data structures and object-oriented features are just syntactical sugar and are turned into more basic operations at compile time.

What about interpreted languages like JavaScript, Lua, and Python, you ask? Well, they are actually software programs written in compiled languages! So at their root, they also use purely numbers, just with many layers of abstraction on top.

The fact that really all computers are doing are a bunch of calculations with a bunch of numbers illustrates that that they are fundamentally calculators. This allows them to map cleanly to _bits_, which are the base unit of numbers in a binary number system.