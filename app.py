import cv2

def main():
    # Prompt user to enter the RTSP URL
    rtsp_url = input("Enter the RTSP URL of the CCTV camera: ")

    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Error: Could not open RTSP stream. Please check the URL.")
        return

    # Loop to continuously get frames
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Error: Cannot receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('CCTV Feed', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
