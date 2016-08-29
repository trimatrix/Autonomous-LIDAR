bHeight = 2;
bWidth = 72;
bLength = 50;
padding = 5;
lip =3;
difference(){
  cube([76, 65, 52]);
  translate([5, -1, 5]){
    cube([66,61,42]);
  }
  translate([2,-1,25]){
    cube([bWidth, 61, bHeight]);
  }
}
