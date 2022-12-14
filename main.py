# Real Time Human Detection & Counting
# imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import argparse
from Human_Detection import Detector
import imutils

# Main Window & Configuration
window = tk.Tk()
window.title("Real Time Human Detection & Counting")
window.iconbitmap('Images/icon.ico')
window.geometry('1000x700')

# top label
start1 = tk.Label(text="REAL-TIME-HUMAN\nDETECTION  &  COUNTING",
                  font=("Arial", 50, "underline"), fg="magenta")  # same way bg
start1.place(x=100, y=20)

# function defined to start the main application


def start_fun():
    window.destroy()


# created a start button
Button(window, text="▶ START", command=start_fun, font=("Arial", 25), bg="orange",
       fg="blue", cursor="hand2", borderwidth=3, relief="raised").place(x=130, y=570)

# image on the main window
path1 = "Images/front2.png"
img2 = ImageTk.PhotoImage(Image.open(path1))
panel1 = tk.Label(window, image=img2)
panel1.place(x=90, y=250)

# image on the main window
path = "Images/front1.png"
img1 = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image=img1)
panel.place(x=380, y=180)

exit1 = False
# function created for exiting from window


def exit_win():
    global exit1
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        exit1 = True
        window.destroy()


# exit button created
Button(window, text="❌ EXIT", command=exit_win, font=("Arial", 25), bg="red",
       fg="blue", cursor="hand2", borderwidth=3, relief="raised").place(x=680, y=570)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

if exit1 == False:
    # Main Window & Configuration of window1
    window1 = tk.Tk()
    window1.title("Real Time Human Detection & Counting")
    window1.iconbitmap('Images/icon.ico')
    window1.geometry('1000x700')

    filename = ""
    filename1 = ""
    filename2 = ""

    def argsParser():
        arg_parse = argparse.ArgumentParser()
        arg_parse.add_argument(
            "-v", "--video", default=None, help="path to Video File ")
        arg_parse.add_argument(
            "-i", "--image", default=None, help="path to Image File ")
        arg_parse.add_argument("-c", "--camera", default=False,
                               help="Set true if you want to use the camera.")
        arg_parse.add_argument("-o", "--output", type=str,
                               help="path to optional output video file")
        args = vars(arg_parse.parse_args())
        return args

    # ---------------------------- image section ------------------------------------------------------------
    # ---------------------------- image section ------------------------------------------------------------
    # ---------------------------- image section ------------------------------------------------------------
    # ---------------------------- image section ------------------------------------------------------------
    # ---------------------------- image section ------------------------------------------------------------
    # ---------------------------- image section ------------------------------------------------------------
    # ---------------------------- image section ------------------------------------------------------------
    def image_option():
        # new windowi created for image section
        windowi = tk.Tk()
        windowi.title("Human Detection from Image")
        windowi.iconbitmap('Images/icon.ico')
        windowi.geometry('1000x700')

        # function defined to open the image
        def open_img():
            global filename1, max_count1, framex1, county1, max1, avg_acc1_list, max_avg_acc1_list, max_acc1, max_avg_acc1
            max_count1 = 0
            framex1 = []
            county1 = []
            max1 = []
            avg_acc1_list = []
            max_avg_acc1_list = []
            max_acc1 = 0
            max_avg_acc1 = 0

            filename1 = filedialog.askopenfilename(
                title="Select Image file", parent=windowi)
            path_text1.delete("1.0", "end")
            path_text1.insert(END, filename1)

        # function defined to detect the image
        def det_img():
            global filename1, max_count1, framex1, county1, max1, avg_acc1_list, max_avg_acc1_list, max_acc1, max_avg_acc1
            max_count1 = 0
            framex1 = []
            county1 = []
            max1 = []
            avg_acc1_list = []
            max_avg_acc1_list = []
            max_acc1 = 0
            max_avg_acc1 = 0

            image_path = filename1
            if(image_path == ""):
                mbox.showerror(
                    "Error", "No Image File Selected!", parent=windowi)
                return
            info1.config(text="Status : Detecting...")
            # info2.config(text="                                                  ")
            mbox.showinfo("Status", "Detecting, Please Wait...",
                          parent=windowi)
            # time.sleep(1)
            detectByPathImage(image_path)

            info1.config(text="Status : Detection & Counting Completed")

        # main detection process process here

        def detectByPathImage(path):
            global filename1, max_count1, framex1, county1, max1, avg_acc1_list, max_avg_acc1_list, max_acc1, max_avg_acc1
            max_count1 = 0
            framex1 = []
            county1 = []
            max1 = []
            avg_acc1_list = []
            max_avg_acc1_list = []
            max_acc1 = 0
            max_avg_acc1 = 0

            #  detect image
            img = cv2.imread(path)
            img = imutils.resize(img, width=700)
            img = Detector(img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.imshow("Human Detection from Image", img)
            # info1.config(
            #     text="                                                  ")
            # info1.config(text="Status : Detection & Counting Completed")
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        def prev_img():
            global filename1
            img = cv2.imread(filename1, 1)
            cv2.imshow("Selected Image Preview", img)

        # for images ----------------------
        lbl1 = tk.Label(windowi, text="DETECT  FROM\nIMAGE",
                        font=("Arial", 50, "underline"), fg="brown")
        lbl1.place(x=230, y=20)
        lbl2 = tk.Label(windowi, text="Selected Image",
                        font=("Arial", 30), fg="green")
        lbl2.place(x=80, y=200)
        path_text1 = tk.Text(windowi, height=1, width=37, font=(
            "Arial", 30), bg="light yellow", fg="orange", borderwidth=2, relief="solid")
        path_text1.place(x=80, y=260)

        Button(windowi, text="SELECT", command=open_img, cursor="hand2", font=(
            "Arial", 20), bg="light green", fg="blue").place(x=220, y=350)
        Button(windowi, text="PREVIEW", command=prev_img, cursor="hand2",
               font=("Arial", 20), bg="yellow", fg="blue").place(x=410, y=350)
        Button(windowi, text="DETECT", command=det_img, cursor="hand2",
               font=("Arial", 20), bg="orange", fg="blue").place(x=620, y=350)

        info1 = tk.Label(windowi, font=("Arial", 30), fg="gray")
        info1.place(x=100, y=445)
        # info2 = tk.Label(windowi,font=("Arial", 30), fg="gray")
        # info2.place(x=100, y=500)

        def exit_wini():
            if mbox.askokcaxncel("Exit", "Do you want to exit?", parent=windowi):
                windowi.destroy()
        windowi.protocol("WM_DELETE_WINDOW", exit_wini)

    # ---------------------------- video section ------------------------------------------------------------
    # ---------------------------- video section ------------------------------------------------------------
    # ---------------------------- video section ------------------------------------------------------------
    # ---------------------------- video section ------------------------------------------------------------
    # ---------------------------- video section ------------------------------------------------------------
    # ---------------------------- video section ------------------------------------------------------------
    # ---------------------------- video section ------------------------------------------------------------
    # ---------------------------- video section ------------------------------------------------------------

    def video_option():
        # new windowv created for video section
        windowv = tk.Tk()
        windowv.title("Human Detection from Video")
        windowv.iconbitmap('Images/icon.ico')
        windowv.geometry('1000x700')

        # function defined to open the video
        def open_vid():
            global filename2, max_count2, framex2, county2, max2, avg_acc2_list, max_avg_acc2_list, max_acc2, max_avg_acc2
            max_count2 = 0
            framex2 = []
            county2 = []
            max2 = []
            avg_acc2_list = []
            max_avg_acc2_list = []
            max_acc2 = 0
            max_avg_acc2 = 0

            filename2 = filedialog.askopenfilename(
                title="Select Video file", parent=windowv)
            path_text2.delete("1.0", "end")
            path_text2.insert(END, filename2)

        # function defined to detect inside the video
        def det_vid():
            global filename2, max_count2, framex2, county2, max2, avg_acc2_list, max_avg_acc2_list, max_acc2, max_avg_acc2
            max_count2 = 0
            framex2 = []
            county2 = []
            max2 = []
            avg_acc2_list = []
            max_avg_acc2_list = []
            max_acc2 = 0
            max_avg_acc2 = 0

            video_path = filename2
            if (video_path == ""):
                mbox.showerror(
                    "Error", "No Video File Selected!", parent=windowv)
                return
            info1.config(text="Status : Detecting...")
            # info2.config(text="                                                  ")
            mbox.showinfo("Status", "Detecting, Please Wait...",
                          parent=windowv)
            # time.sleep(1)

            args = argsParser()
            writer = None
            if args['output'] is not None:
                writer = cv2.VideoWriter(
                    args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))

            detectByPathVideo(video_path, writer)

            info1.config(text="Status : Detection done")

        # the main process of detection in video takes place here
        def detectByPathVideo(path, writer):
            global filename2, max_count2, framex2, county2, max2, avg_acc2_list, max_avg_acc2_list, max_acc2, max_avg_acc2
            max_count2 = 0
            framex2 = []
            county2 = []
            max2 = []
            avg_acc2_list = []
            max_avg_acc2_list = []
            max_acc2 = 0
            max_avg_acc2 = 0

            cap = cv2.VideoCapture(path)
            # size = (800, int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            # # size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            # print(size)
            # fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'x264' doesn't work
            # out = cv2.VideoWriter('./testing/res_t2.mp4',fourcc, 20.0,(980,498))  # 'False' for 1-ch instead of 3-ch for color

            while True:
                ret, frame = cap.read()
                # frame = cv2.resize(frame,(980,498))
                # frame = imutils.resize(frame, width=800)
                frame = Detector(frame)
                # out.write(frame)
                # cv2.resizeWindow('Car Detection System', 600, 600)
                # k = cv2.waitKey(30) & 0xff
                # if k == 27:
                #     break
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            cv2.destroyAllWindows()

        # funcion defined to preview the selected video
        def prev_vid():
            global filename2
            cap = cv2.VideoCapture(filename2)
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    img = cv2.resize(frame, (800, 500))
                    cv2.imshow('Selected Video Preview', img)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()

        lbl1 = tk.Label(windowv, text="DETECT  FROM\nVIDEO",
                        font=("Arial", 50, "underline"), fg="brown")
        lbl1.place(x=230, y=20)
        lbl2 = tk.Label(windowv, text="Selected Video",
                        font=("Arial", 30), fg="green")
        lbl2.place(x=80, y=200)
        path_text2 = tk.Text(windowv, height=1, width=37, font=(
            "Arial", 30), bg="light yellow", fg="orange", borderwidth=2, relief="solid")
        path_text2.place(x=80, y=260)

        Button(windowv, text="SELECT", command=open_vid, cursor="hand2", font=(
            "Arial", 20), bg="light green", fg="blue").place(x=220, y=350)
        Button(windowv, text="PREVIEW", command=prev_vid, cursor="hand2",
               font=("Arial", 20), bg="yellow", fg="blue").place(x=410, y=350)
        Button(windowv, text="DETECT", command=det_vid, cursor="hand2",
               font=("Arial", 20), bg="orange", fg="blue").place(x=620, y=350)

        info1 = tk.Label(windowv, font=("Arial", 30), fg="gray")  # same way bg
        info1.place(x=100, y=440)

        # function defined to exit from windowv section
        def exit_winv():
            if mbox.askokcancel("Exit", "Do you want to exit?", parent=windowv):
                windowv.destroy()
        windowv.protocol("WM_DELETE_WINDOW", exit_winv)

    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------
    # ---------------------------- camera section ------------------------------------------------------------

    def camera_option():
        # new window created for camera section
        windowc = tk.Tk()
        windowc.title("Human Detection from Camera")
        windowc.iconbitmap('Images/icon.ico')
        windowc.geometry('1000x700')

        # function defined to open the camera
        def open_cam():
            global max_count3, framex3, county3, max3, avg_acc3_list, max_avg_acc3_list, max_acc3, max_avg_acc3
            max_count3 = 0
            framex3 = []
            county3 = []
            max3 = []
            avg_acc3_list = []
            max_avg_acc3_list = []
            max_acc3 = 0
            max_avg_acc3 = 0

            args = argsParser()

            info1.config(text="Status : Opening Camera...")
            # info2.config(text="                                                  ")
            mbox.showinfo(
                "Status", "Opening Camera...Please Wait...", parent=windowc)
            # time.sleep(1)

            writer = None
            if args['output'] is not None:
                writer = cv2.VideoWriter(
                    args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))
            if True:
                detectByCamera(writer)

            info1.config(text="Status : Camera closed")

        # function defined to detect from camera
        def detectByCamera(writer):
            global max_count3, framex3, county3, max3, avg_acc3_list, max_avg_acc3_list, max_acc3, max_avg_acc3
            max_count3 = 0
            framex3 = []
            county3 = []
            max3 = []
            avg_acc3_list = []
            max_avg_acc3_list = []
            max_acc3 = 0
            max_avg_acc3 = 0

            # define a video capture object
            vid = cv2.VideoCapture(0)

            while(True):
                # Capture the video frame
                # by frame
                ret, frame = vid.read()

                # Display the resulting frame
                frame = Detector(frame)

                # the 'q' button is set as the
                # quitting button you may use any
                # desired button of your choice
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # After the loop release the cap object
            vid.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

        lbl1 = tk.Label(windowc, text="DETECT  FROM\nCAMERA", font=(
            "Arial", 50, "underline"), fg="brown")  # same way bg
        lbl1.place(x=230, y=20)

        Button(windowc, text="OPEN CAMERA", command=open_cam, cursor="hand2", font=(
            "Arial", 20), bg="light green", fg="blue").place(x=370, y=230)

        info1 = tk.Label(windowc, font=("Arial", 30), fg="gray")  # same way bg
        info1.place(x=100, y=330)

        # function defined to exit from the camera window
        def exit_winc():
            if mbox.askokcancel("Exit", "Do you want to exit?", parent=windowc):
                windowc.destroy()
        windowc.protocol("WM_DELETE_WINDOW", exit_winc)

    # ----------------------------- options -----------------------------
    # ----------------------------- options -----------------------------
    # ----------------------------- options -----------------------------
    # ----------------------------- options -----------------------------
    # ----------------------------- options -----------------------------
    # ----------------------------- options -----------------------------
    lbl1 = tk.Label(text="OPTIONS", font=(
        "Arial", 50, "underline"), fg="brown")  # same way bg
    lbl1.place(x=340, y=20)

    # image on the main window
    pathi = "Images/image1.jpg"
    imgi = ImageTk.PhotoImage(Image.open(pathi))
    paneli = tk.Label(window1, image=imgi)
    paneli.place(x=90, y=110)

    # image on the main window
    pathv = "Images/image2.png"
    imgv = ImageTk.PhotoImage(Image.open(pathv))
    panelv = tk.Label(window1, image=imgv)
    panelv.place(x=700, y=260)  # 720, 260

    # image on the main window
    pathc = "Images/image3.jpg"
    imgc = ImageTk.PhotoImage(Image.open(pathc))
    panelc = tk.Label(window1, image=imgc)
    panelc.place(x=90, y=415)

    # created button for all three option
    Button(window1, text="DETECT  FROM   IMAGE ➡", command=image_option, cursor="hand2",
           font=("Arial", 30), bg="light green", fg="blue").place(x=350, y=150)
    Button(window1, text="DETECT  FROM  VIDEO ➡", command=video_option, cursor="hand2", font=(
        "Arial", 30), bg="light blue", fg="blue").place(x=110, y=300)  # 90, 300
    Button(window1, text="DETECT FROM CAMERA ➡", command=camera_option, cursor="hand2",
           font=("Arial", 30), bg="light green", fg="blue").place(x=350, y=450)

    # function defined to exit from window1
    def exit_win1():
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            window1.destroy()

    # created exit button
    Button(window1, text="❌ EXIT", command=exit_win1,  cursor="hand2",
           font=("Arial", 25), bg="red", fg="blue").place(x=440, y=600)

    window1.protocol("WM_DELETE_WINDOW", exit_win1)
    window1.mainloop()
