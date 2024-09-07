{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "778505d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Admin\\AppData\\Roaming\\Python\\Python311\\site-packages\\google\\protobuf\\symbol_database.py:55: UserWarning: SymbolDatabase.GetPrototype() is deprecated. Please use message_factory.GetMessageClass() instead. SymbolDatabase.GetPrototype() will be removed soon.\n",
      "  warnings.warn('SymbolDatabase.GetPrototype() is deprecated. Please '\n"
     ]
    }
   ],
   "source": [
    "# pip install opencv-python mediapipe tensorflow numpy\n",
    "\n",
    "# Step 1: Import Libraries\n",
    "import cv2\n",
    "import mediapipe as mp\n",
    "\n",
    "# Step 2: Initialize MediaPipe Hands\n",
    "mp_hands = mp.solutions.hands\n",
    "hands = mp_hands.Hands()\n",
    "mp_draw = mp.solutions.drawing_utils\n",
    "\n",
    "# Step 3: Initialize Video Capture\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "# Step 4: Capture and Process Each Frame\n",
    "while cap.isOpened():\n",
    "    ret, frame = cap.read()\n",
    "    if not ret:\n",
    "        break\n",
    "\n",
    "    # Flip the frame horizontally for a later selfie-view display\n",
    "    frame = cv2.flip(frame, 1)\n",
    "    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)\n",
    "    results = hands.process(frame_rgb)\n",
    "\n",
    "    # Check if any hands are detected\n",
    "    if results.multi_hand_landmarks:\n",
    "        for hand_landmarks in results.multi_hand_landmarks:\n",
    "            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)\n",
    "\n",
    "            # Initialize list to store landmark coordinates\n",
    "            landmark_list = []\n",
    "            for id, lm in enumerate(hand_landmarks.landmark):\n",
    "                # Get the coordinates\n",
    "                h, w, c = frame.shape\n",
    "                cx, cy = int(lm.x * w), int(lm.y * h)\n",
    "                landmark_list.append([cx, cy])\n",
    "\n",
    "            # Gesture recognition logic\n",
    "            if len(landmark_list) != 0:\n",
    "                # Example logic for gesture recognition\n",
    "                # Open Hand (Palm) Gesture\n",
    "                if landmark_list[4][1] < landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:\n",
    "                    gesture = \"Syntax Sarcasm\"\n",
    "                # Pointing Up Gesture\n",
    "                elif landmark_list[4][1] > landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:\n",
    "                    gesture = \"Join the Workshop\"\n",
    "                else:\n",
    "                    gesture = None\n",
    "\n",
    "                # Display the corresponding text\n",
    "                if gesture:\n",
    "                    cv2.putText(frame, gesture, (landmark_list[0][0] - 50, landmark_list[0][1] - 50),\n",
    "                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)\n",
    "\n",
    "    # Step 5: Display the Frame\n",
    "    cv2.imshow('Hand Gesture Recognition', frame)\n",
    "\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "# Step 6: Release Resources\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90f56843",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
