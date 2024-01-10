"""
imports unittest and uses a bash (shell)file to execute the script.

so pyton *file name of test*.py  can ad -v which makes test case have more details printed 

working inside of a class(unittest.testcase)
on bas "." represent passed tests
OK will display if passed

.assertequals checks if 2 elements are the same (thing, other thing)
.assertTrue/False checks if something is true or false

could check then with e.g.

(if it doesnt have test in the name it won't run, unless you use runTest which is an inbuilt func)
def test_triangle (self):
result=triangle_area.triangle(10,5)
self.assertEqual(result,25)
self.assertRaises(ValueError, *whatever you expect the error to be e.g. rectangle_perimeter.getperimeter, 10,0)

if you imported the triangle_area script then ran this test it would check it got the matching result

import your script to check
-does not matter what order funcs are written in they will be executed alphanumerically
-each test case should be independent 

-m unitest test_shape_area.py -v

-m unitest specifices that we are using unitest to run this 
-q test_shape_area.TestArea.test_square <-- runs the specific test out of that test file, the file, class then func. can use to run multiple tests
^ the -q is quiet mode it reduces the ammount of output to the console

@unitest.skip() decorattor tell script to skil this test rather than del or commentin gout 
can also use @unitest.skipIf(arg, message for skipping)
@unnitest.skipunless()
"""