from vex import *

brain = Brain()
controller = Controller()


def Drive():
        # Intialize all drivetrain motors
        # Higher gear ratio means more torque and if true motor is upside down
        motor1 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
        # Both motors 2 and 3 are upside down
        motor2 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
        motor3 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)

        motor4 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)

        # Respective motor sides grouped together using premade motor group function so all can be spun at the same time
        left_side = MotorGroup(motor1, motor4)
        right_side = MotorGroup(motor2, motor3)
        
        # Group all motors and sides  and retrun all from function
        Motor_List = [left_side, right_side]
        return Motor_List
    


def Autonomus():
 
    # Get motor list from drive function
    Motor_List = Drive()

    # Assign left and right side motors to variables
   
    left_side = Motor_List[0]
    right_side = Motor_List[1]

    # Drivtrain allowed me to group left and right side motors together so two groups in one
    Wheels = DriveTrain(left_side, right_side)
    
    # Print to brain screen to show autonomus has started
    brain.screen.print("Autonomous start")

    # Autonomus commands

    # Velocity and direction
    Wheels.set_drive_velocity(100, PERCENT)
    Wheels.drive(FORWARD)

    # Duration of time motor spins
    wait(.5, SECONDS)

    # Stop spin but allow rotation if any
    Wheels.stop(BrakeType.COAST)

    
    Wheels.drive(REVERSE)
    wait(.5, SECONDS)
    Wheels.stop(BrakeType.COAST)


    # Make bot spin to the right
    left_side.set_velocity(100, VelocityUnits.PERCENT)
    left_side.spin(FORWARD)
    wait(.5, SECONDS)
    left_side.stop(BrakeType.COAST)

    # Make bot spin to the left
    right_side.set_velocity(100, VelocityUnits.PERCENT)
    right_side.spin(FORWARD)
    wait(.5, SECONDS)
    right_side.stop(BrakeType.COAST)

    # Make bot spin in place
    left_side.spin(FORWARD)
    right_side.spin(REVERSE)
    wait(3, SECONDS)

    left_side.stop(BrakeType.COAST)
    right_side.stop(BrakeType.COAST)

    # Clear screen after autonomus ends
    brain.screen.clear_screen()
    return

if __name__ == "__main__":
    def main():
        
        Autonomus()
        brain.program_stop()
    main()