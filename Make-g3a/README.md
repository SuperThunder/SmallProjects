# mkg3a
Command line interface for the mkg3a utility to compile code for Casio Prizm calculators

Stage 1 (compiling code) only works on Linux. Stage 2 (building code into g3a) only works on windows with mkg3a utility built by
cemetech (I think) community. So what you do is compile your project on Linux with the makefile in the project folder, 
sync the changes in a repository (or send them over manually) to a windows computer that then runs mkg3a.exe through mkg3acom.exe
and then you can put that on your shiny Casio Prizm.

Basically,

1. write code

2. compile on linux

3. build to g3a on windows

4. put on calculator

Future ideas: work in some python or something that's not plain old C to automatically link the Windows machine
to the linux one so you can just push a button on the Linux machine and the build process on both happens automatically.
Or maybe run a Windows VM on the Linux machine, or get Wine to play nicely with mkg3a.exe.
Or possibly even get mkg3a working for Linux.
