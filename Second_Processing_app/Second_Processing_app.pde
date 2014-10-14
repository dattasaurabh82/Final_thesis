import com.temboo.core.*;
import com.temboo.Library.Dropbox.FilesAndMetadata.*;
import com.temboo.Library.Utilities.Encoding.*;

import SimpleOpenNI.*;

SimpleOpenNI  kinect;

PrintWriter storedOutPut;
PrintWriter tempOutPut;

PVector com = new PVector();                                   
PVector com2d = new PVector(); 

float shoulderAngle, elbowAngle;

String timestamp;

// Create a session using your Temboo account application details
TembooSession session = new TembooSession("dattasaurabh82", "myFirstApp", "913f5105-8360-4642-8");
// The name of your Temboo Dropbox Profile 
String dropboxProfile = "DropBoxTemboo";
// Declare file name and content strings
String fileName, b64FileContents;


void setup()
{
  size(640, 480);

  kinect = new SimpleOpenNI(this);
  if (kinect.isInit() == false)
  {
    println("Can't init SimpleOpenNI, maybe the camera is not connected!"); 
    exit();
    return;
  }

  // enable depthMap generation 
  kinect.enableDepth();
  kinect.enableRGB();

  // enable skeleton generation for all joints
  kinect.enableUser();
  //kinect.setMirror(true);

  //create the .txt file with a time stamp on it's name
  timestamp = year() + "_" + nf(month(),2) + "_"+ nf(day(),2) + "__"  + nf(hour(),2) + "_"+ nf(minute(),2) +"_"+ nf(second(),2);
  //println(timestamp);
  tempOutPut = createWriter("joint_data.txt");
  storedOutPut = createWriter("E:\\Test\\Second_Processing_app\\data_files\\" + "joint_data" + timestamp + ".txt");
// Set file name and contents
  
  fileName = "joint_data"+timestamp+".txt";
  //fileContents = "You just made this file with Processing and Temboo! (Now you can put something more awesome here.)";

}

void draw()
{
  //update the cam
  kinect.update();
  //over lay normal image
  PImage normalImage = kinect.rgbImage();
  image(normalImage, 0, 0);
  filter(GRAY);


  //Get user list
  int[] userList = kinect.getUsers();
  for (int i=0; i<userList.length; i++)
  {
    //int userId = userList.get(0);
    if (kinect.isTrackingSkeleton(userList[i]))
    {
      //draw the skeleton if it's available
      stroke(255, 255, 255); 
      strokeWeight(7); 
      smooth();
      drawSkeleton(userList[i]);

      //Get the positions of the three joints of the arm.

      //Assign the co-ordinates as vectors.
      PVector rightHand = new PVector();
      PVector rightElbow = new PVector();
      PVector rightShoulder = new PVector();
      PVector rightHip = new PVector();

      kinect.getJointPositionSkeleton(userList[i], SimpleOpenNI.SKEL_RIGHT_HAND, rightHand);
      kinect.getJointPositionSkeleton(userList[i], SimpleOpenNI.SKEL_RIGHT_ELBOW, rightElbow);
      kinect.getJointPositionSkeleton(userList[i], SimpleOpenNI.SKEL_RIGHT_SHOULDER, rightShoulder);
      //We need right hip to orient the shoulder angle.
      kinect.getJointPositionSkeleton(userList[i], SimpleOpenNI.SKEL_RIGHT_HIP, rightHip);

      //reduce our joint vectors to two dimensions.
      PVector rightHand2D = new PVector(rightHand.x, rightHand.y);
      PVector rightElbow2D = new PVector(rightElbow.x, rightElbow.y);
      PVector rightShoulder2D = new PVector(rightShoulder.x, rightShoulder.y);
      PVector rightHip2D = new PVector(rightHip.x, rightHip.y);

      //calculating the reference axes.
      PVector torsoOrientation = PVector.sub(rightShoulder2D, rightHip2D);
      PVector upperArmOrientation = PVector.sub(rightElbow2D, rightShoulder2D);

      //calculating the angles between the joints
      shoulderAngle = angleOf(rightElbow2D, rightShoulder2D, torsoOrientation);
      elbowAngle = angleOf(rightHand2D, rightElbow2D, upperArmOrientation);

      //Show the angles on the screen
      fill(255);
      text("Shoulder Angle: " + int(shoulderAngle) + "\n" + "Elbow Angle : " + int(elbowAngle), 20, 100);
      tempOutPut.print("Shoulder Angle: " + shoulderAngle + "," + " " + "Elbow Angle: " + elbowAngle);
      //fileContents = shoulderAngle;
    }
  }
}

//
float angleOf(PVector one, PVector two, PVector axis) {
  PVector limb = PVector.sub(two, one);
  return degrees(PVector.angleBetween(limb, axis));
}

// draw the skeleton with the selected joints
void drawSkeleton(int userId)
{
  // to get the 3d joint data
  /*
  PVector jointPos = new PVector();
   kinect.getJointPositionSkeleton(userId,SimpleOpenNI.SKEL_NECK,jointPos);
   println(jointPos);
   */

  kinect.drawLimb(userId, SimpleOpenNI.SKEL_HEAD, SimpleOpenNI.SKEL_NECK);

  kinect.drawLimb(userId, SimpleOpenNI.SKEL_NECK, SimpleOpenNI.SKEL_LEFT_SHOULDER);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER, SimpleOpenNI.SKEL_LEFT_ELBOW);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_ELBOW, SimpleOpenNI.SKEL_LEFT_HAND);

  kinect.drawLimb(userId, SimpleOpenNI.SKEL_NECK, SimpleOpenNI.SKEL_RIGHT_SHOULDER);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER, SimpleOpenNI.SKEL_RIGHT_ELBOW);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_ELBOW, SimpleOpenNI.SKEL_RIGHT_HAND);

  kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER, SimpleOpenNI.SKEL_TORSO);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER, SimpleOpenNI.SKEL_TORSO);

  kinect.drawLimb(userId, SimpleOpenNI.SKEL_TORSO, SimpleOpenNI.SKEL_LEFT_HIP);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_HIP, SimpleOpenNI.SKEL_LEFT_KNEE);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_KNEE, SimpleOpenNI.SKEL_LEFT_FOOT);

  kinect.drawLimb(userId, SimpleOpenNI.SKEL_TORSO, SimpleOpenNI.SKEL_RIGHT_HIP);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_HIP, SimpleOpenNI.SKEL_RIGHT_KNEE);
  kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_KNEE, SimpleOpenNI.SKEL_RIGHT_FOOT);
}

// -----------------------------------------------------------------
// SimpleOpenNI events

void onNewUser(SimpleOpenNI curkinect, int userId)
{
  println("onNewUser - userId: " + userId);
  println("\tstart tracking skeleton");
  fill(255);
  text("onNewUser - userId: " + userId + "\n" + "start tracking skeleton", 20, 20);
  curkinect.startTrackingSkeleton(userId);
}

void onLostUser(SimpleOpenNI curkinect, int userId)
{
  println("onLostUser - userId: " + userId);
  fill(255);
  text("onLostUser - userId: " + userId, 20, 60);
}

void onVisibleUser(SimpleOpenNI curkinect, int userId)
{
  println("onVisibleUser - userId: " + userId);
  fill(255);
  text("onVisibleUser - userId: " + userId, 20, 80);
}


void keyPressed()
{
  switch(key)
  {
  //case 's':
  //case 'S':
    //tempOutPut.println("Shoulder Angle: " + shoulderAngle + "," + " " + "Elbow Angle: " + elbowAngle);
  //  break;
//
  case 'o':
  case 'O':
    tempOutPut.flush();
    storedOutPut.flush(); 
    tempOutPut.close();
    tempOutPut.close();
    
    // Base64 encode a string and upload it to Dropbox
    runBase64EncodeChoreo();
    runUploadFileChoreo();
    
    exit();
  }
}  

void runBase64EncodeChoreo() {
  
  String[] fileContents = loadStrings("joint_data.txt");
  String joinedContents = join(fileContents,",");
  // Create the Choreo object using your Temboo session
  Base64Encode base64EncodeChoreo = new Base64Encode(session);

  // Set inputs
  base64EncodeChoreo.setText(joinedContents);

  // Run the Choreo and store the results
  Base64EncodeResultSet base64EncodeResults = base64EncodeChoreo.run();

  // Set base64FileContents
  b64FileContents = base64EncodeResults.getBase64EncodedText();
  println(fileName+" has been Base64 encoded...");
}

void runUploadFileChoreo() {
  // Create the Choreo object using your Temboo session
  UploadFile uploadFileChoreo = new UploadFile(session);

  // Set Profeil
  uploadFileChoreo.setCredential(dropboxProfile);

  // Set inputs
  uploadFileChoreo.setFileName(fileName);
  uploadFileChoreo.setFileContents(b64FileContents);

  // Run the Choreo and store the results
  UploadFileResultSet uploadFileResults = uploadFileChoreo.run();
  println("and uploaded to Dropbox!");
}
