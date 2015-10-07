from myo import Myo
import sys
import math

last_pose = None

def printData(myo):
  global last_pose
  
  # Rotation is represented by number of stars (as in hello-myo.exe)
  (roll_str, pitch_str, yaw_str) = ["*" * int(r) for r in myo.getRotationScaled(18.0)]
  #roll_str = ["*" * int(myo.getRoll()*180/17*math.pi)]
  #pitch_str = ["*" * int(myo.getPitch()*180/17*math.pi)]
  #yaw_str = ["*" * int(myo.getYaw()*180/math.pi)]
  
  
  arm_str = myo.getArmString()
  
  pose_str = myo.getPoseString()
  
  # Print out the rotation and arm state on the same line each update
  sys.stdout.write('\r[{:17s}][{:17s}][{:17s}][{:1s}][{:15s}]'.format(
      roll_str,
      pitch_str,
      yaw_str,
      arm_str, 
      pose_str,
    )
  )
  
  if (pose_str == "fist") and (last_pose != myo.getPose()):
    myo.vibrate(Myo.VIBE_MEDIUM)
  
  last_pose = myo.getPose()

"""def main():
  myMyo = Myo(callback=printData)
  myMyo.daemon = True
  myMyo.start()
  raw_input("Press enter to exit")
      
if __name__ == "__main__":
    main()
"""