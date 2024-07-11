# Summary
This plugin calculates the “Yarding Distance,” which represents the average distance from a polygon to a point.<br>
Input : Polygon (layer), Point (click on the map) and Dot spacing<br>
Steps : Create dots over the polygon. Measure the lengths from the dots to the point. Calculate the average of these lengths.<br>
Output : Calculated layers (yard point, wood dots, transport lines, and labeled polygon)<br>
The distance calculation is based on the project coordinate system, and both the Euclidean distance and the Manhattan distance are provided in the output.<br>
