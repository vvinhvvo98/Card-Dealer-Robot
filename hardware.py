'''! @page hardware 3D CAD Modeling
    @section seca_1     Overview
                        This robot has a strong design with two linear ball bearings and a 3/4 inches shaft to support its structure. 
                        On top of this base, it has electronic parts and spacers for organization. 
                        Its card distribution system uses a spring to press cards against a spinning wheel, driven by a NEMA 17 motor. 
                        The part that distributes cards can be easily removed and attached with four magnets for quick card loading

    @section seca_2     Part 1: Base
                        3D Model: Assembly
                        This assembly is immovably static, serving as a stable reference frame anchored to the ground.
                        @image html base.png
                        
                        As shown in the exploded view, the fixed ball bearing is attached to the internal spur gear  by 2 set of bolts and nuts
                        3D Model: Exploded View
                        @image html basee.png
                        
                        3D Model: Internal Spur Gear
                        The internal gear, 3D printed and featuring 200 teeth, achieves a gear ratio of 1:4 when paired with the driven spur gear, which has 50 teeth.
                        @image html ispur.png
                        
                        3D Model: Fixed Ball Bearing 
                        This fixed allignment ball bearing and its housing is purchased from McMaster-Carr for a 3/4 inches diameter shaft
                        @image html bearing.png
                        
    @section seca_3     Part 2: Bottom
                        3D Model: Assembly
                        This assembly forms the base component of the rotating section and will facilitate the rotation of the robot by incorporating a NEMA 17 stepper motor and a driven gear.
                        @image html bottom.png 
                        
                        3D Model: Exploded View
                        As shown in the exploded view, the fixed ball bearing is attached to the bottom assembly by 2 set of bolts and nuts.
                        Then the whole assembly is supported with a 3/4 inches diameter shaft.
                        The spur gear is attached directly into the stepper motor to rotate the robot.
                        Two magnets is added to provide a convinient detachable feature for subassembly in @ref seca_br3
                        @image html bottome.png 
                        
                        3D Model: Platform + Stepper Housing
                        The housing platform has location for mounting the NEMA 17 stepper motor, fixed ball bearing, magnets, etc
                        @image html platformmid.png
                        
                        3D Model: Fix Ball Bearing
                        This fixed allignment ball bearing and its housing is purchased from McMaster-Carr for a 3/4 inches diameter shaft
                        @image html bearing.png
                        
                        3D Model: 3D printed Spur Gear
                        The spur gear is also 3D printed and has 50 teeth to archive a 1:4 gear ratio
                        @image html spur.png
                        
                        3D Model: Magnets
                        These two magnets are purchased from McMaster-Carr 
                        @image html magnets.png
                        
                        
    @section seca_br3   Part 3: Middle
                        3D Model: Assembly
                        @image html cardshoot.png
                        
                        3D Model: Exploded View
                        @image html shoote.png 
                        
                        3D Model: Housing
                        @image html housingshoot.png 
                        
    @section seca_br4   Part 4: Top
                        3D Model: Assembly
                        @image html top.png
                        
                        3D Model: Exploded View
                        @image html tope.png
                        
                        3D Model: Lower Plate
                        @image html lower.png
                        
                        3D Model: Upper Plate
                        @image html upper.png
                        
    @section seca_br6   Final Design
                        3D Model: Final Assembly
                        @image html finaldesign.png
                        
                        3D Model: Exploded View
                        @image html final.png
                        
    @section seca_br7   CAD REFERENCE
                        All CAD modeling from SolidWorks can be access in the "CAD" folder through https://github.com/vvinhvvo98/Card-Dealer-Robot
                        
                         
                        
   @author              Vinh Vo
   @date                Sep 12, 2022
'''