include <arduino.scad>

difference(){
	enclosure(boardType = UNO, wall =  5, offset =  2, heightExtension = 10);
		translate([19,80,23]){
			rotate([90,0,0]){
				cube([16,30, 20]);
			}
		}
}