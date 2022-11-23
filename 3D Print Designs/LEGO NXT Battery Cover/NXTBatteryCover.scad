thickness = 1.5;
width = 61;
length = 88;
tabWidth = 3;
tabLength = 19.5;
tabZOffset = 1.5;
tabAttachWidth = 2;
clipWidth = 5;
clipLength = 29;
clipHeight = 14;
clipAttachWidth = 1;
holeWidth = 14;
holeLength = 70;

$fn=20;

difference(){
	translate([-width/2, -length/2]) cube([width, length, thickness]);
	translate([width/3-holeWidth,-holeLength/2,-1]) cube([holeWidth,holeLength,thickness+2]);
	translate([-width/3,-holeLength/2,-1]) cube([holeWidth,holeLength,thickness+2]);
}
translate([width/2-tabAttachWidth, -tabLength/2, tabZOffset]) cube([tabAttachWidth+tabWidth, tabLength, thickness]);

translate([width/2+tabWidth-1, -tabLength/2]) cube([1.2, tabLength, thickness]);

translate([-width/2-clipWidth+clipAttachWidth, -clipLength/2]) cube([clipWidth, clipLength, clipHeight-clipWidth/2]);
		translate([-width/2-clipWidth/2+clipAttachWidth, clipLength/2, clipHeight-clipWidth/2]) rotate([90,0]	) cylinder(clipLength, clipWidth/2, clipWidth/2);