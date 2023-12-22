'''!@file                mainpage.py
    @brief               CARD DEALER ROBOT PROJECT
    @details             This porfolio page will be documenting everything related to personal project called CARD DEALER ROBOT
                         include coding work, electronics, and logic behind the robot
                         Please feel free to explore the files and email me at vinhvo.career@gmail.com if you have any question

    @mainpage
    

    @section sec_1       OBJECTIVE
                         The project's purpose is to design a robot that simplifies the card-dealing process for popular games such as Poker and Blackjack. 
                         The robot will be equipped with a straightforward display screen, allowing players to easily select the game, determine the number of participants, and set the card distribution per player. 
                         It will include a convenient memory feature to enable users to quickly replay the game without re-entering the same details, maintaining the card order for consistency in games where this is essential. 
                         Speed in dealing cards is a critical aspect, ensuring that game flow is not interrupted. In addition, the robot will be crafted with an aesthetically pleasing design, making it an attractive addition to any gaming table. 
                         This blend of functionality, speed, and design aims to deliver a seamless and engaging card game experience.

    @section sec_2       HARDWARE
                         The design concept for this project involves constructing a robot with a two-part subassembly. 
                         The first part is the base, designed to remain immobile, providing stability and support. 
                         The second part is an upper segment that incorporates a spur gear. 
                         This gear will be connected to a stepper motor, which is responsible for the controlled rotational and pivotal movements of the robot, allowing it to adjust its orientation as needed.
                         
                         To visualize the idea before we proceed with the detailed engineering work, a hand-drawn sketch will be used. This sketch will serve as a preliminary visual guide, illustrating the basic structure and function of the two-part mechanism.

                         SKETCH GOES HERE
                         
                         For more information on the design, you can check out the detailed CAD model at @ref hardware.
                         
    @section sec_3       FIRMWARE
                         For the educational objectives of the Mechatronics ME 405 course, the selected microcontroller is the Nucleo STM32, which is complemented by an extension board known as the "Shoe of Brian." 
                         This extension board, provided by Lecturer Charlie Refvem, enables the use of the MicroPython programming language with the Nucleo STM32, offering an alternative to the conventional C language. 
                         The Nucleo STM32 is readily available for purchase on platforms like Amazon at an affordable price, making it accessible for students. 
                         However, the "Shoe of Brian" extension board is specially designed and developed exclusively for the ME 405 course by of Dr. Ridgely.
                         Figure below is the Nucleo STM32 microcontroller, integrated with its specialized extension, the "Shoe of Brian" board. 
                         
                         
                             
                         More details about how the electronic parts are connected and designed will be given in the @ref firmware section. 
                         This part of the document will clearly explain how all the components work together.
                         
    @section sec_4      SIMULATION
                        The simulation aspect of this project involves creating a model and manually deriving the equations of motion for ROMI. 
                        Two solvers, the Euler solver and the RK4 solver, are used to predict and control ROMI's path based on the velocities of both wheels. 
                        The simulation considers two approaches: the first involves selecting the turning radius and speed of ROMI, while the second focuses on determining the wheel speeds as a function of time.
                        
                        These simulations are then integrated into either Jupyter Notebook or MATLAB with detailed results presented in the @ref simulation section. 
                        However, understanding the underlying physics and geometry of these equations can be challenging. 
                        A figure is provided below, which illustrates the hand-derived model of ROMI in a state-space vector format, complete with explanations of all parameters and their dimensions.
                         

    
    @section sec_5      FINAL DESIGN
                        The final CAD design of the ROMI robot includes an array of components: a digital line sensor module with five channels, an analog line sensor module, an ultrasonic distance sensor, two DC motors each equipped with built-in encoders, and two micro servos. 
                        The complete assembly of ROMI, representing the culmination of the term project, is depicted in the figure below. 
                        This design is current as of December 13, 2023. Please note that any further updates beyond this date will not be included in this portfolio due to time constraints.
                        
                        
      
    @section sec_6      TASK DIAGRAM
                        The robot will concurrently execute four tasks, as outlined in the Task Diagram below. 
                        This diagram specifies the duration (in ms) and relative priority of each task. 
                        These tasks will be scheduled according to their assigned priorities and periods using a scheduler script, the code for which has been provided by Lecturer Charlie Refvem.
                        
                        Note: All diagrams are listed and explain in detail at @ref diagram for futher more description
                        
                        
                        
    @section sec_7      MILESTONES DEMO
                        Below are four consecutive milestones that are overcome to complete the project as describe in the objective section. ROMI should first be able to follow any type of black line that is drawn, avoid a random wall obstacle at any point, stop at the predetermined target, the finally return at the Home position
                        Furthermore about the logic behind the performance, please visit the Task Diagram as well as the Finite State Machine Diagram at @ref diagram, also state diagram can approach at the task section below:
                            
                        task_MOT.py - Control ROMI motor base on input share from different task  
                        
                        task_IMU.py - Rrun BNO055 IMU Sensor and processing the data
                        
                        task_ULS.py - Managing Ultrasonic Sensor readings in a state machine manner
                        
                        task_SER.py - Control servo motors based on external signals and states
                            
                        
                        
                        Line Following Demo
                        
                        This demonstration focus the consistency of the line-following function and the ROMI's capability to recognize the absence of a line signal. 
                        When no line is detected, the ROMI will slow down in explore mode. 
                        This function marks the first milestone of the whole project
                        
                        
                        
                        Wall Obstacle Avoiding Demo
                        
                        This demonstration focus on the capability of avoiding wall obstacles.
                        As illustrated in the small GIF figure below, ROMI is able to adapt to obstacles at any size and will return back the track as soon as the ultrasonic distance sensor can not detect the wall anymore.
                        This design will make sure ROMI can getaway from any obstacle size and loction not just the praticing obstacle in the lab.
                        This function marks the second milestone of the whole project
                        
                        
                        
                        Stop at Target Demo
                        
                        This demonstration focus on the ability of stop at the Target after avoiding the obstacle. When no line is detected, the ROMI will slow down in explore mode and keep track of the traveled distance since its translate in to explore mode.
                        If the distance is greater than 0.15 [m] or 15 [cm], ROMI will stop and notice that as the Target.
                        This function marks the third milestone of the whole project
                        
                        
                        
                        Return Home Demo
                        
                        This demonstration focus on the ability of returning Home after reaching the Target. By collecting the IMU yaw corrected yaw angle and the distance travel of very cycle of task, ROMI is able to keep track of X and Y global cordinate which is exactly the same
                        cordinate from the hand derivation of the previous sectio that can be found at @ref simulation. Then the returning goal can be breakdown to 2 distingush state, return y until y ~ 0 [m] and then return x until x ~ 0 [m]. 
                        This function marks the final milestone of the whole project
                        
                        
                        
    @section sec_8      FULLCOURSE DEMONSTRATION
                        As detailed in @ref sec_1 Section, the integration of all milestones archived in  @ref sec_7 is more than sufficient to enable the autonomous two-wheeled robot ROMi to successfully complete the practice course outlined
                        
                        The final run result in ROMI is able to complete the whole course and return to the starting location in [33 seconds] total.
                        
                        The final course setup is described in figure below for competitors.
                        
                        @image html track.png
                        
                        Note: Real-time video URL link is accessible in @ref sec_yout
    
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