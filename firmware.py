'''! @page firmware Electronic & Firmware
    @section sec_o      Overview 
                        This card dealer machine project is centered around an Arduino Nano, selected for its compact size and efficient logic control, 
                        paired with two NEMA 17 stepper motors—one for the machine's rotation and another for card dealing precision. 
                        The user interface combines a small OLED screen for crisp information display, including player count and game settings, and a 12x4 keyboard for easy data entry, all within a design that's both space-efficient and durable for continuous use. 
                        Detailed interconnectivity and operation of these electronic components will be further elaborated in the firmware documentation section.
                         
    @section sec_1      Custom PCB
                        To improve both the visual appeal and the ease of debugging or replicating your project, consider implementing these enhancements in your custom PCB, designed with EasyEDA software:
                            
                                1. 1 Arduino Nano
                                2. 3 DRV8825 Stepper Motor Driver 
                                3. 1 Connection for the keypad
                                4. 1 Connection for the OLED screen
                                5. 6 Filter capacitors
                            
                        @image html pcb.png
                        
    @section sec_1s     Schematic Diagram
                        Overall, the schematic below describe the connections between pins and electronics component of the robot.
                        Keynote:
                            1. Power voltage 12V for Stepper Motor (2 pins)
                            2. Power voltage 9V for Arduino Nano (2 pins)
                            3. Stepper Driver Motor (16 pins/each)
                            4. OLED Screen (4 pins)
                            5. Keyboard 4x4 (8 pins)
                            
                        @image html connection.png
                        
    @section sec_2      Arduino Nano
                        The project will utilize the Arduino Nano as its microcontroller. 
                        The key benefit of selecting the Arduino Nano lies in its compact size, coupled with a sufficient number of pins to effectively manage all the necessary components.
                        
                        @image html mcu.png
                        
                        
    @section sec_3      Step Down Regulator
                        The design is configured to operate two stepper motors using a 12V input voltage. 
                        However, since the Arduino Nano microcontroller functions at 9V, directly applying 12V would damage it. 
                        Therefore, the inclusion of a step-down regulator is essential to convert the voltage from 12V to 9V, thereby safely powering the Arduino Nano microcontroller.
                        
                        @image html stepdown.png
                        
    @section sec_32     DRV8825 Stepper Motor Driver 
                        For saving pins from the controller and simplified the control of 2 stepper motor (usually need 4 pwm pins). 
                        Consider DRV8825 driver can save up to 2 pins for every operating stepper motor
                        
                        @image html driver.png              
                        
                        
    @section sec_4      NEMA 17 Stepper Motor 
                        The NEMA 17 Stepper Motor is chosen for its simplicity and user-friendliness, in addition to its high torque capabilities.
                        @image html nema.png
                        
    @section sec_5      OLED Screen
                        Small OLED Screen is connected to the microcontroller using I2C communication for display the state of the robot and supporting the user-interface
                        @image html oled.png
                        
                        
    @section sec_6      Keyboard 4x4
                        A 4x4 keyboard is sufficient for all the purposes of the robot
                        @image html keyboard.png
                        
                        
    @section sec_7      RGB LED     
                        A simple RGB LED is connect to blink green as valid input and blink red as invalid input
                        @image html led.png   
                        
                        
   @author              Vinh Vo
   @date                Sep 12, 2023
'''