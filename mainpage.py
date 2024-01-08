'''!@file                mainpage.py
    @brief               CARD DEALER ROBOT PROJECT
    @details             This porfolio page will be documenting everything related to personal project called CARD DEALER ROBOT
                         include coding work, electronics, and logic behind the robot
                         Please feel free to explore the files and email me at vinhvo.career@gmail.com if you have any question

    @mainpage
    

    @section secs_1     OBJECTIVE
                        The project's purpose is to design a robot that simplifies the card-dealing process for popular games such as Poker and Blackjack. 
                        The robot will be equipped with a straightforward display screen, allowing players to easily select the game, determine the number of participants, and set the card distribution per player. 
                        It will include a convenient memory feature to enable users to quickly replay the game without re-entering the same details, maintaining the card order for consistency in games where this is essential. 
                        Speed in dealing cards is a critical aspect, ensuring that game flow is not interrupted. In addition, the robot will be crafted with an aesthetically pleasing design, making it an attractive addition to any gaming table. 
                        This blend of functionality, speed, and design aims to deliver a seamless and engaging card game experience.

    @section secs_2     HARDWARE
                        The design concept for this project involves constructing a robot with a four-part subassembly. 
                        
                        Part 1 is the bottom base, designed to remain immobile, providing stability and support.
                        
                        Part 2 is an middle pard that incorporates a spur gear that will rotate with respect to the base
                        
                        Part 3 is in a seperate part that use to hold the card deck and shooting card out for card distribution that is attached by 4 strong magnets.
                        
                        Part 4 is the top piece that is included everything for User Interface such as indicator LED, OLED screen and 4x4 keyboard.

                        SKETCH GOES HERE
                         
                        For more information on the design, you can check out the detailed CAD model at @ref hardware.
                         
    @section secs_3     FIRMWARE
                        For this project, consider using an Arduino Nano as the microcontroller due to its compact size and efficiency in controlling input and output logic. 
                        Include two NEMA 17 stepper motors: one to control the rotation, and the other for the precise dealing of cards from the deck. 
                        Implement a user-friendly interface featuring a small OLED screen for clear display of information like the number of players and cards per player, along with various settings. 
                        A 12x4 keyboard will allow for easy input of these details. The design should focus on a compact yet robust build to accommodate continuous card dealing.
                             
                        More details about how the electronic parts are connected and designed will be given in the @ref firmware section. 
                        This part of the document will clearly explain how all the components work together.
                        
    
    @section secs_5     FINAL DESIGN
                        Figure below shows the final design of the robot
                        This design is current as of September 12, 2022. Please note that any further updates beyond this date will not be included.
                        
                        @image html finaldesign.png
      
    @section secs_6     FLOW DIAGRAM
                        The project's diagram, started early in the junior year, uses block coding instead of a typical Finite State Machine. 
                        A flow diagram is included to clearly show how the robot works. 
                        The diagram of this project does not follow the Finite State Machine but contains a lot of block coding since the project is start early of school years.
                        However, the flow diagram below will briefly describe the running flow of the robot.
                        
                        @image html flowchart.png
                        
    @section sec_yout   YOUTUBE REFERENCE
                        All videos including all the fail and successful run can be reference and accessible in the following URL links:
                            
                        All Videos:                    
                        
                        

    @section sec_repo   REPOSITORY REFERENCE
                        All code that will be referenced in this portfolio relate to ROMI project
                        is accessible through https://github.com/vvinhvvo98/Card-Dealer-Robot
                        
                        However, you may find it more useful to read through
                        the whole pages before looking around there. 
                       
   @author              Vinh Vo
   @date                Sep 12, 2022
'''