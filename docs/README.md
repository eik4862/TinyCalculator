# Tiny calculator

> Tiny calculator for undergraduate-level numerical analysis & statistics.

With easy grammar similar that of MATHEMATICA, enjoy basic numerical computations.
__
## Where its name comes from?
The name __tiny calculator__ comes from The famous computer architecture textbook _Computer Systems: a programmer's perspective_ written by Randal E. Bryant.
In the textbook, there is a sample code for server using multithreading and as you might have noticed, the name of this server is __tiny server__!
Thus its name, __tiny calculator__.

## Why we made tiny calculator?
Tiny calculator is started from a homework of Introduction of Numerical Analysis class in SNU. (Thus our project has its name, __NA__!)
As a homework, we wrote many numerical codes with C++ and somehow felt that it will be great if we collect all those into one stand-alone program.
Since developing such large program with C++ in limited time is hard, we decided to write it with Python.
Maybe, at some day, we can port our tiny calculator into C++ for better performance.
(Actually, we already wrote some code base for core functionality including C++ specific modules like memory manager, but there are also _huge_ amounts of bugs to fix :))

## Who needs this documentation?
This documentation is for developers who want to further improve our tiny calculator or embed its functionality to other apps.
Thus it is not for end users who are just happy with original tiny calculator.
We suppose that the reader of this document has basic knowledge on programming, mathematics, and statistics.
__With this document, feel free to improve and modify our tiny calculator!__

## How to make documentation like this?
As you know, making documentation of program or code is _very_ tedious job.
But we discovered a precious tool which essentially remove this.
[Docsify](https://docsify.js.org/#/) ([github](https://github.com/docsifyjs/docsify/)) is a magical documentation site generator with various plug-ins.
Using markdown-like grammar, it generates full-blown awesome web page based on [Vue.js framework](https://vuejs.org).
One can get docsify by simply typing the following command in one's shell.
```bash
  npm install docsify-cli -g
```
Also, for better appearance, we used [Bootstrap](https://getbootstrap.com) CSS library.
One can get bootstrap by typing the following command in the shell.
```bash
    npm install bootstrap
```
For those who want to link it dynamically, use Bootstrap CDN by adding following two lines in your html.
```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
```