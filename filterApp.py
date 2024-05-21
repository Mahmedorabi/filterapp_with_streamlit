import streamlit as st 
import numpy as np 
import cv2

st.title("Filters Application")

def Black_white(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return gray

def vignette(img,level=2):
    hight,width=img.shape[:2]
    X_kernal=cv2.getGaussianKernel(hight,hight/level)
    y_kernal=cv2.getGaussianKernel(width,width/level)
    
    kernal=y_kernal*X_kernal.T 
    mask=kernal/kernal.max()
    img_vignette=np.copy(img)
    for i in range(3):
        img_vignette[:,:,i]=img_vignette[:,:,i]*mask
    return img_vignette

def pencil_sketch(img,ksize):
    blur=cv2.GaussianBlur(img,(ksize,ksize),0,0)
    sketch,_=cv2.pencilSketch(blur)
    return sketch

def HDR(img,sigma_s=10,sigma_r=0.1):
    blur=cv2.GaussianBlur(img,(5,5),0,0)
    HD_img=cv2.detailEnhance(blur,sigma_s=sigma_s,sigma_r=sigma_r)
    return HD_img

def stylization(img,sigma_s=10,sigma_r=0.1):
    blur=cv2.GaussianBlur(img,(5,5),0,0)
    style=cv2.stylization(blur,sigma_s=sigma_s,sigma_r=sigma_r)
    return style

def Brightness(img,level):
    bright=cv2.convertScaleAbs(img,beta=level)
    return bright

upload=st.file_uploader("Choose an Image",['jpg','png'])

if upload is not None:
    raw_byte=np.asarray(bytearray(upload.read()),dtype=np.uint8)
    img=cv2.imdecode(raw_byte,cv2.IMREAD_COLOR)
    
    input_col,output_col=st.columns(2)
    with input_col:
        st.header("Original Image")
        st.image(img,channels='BGR',use_column_width=True)
        
    st.header("Filter List")
    option=st.selectbox("Select Filter",("None","Black&White","vignette","pencil_sketch","HDR","stylization","Brightness"))
    
    
    output_flag=1
    color='BGR'
    if option=='None':
        output_flag=0
        output=img
    
    elif option=='Black&White':
        output=Black_white(img)    
        color='Gray'
    
    elif option=="vignette":
        level=st.slider("Level",2,10,2)
        output=vignette(img,level)
    
    elif option=="pencil_sketch":
        ksize=st.slider("Kernal",1,10,4)
        output=pencil_sketch(img,ksize)
        color='Gray'
    
    elif option=="HDR":
        output=HDR(img)
    
    elif option=="stylization":
        sigma_s=st.slider("level",0,200,10,step=10)
        output=stylization(img,sigma_s)
    
    elif option=="Brightness":
        level=st.slider("level",-50,50,0,step=5)
        output=Brightness(img,level)
    
    with output_col:
        st.header("Output Image")
        st.image(output,channels=color)

