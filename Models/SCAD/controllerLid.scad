include <arduino.scad>
rotate([180,0,0]){
	difference(){
		enclosureLid(boardType = UNO, wall = 5, offset = 2);
		translate([19,80,-4]){
			rotate([90,0,0]){
				cube(16,30,11);
			}
		}
	}
}
