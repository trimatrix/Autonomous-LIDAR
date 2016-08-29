rotate([90,0,0]){
     difference(){
	  union(){
	       cube([76, 5,52]);
	       translate([5,4,5]){
		    cube([65,4,41]);  
	       }
	  }
	  translate([33,-1,-1]){
	       cube([10,11,16]);  
	  }
     }
}
