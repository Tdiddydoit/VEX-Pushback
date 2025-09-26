# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Terrance Haris                                               #
# 	Created:      9/22/2025, 4:12:24 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain and controller pre made functions
brain=Brain()
controller = Controller()

class Bot_Motors():
    def Drivetrain(self):
        # Intialize all drivetrain motors
        # Higher gear ratio means more torque and if true motor is upside down
        motor1 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
        # Both motors 2 and 3 are upside down
        motor2 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
        motor3 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)

        motor4 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)

        # Respective motor sides grouped together using premade motor group function so all can be spun at the same time
        self.left_side = MotorGroup(motor1, motor4)
        self.right_side = MotorGroup(motor2, motor3)

        # Group all motors and sides  and retrun all from function
        DriveTrain = [motor1,motor2,motor3,motor4, self.left_side, self.right_side]
        return DriveTrain

# Initialize robot motors and create a MotorGroup for all drive motors
bot = Bot_Motors()
# returns [m1, m2, m3, m4, left_group, right_group]
Motor_list = bot.Drivetrain()

def Autonomus():

    # The first four items are the individual motors
    motors = Motor_list[0:4]
    All_Wheels = MotorGroup(motors)

    brain.screen.clear_line()
    brain.screen.print("Autonomous start")

    # Autonomus commands

    # Velocity and direction
    All_Wheels.set_velocity(100, VelocityUnits.PERCENT)
    All_Wheels.spin(FORWARD)

    # Duration of motor spins
    wait(3, SECONDS)

    # Stop spin but allow rotation if any
    All_Wheels.stop(BrakeType.COAST)

    All_Wheels.set_velocity(100, VelocityUnits.PERCENT)
    All_Wheels.spin(REVERSE)
    wait(3, SECONDS)
    All_Wheels.stop(BrakeType.COAST)

    # Clear screen after autonomus ends
    brain.screen.clear_screen()


def User_Control():
    # Print user contol on screen
    brain.screen.print("User Control")
   



    # grab left and right side from dirvetrain class
    left_side = Motor_list[4]
    right_side = Motor_list[5]

    # Constanly read and apply  joystick postions while in user control
    while True:
        # Read joystick positions
        LeftJoy = controller.axis3.position()
        RightJoy = controller.axis2.position()

        # Control motors via joystick position
        # Sin motors at the same power as the postion of the joystick
        def apply_joy_to_group(Side, Joy):
            if Joy > 0:
                Side.spin(FORWARD, Joy, VelocityUnits.PERCENT)
            elif Joy < 0:
                Side.spin(REVERSE, abs(Joy), VelocityUnits.PERCENT)
            else:
                Side.stop(BrakeType.COAST)

        # Pass motor sides and Joystick postions to function
        apply_joy_to_group(left_side, LeftJoy)
        apply_joy_to_group(right_side, RightJoy)

        # Display joystick values on screen
        brain.screen.set_cursor(2, 1)  # Line 2, column 1
        brain.screen.print("L: ", LeftJoy, "  R: ", RightJoy, "   ")

        wait(20, TimeUnits.MSEC)  # Small delay for smoother updates

        if LeftJoy & RightJoy == 0:
            wait(10, SECONDS)
            break



if __name__ == "__main__":
    def main():
        # Call everything in and run main 
        Autonomus()
        User_Control()
        brain.program_stop()
    main()
