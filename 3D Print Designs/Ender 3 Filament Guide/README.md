# Ender 3 Filament Guide for Sainsmart's 3DP Design

One issue with the Ender 3 is the lack of a filament guide. The biggest problem is that filament has a 90 degree bend into the extruder motor assembly. This can cause the filament to under-extrude or even break. 

The filament spool is mounted on the top of the printer and the filament could get caught on the frame or other parts of the printer, causing jams or tangles. A filament guide helps to direct the filament smoothly from the spool to the extruder, reducing the risk of jams and improving print quality.

I remixed [this filament guide](https://www.thingiverse.com/thing:3052488) to fix some minor problems with my particular implementation of the Ender 3 design. I was printing with MakeShaper PLA and these modifications worked well for me. I also added the feeder from [this design](https://www.thingiverse.com/thing:4849559) to keep filament away from other moving parts and prevent tangling.

1. I knocked out the bottom edge in the section of the bracket. The metal piece I need to install this on has no bottom clearance so it wouldn't fit. I also adjusted the bracket hole size for the M4 so that it would thread a little easier during installation. It now securely cuts threads on both sides of the bracket arm as you insert the bolt.

2. The spacers were surprisingly challenging to tune. The bolt would not get past the spacer in the original design since it wouldn't thread. It was also too loose inside the 608 bearing. Since it's inside the bearing, they spin freely when you try to thread the bolt through them. To fix this, I,
    - enlarged the hole so that the bolt feeds cleanly through the spacers
    - sized the spacer up slightly for a simple press-fit inside the bearing
    - added a slight chamfer around the hole on the bottom side so that the bottom layer doesn't splay out and require clean up of that edge of the hole after printing.

The only piece that needs support is the guide.

Included are a couple of photos to show the assembly and installation.

You'll need a 608 bearing (common skateboard bearing) and an M4-16 bolt. Longer would work but isn't necessary. Print the spacer twice.
