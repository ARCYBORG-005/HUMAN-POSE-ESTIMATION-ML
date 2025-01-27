# HUMAN-POSE-ESTIMATION-ML
AICTE ASP MICROSOFT INTERNSHIP

*GitHub Project Repository: Pose Detection Application*

*Overview:*  
This repository contains the implementation of a Pose Detection application built using Python, OpenCV, Streamlit, and Mediapipe. The application is designed to detect human body landmarks, such as joints and facial features, from video or image inputs. The system marks each joint with a distinctive dot and connects them with lines to visualize the human pose. It uses real-time video analysis, offering a practical solution for fitness tracking, sports analysis, or rehabilitation exercises.

*Key Features:*  
- *Pose Detection:* The model detects 33 body landmarks, including major joints and facial features (eyes, nose, and mouth), in real-time video or image inputs.
- *Visualization:* Detected landmarks are visualized with connected lines, highlighting human body posture.
- *User Interface:* Streamlit is used to create an intuitive interface where users can upload videos or images to detect poses. The interface displays the results interactively.
- *Single Person Detection:* The application is currently optimized to detect poses of a single person per input. This limitation ensures better accuracy and performance for individual analysis.

*Technologies Used:*  
- *Python:* Primary programming language used for application development.  
- *OpenCV:* For video/image processing.  
- *Mediapipe:* For pose estimation, providing an efficient model to detect human body landmarks.  
- *Streamlit:* For creating an interactive user interface to display results and take user inputs.  

*How to Run the Application:*  
1. Clone this repository to your local machine.
2. Install the required libraries:  
   
   pip install -r requirements.txt
   
3. Run the Streamlit app:
   
   streamlit run app.py
   
4. Upload a video or image to detect poses and visualize the landmarks.

*Future Improvements:*  
- Support for multi-person pose detection in videos with the ability to differentiate between multiple individuals.
- Integration with machine learning models for activity recognition based on the detected poses.
- Real-time performance optimization for faster processing and scalability across multiple platforms.
- Compatibility with mobile devices and cloud-based services for broader accessibility.

*Conclusion:*  
This Pose Detection application serves as a basic yet powerful tool for visualizing and analyzing human body movements. It has significant potential for fitness, sports analytics, and rehabilitation applications. The code is optimized for simplicity, making it easy to understand and extend for further research or real-world applications.
