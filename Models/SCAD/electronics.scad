bLength = 180;
bWidth = 180;
binHeight = 120;
margin = 15;
lip = 5;
lipDepth = 10;
difference(){
  cube([bLength+margin*2, bWidth+margin*2, binHeight]);
  translate([margin, margin, margin])
    cube([bLength, bWidth, binHeight]);
  translate([margin-lip, margin-lip, binHeight-lip])
    cube([bLength+lip*2, bWidth+lip*2, binHeight]);
}
