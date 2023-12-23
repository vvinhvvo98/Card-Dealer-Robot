'''!@file                mainpage.py
    @brief               CARD DEALER ROBOT PROJECT
    @details             This porfolio page will be documenting everything related to personal project called CARD DEALER ROBOT
                         include coding work, electronics, and logic behind the robot
                         Please feel free to explore the files and email me at vinhvo.career@gmail.com if you have any question

    @mainpage
    

    @section sec_1      OBJECTIVE
                        The project's purpose is to design a robot that simplifies the card-dealing process for popular games such as Poker and Blackjack. 
                        The robot will be equipped with a straightforward display screen, allowing players to easily select the game, determine the number of participants, and set the card distribution per player. 
                        It will include a convenient memory feature to enable users to quickly replay the game without re-entering the same details, maintaining the card order for consistency in games where this is essential. 
                        Speed in dealing cards is a critical aspect, ensuring that game flow is not interrupted. In addition, the robot will be crafted with an aesthetically pleasing design, making it an attractive addition to any gaming table. 
                        This blend of functionality, speed, and design aims to deliver a seamless and engaging card game experience.

    @section sec_2      HARDWARE
                        The design concept for this project involves constructing a robot with a two-part subassembly. 
                        The first part is the bottom base, designed to remain immobile, providing stability and support. 
                        The second part is an upper segment that incorporates a spur gear. 
                        This gear will be connected to a stepper motor, which is responsible for the controlled rotational and pivotal movements of the robot, allowing it to adjust its orientation as needed.  
                        To visualize the idea before we proceed with the detailed engineering work, a hand-drawn sketch will be used. This sketch will serve as a preliminary visual guide, illustrating the basic structure and function of the two-part mechanism.

                        SKETCH GOES HERE
                         
                        For more information on the design, you can check out the detailed CAD model at @ref hardware.
                         
    @section sec_3      FIRMWARE
                        For this project, consider using an Arduino Nano as the microcontroller due to its compact size and efficiency in controlling input and output logic. 
                        Include two NEMA 17 stepper motors: one to control the rotation of the upper part for rotation, and the other for the precise dealing of cards from the deck. 
                        Implement a user-friendly interface featuring a small OLED screen for clear display of information like the number of players and cards per player, along with various settings. 
                        A 12x4 keyboard will allow for easy input of these details. The design should focus on a compact yet robust build to accommodate continuous card shuffling and dealing, ensuring a seamless and user-engaging experience.
                             
                        More details about how the electronic parts are connected and designed will be given in the @ref firmware section. 
                        This part of the document will clearly explain how all the components work together.
                        
    
    @section sec_5      FINAL DESIGN
                        The final CAD design of the ROMI robot includes an array of components: a digital line sensor module with five channels, an analog line sensor module, an ultrasonic distance sensor, two DC motors each equipped with built-in encoders, and two micro servos. 
                        The complete assembly of ROMI, representing the culmination of the term project, is depicted in the figure below. 
                        This design is current as of December 13, 2023. Please note that any further updates beyond this date will not be included in this portfolio due to time constraints.
                        
                        
      
    @section sec_6      TASK DIAGRAM
                        The robot will concurrently execute four tasks, as outlined in the Task Diagram below. 
                        This diagram specifies the duration (in ms) and relative priority of each task. 
                        These tasks will be scheduled according to their assigned priorities and periods using a scheduler script, the code for which has been provided by Lecturer Charlie Refvem.
                        
                        Note: All diagrams are listed and explain in detail at @ref diagram for futher more description
                        
    @section sec_7      PROJECT COMPLETE
                        
                        
    
    @section sec_yout   YOUTUBE REFERENCE
                        All videos including all the fail and successful run can be reference and accessible in the following URL links:
                            
                        All Videos:                     https://www.youtube.com/channel/UCh_4F4CJVqvAhHmCMTvIb-w
                        
                        

    @section sec_repo   REPOSITORY REFERENCE
                        All code that will be referenced in this portfolio relate to ROMI project
                        is accessible through []
                        
                        However, you may find it more useful to read through
                        the labs before looking around there. 
                       
   @author              Vinh Vo
   @author              Quinlan Stephens
   @date                Dec 12, 2023
'''