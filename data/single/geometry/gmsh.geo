///////////////////////////////////////////////////////////////////
// Gmsh geometry file for the domain used in Barlag 1998
// The 3d domain consists of two layers and a 2d fault zone
// embedded in the upper one. Meshing is done using Hexahedra.
///////////////////////////////////////////////////////////////////

numPointsX = 11;              // no. vertices in x direction
numPointsY = 11;              // no. vertices in y direction
numPointsZ_layer1 = 5;        // no. vertices in z in layer one
numPointsZ_layer2_below = 5;  // no. vertices in z in layer two below the fault
numPointsZ_layer2_above = 5;  // no. vertices in z in layer two above the fault

// domain bounding box
Point(1) = {0.0, 0.0, 0.0, 1.0};
Point(2) = {100.0, 0.0, 0.0, 1.0};
Point(3) = {100.0, 100.0, 0.0, 1.0};
Point(4) = {0.0, 100.0, 0.0, 1.0};
Point(5) = {0.0, 0.0, 100.0, 1.0};
Point(6) = {100.0, 0.0, 100.0, 1.0};
Point(7) = {100.0, 100.0, 100.0, 1.0};
Point(8) = {0.0, 100.0, 100.0, 1.0};

// Lower layer boundary points
Point(9) = {0.0, 0.0, 10.0, 1.0};
Point(10) = {100.0, 0.0, 10.0, 1.0};
Point(11) = {100.0, 100.0, 10.0, 1.0};
Point(12) = {0.0, 100.0, 10.0, 1.0};

// fault zone boundary points
Point(13) = {0.0, 0.0, 80.0, 1.0};
Point(14) = {100.0, 0.0, 20.0, 1.0};
Point(15) = {100.0, 100.0, 20.0, 1.0};
Point(16) = {0.0, 100.0, 80.0, 1.0};

// injection zone additional points
Point(17) = {0.0, 0.0, 90.0, 1.0};
Point(18) = {100.0, 0.0, 60.0, 1.0};
Point(19) = {100.0, 100.0, 60.0, 1.0};
Point(20) = {0.0, 100.0, 90.0, 1.0};

// layer one vertical discretization
Line(1) = {1, 9};
Line(2) = {4, 12};
Line(3) = {2, 10};
Line(4) = {3, 11};
Transfinite Line{1:4} = numPointsZ_layer1;

// layer two vertical discretization below the fault
Line(5) = {10, 14};
Line(6) = {11, 15};
Line(7) = {12, 16};
Line(8) = {9, 13};
Transfinite Line{5:8} = numPointsZ_layer2_below;

// layer two vertical discretization above the fault
Line(9) = {5, 17};
Line(10) = {17, 13};
Line(11) = {8, 20};
Line(12) = {20, 16};
Line(13) = {6, 18};
Line(14) = {18, 14};
Line(15) = {7, 19};
Line(16) = {19, 15};
Transfinite Line{9:16} = numPointsZ_layer2_above/2;

// discretization in x-direction
Line(17) = {1, 2};
Line(18) = {9, 10};
Line(19) = {13, 14};
Line(20) = {5, 6};
Line(21) = {4, 3};
Line(22) = {12, 11};
Line(23) = {16, 15};
Line(24) = {8, 7};
Line(33) = {17, 18};
Line(34) = {20, 19};
Transfinite Line{17:24} = numPointsX;
Transfinite Line{33, 34} = numPointsX;

// discretization in y-direction
Line(25) = {2, 3};
Line(26) = {10, 11};
Line(27) = {14, 15};
Line(28) = {6, 7};
Line(29) = {1, 4};
Line(30) = {9, 12};
Line(31) = {13, 16};
Line(32) = {5, 8};
Line(35) = {17, 20};
Line(36) = {18, 19};
Transfinite Line{25:32} = numPointsY;
Transfinite Line{35, 36} = numPointsY;

// fracture plane
Line Loop(1) = {19, 27, -23, -31};
Plane Surface(1) = {1};

// lower matrix volume
Line Loop(2) = {1, 18, -3, -17};
Plane Surface(2) = {2};
Line Loop(3) = {3, 26, -4, -25};
Plane Surface(3) = {3};
Line Loop(4) = {4, -22, -2, 21};
Plane Surface(4) = {4};
Line Loop(5) = {2, -30, -1, 29};
Plane Surface(5) = {5};
Line Loop(6) = {29, 21, -25, -17};
Plane Surface(6) = {6};
Line Loop(7) = {26, -22, -30, 18};
Plane Surface(7) = {7};
Surface Loop(1) = {7, 3, 2, 5, 4, 6};
Volume(1) = {1};

// upper matrix volume below fault
Line Loop(8) = {18, 5, -19, -8};
Plane Surface(8) = {8};
Line Loop(9) = {5, 27, -6, -26};
Plane Surface(9) = {9};
Line Loop(10) = {6, -23, -7, 22};
Plane Surface(10) = {10};
Line Loop(11) = {7, -31, -8, 30};
Plane Surface(11) = {11};
Surface Loop(2) = {1, 8, 9, 10, 11, 7};
Volume(2) = {2};

// upper matrix volume above fault to injection zone
Line Loop(12) = {10, 19, -14, -33};
Plane Surface(12) = {12};
Line Loop(13) = {14, 27, -16, -36};
Plane Surface(13) = {13};
Line Loop(14) = {16, -23, -12, 34};
Plane Surface(14) = {14};
Line Loop(15) = {12, -31, -10, 35};
Plane Surface(15) = {15};
Line Loop(16) = {33, 36, -34, -35};
Plane Surface(16) = {16};
Surface Loop(3) = {16, 12, 15, 14, 13, 1};
Volume(3) = {3};

// upper matrix volume above injection zone
Line Loop(17) = {9, 33, -13, -20};
Plane Surface(17) = {17};
Line Loop(18) = {13, 36, -15, -28};
Plane Surface(18) = {18};
Line Loop(19) = {15, -34, -11, 24};
Plane Surface(19) = {19};
Line Loop(20) = {11, -35, -9, 32};
Plane Surface(20) = {20};
Line Loop(21) = {32, 24, -28, -20};
Plane Surface(21) = {21};
Surface Loop(4) = {21, 20, 19, 18, 17, 16};
Volume(4) = {4};

// use hexaheders for meshing
Transfinite Surface "*";
Recombine Surface "*";
Transfinite Volume "*";

// give physical entity indices to layers
Physical Volume(1) = {1};     // lower layer
Physical Volume(2) = {2,3,4}; // upper layer
Physical Surface(3) = {1};    // fault zone
