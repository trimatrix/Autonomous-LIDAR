rotate([180, 0, 0]) {

difference(){
  cube([32,70,32]);
  translate([5, 5, -1]) {
    cube(size=[22, 60, 23], center=false);
  }
  translate([11, -10, -1]) {
    cube([10,100,11]);
  }
}
}
