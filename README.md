# Motion_Graph2D
automatically make a 2d motion graph from a tennis ball.

In reality, you don't have to use a tennis ball, and instead to modify it, change the 2 numpy arrays that represent color to use a different object.
If the other object has a different size, you also need to get the estimated pixel length and change the LowerP var and the HigherP var in order to make the program more accurate and recognize the ball better. The accuracy of the graph is much better when the tennis ball or other object is the only object detected, otherwise the graph will be completely wrong.
