################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import os, sys, inspect, time
sys.path.append("LeapSDK/lib/Leap")
sys.path.append("LeapSDK/lib/x86")
sys.path.append("LeapSDK/lib")
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    paintX = int(1200/2)
    paintY = int(695/2)
    paintZ = False

    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Connected")

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")
    def isBrushPress():
        return brushPress
    def indexDistalPosX(self):
        tempX = 0
        if self.paintX< -70 :
            tempX = -70
        elif self.paintX > 150:
            tempX =  150
        else:
            tempX = self.paintX
        tempX = abs(tempX+70)*5.45
        return tempX
        
    def indexDistalPosY(self):
        tempY = 0
        if self.paintY< 100:
            tempY = 100
        elif self.paintY > 250:
            tempY = 250
        else:
            tempY = self.paintY

        tempY = abs(tempY-250)*6.75
        return tempY
    def brushPress(self):
        if self.paintZ <= -50:
            return True
        else:
            return False

    def on_frame(self, controller):
        
        # Get the most recent frame and report some basic information
        frame = controller.frame()

##        print ("Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
##              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures())))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

##            print ("  %s, id %d, position: %s" % (
##                handType, hand.id, hand.palm_position))

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
##            print ("  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
##                direction.pitch * Leap.RAD_TO_DEG,
##                normal.roll * Leap.RAD_TO_DEG,
##                direction.yaw * Leap.RAD_TO_DEG))

            # Get arm bone
            arm = hand.arm
##            print ("  Arm direction: %s, wrist position: %s, elbow position: %s" % (
##                arm.direction,
##                arm.wrist_position,
##                arm.elbow_position))

            # Get fingers
            for finger in hand.fingers:

##                print ("    %s finger, id: %d, length: %fmm, width: %fmm" % (
##                    self.finger_names[finger.type()],
##                    finger.id,
##                    finger.length,
##                    finger.width))

                # Get bones
                for b in range(4):
                    bone = finger.bone(b)
                    if b==1:
                        self.paintX = int(bone.next_joint.x)
                        self.paintY = int(bone.next_joint.y)
                        self.paintZ = int(bone.next_joint.z)
                        sys.stdout.write('\r[{}][{}][{}]'.format(self.indexDistalPosX(),self.indexDistalPosY(),self.brushPress()))
                        

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

"""def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)"""


