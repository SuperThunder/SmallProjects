pytrigcalc
==========

A basic and buggy python trigonometry calculator.


HISTORY--------------------------------------------------------------------------------------------------------------------

09/08/14: So much stuff I'll probably forget most of it. Finished trigfunctions class, redid the noofangles counting system, turned the results printing system into something acceptable, fixed noofangles and results system after they promptly broke again.

08/08/14: Scrapped the crappy rightsolve and nonrightsolve methods for a class under which all the solving functions are contained, which will be called from main or a central solving method/class that derives from the trigfunctions class.
Still to add to the trigfunctions class is functions/methods (w/e they're called for this implementation) that are for a case of two angles and one side known.

06/08/14: Renovations to the side input system, simplified some stuff. Started to work on the 8+ cases or w/e that are needed to actually solve every case of a triangle.
BIG IDEA: Rewrite so that we have a triangle class with the variables and solving functions, then a triangle object in which the variables values get entered with the object __init__. (credits to jondb)

05/08/14: Got it working somewhat for right angled triangles after going on a grand adventure with globals, locals, returns and lists.

06/14: Started programming this on a R-Pi while playing CS:GO. Neither my K/D nor my code were good. Before taking a long break fixed an UnboundLocalError and broke everything else.
