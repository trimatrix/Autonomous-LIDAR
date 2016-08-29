module enclosure(width, length, height, wall, recess, lip, cap, hole){
     mainW = width + 2*wall;
     mainL = length + 2*wall;
     mainH = height +wall+recess+cap;
     difference(){
	  cube([mainW, mainL, mainH]);
	  translate([wall,wall, -1]){
	       cube([width,length, height+1+cap]);
	  }
	  translate([wall, wall+lip,height+cap-1]){
	       cube([width, length-2*(lip), recess]);
	  }
	  translate([-1,(mainL/2)-(hole/2),-1]){
	       cube([2+mainW,hole, hole+1]);
	  }
     }
}
module enclosureLid(width, length, wall, cap){
     cube([width+2*wall, length + 2*wall, wall]);
     translate([wall,wall,wall]){
	  cube([width, length, cap]);
     }
}
translate([0,82,44]){
     rotate([180,0,0]){
	  enclosure(width = 52,length = 72, height = 4, wall = 5, recess = 30, lip = 5, cap = 5, hole = 20);
     }
}
translate([70,0,0]){
     enclosureLid(width = 52, length = 72, wall = 5, cap = 5);
}
