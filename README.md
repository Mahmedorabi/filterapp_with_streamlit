# Filter Application
This application allows users to apply various filters to images using a web interface built with Streamlit. It supports filters like Black & White, Vignette, Pencil Sketch, HDR, Stylization, and Brightness adjustment.

## **Features**
- Black & White: Convert the image to grayscale.
- Vignette: Apply a vignette effect to the image with adjustable intensity.
- Pencil Sketch: Transform the image into a pencil sketch.
- HDR: Enhance the image details using HDR techniques.
- Stylization: Apply a stylized effect to the image.
- Brightness: Adjust the brightness of the image.

 ## **Usage**
1. **Run the Streamlit application:**
   ```python
        streamlit run filters.py
   ```
2. **Open your web browser and go to `http://localhost:8501.`**
3. **Upload an image file in JPG or PNG format.**
4. **Choose a filter from the dropdown menu.**
5. **Adjust the filter parameters if applicable.**
6. **View the original and filtered images side by side.**
## Code Overview
The main functions in the script are:

- `BlackWhite(img)`: Converts the input image to grayscale.
- `vignette(img, level)`: Applies a vignette effect to the input image. The intensity of the effect can be adjusted using the level parameter.
- `pencil_sketch(img, ksize)`: Converts the input image to a pencil sketch. The ksize parameter adjusts the kernel size for Gaussian blur.
- `HDR(img, sigma_s, sigma_r)`: Enhances the input image using HDR techniques. sigma_s and sigma_r are parameters for the detail enhancement.
- `stylization(img, sigma_s, sigma_r)`: Applies a stylized effect to the input image. sigma_s and sigma_r are parameters for the stylization.
- `Brightness(img, level)`: Adjusts the brightness of the input image. The level parameter controls the brightness adjustment.

  
The application uses Streamlit to create an interactive web interface, allowing users to upload images, select filters, and adjust filter parameters in real-time.

## Example
1. Upload an image:

2. Select a filter and adjust parameters:

3. View the original and filtered images:

## Dependencies
- OpenCV
- NumPy
- Streamlit


## Function Descriptions
1. **BlackWhite(img)**
  - Purpose: Converts the input image to grayscale.
  - Parameters:
     - img: The input image in BGR color space.
  - Returns: The grayscale version of the input image.
  - Example Usage:
    ```python

    gray_image = BlackWhite(img)
    ```
    ![Screenshot 2024-07-11 042251](https://github.com/Mahmedorabi/filterapp_with_streamlit/assets/105740465/1feb1567-4c73-4edb-88f7-7a87ae84372b)

2.**vignette(img, level)**

   - Purpose: Applies a vignette effect to the input image.
   - Parameters:
     - `img`: The input image in BGR color space.
     - `level`: The intensity level of the vignette effect. Higher values result in a more pronounced vignette.
   - Returns: The image with a vignette effect applied.
   - Example Usage:
      ```python
       vignette_image = vignette(img, level=2)
     ```

      ![Screenshot 2024-07-11 042454](https://github.com/Mahmedorabi/filterapp_with_streamlit/assets/105740465/b9845926-0f7e-4bb8-8739-5bf280f050d9)

3. **pencil_sketch(img, ksize=5)**
  - Purpose: Converts the input image to a pencil sketch.
  - Parameters:
    - img: The input image in BGR color space.
    - ksize: The kernel size for the Gaussian blur. Default is 5.
  - Returns: The pencil sketch version of the input image.
  - Example Usage:
    ``` python

    sketch_image = pencil_sketch(img, ksize=7)
    ```

    ![Screenshot 2024-07-11 042337](https://github.com/Mahmedorabi/filterapp_with_streamlit/assets/105740465/29c08951-9e7b-4dda-a1e3-d8173da17500)

4. **HDR(img, sigma_s=10, sigma_r=0.1)**

  - Purpose: Enhances the details of the input image using HDR techniques.
  - Parameters:
    - img: The input image in BGR color space.
    - sigma_s: Filter sigma in the color space. A larger value means that farther colors within the pixel neighborhood will be mixed together.
    - sigma_r: Filter sigma in the coordinate space. A larger value means that farther pixels will influence each other as long as their colors are similar enough.
  - Returns: The HDR-enhanced version of the input image.
  - Example Usage:
    ``` python
    hdr_image = HDR(img, sigma_s=12, sigma_r=0.2)
    ```
![Screenshot 2024-07-11 042350](https://github.com/Mahmedorabi/filterapp_with_streamlit/assets/105740465/e9c3e96b-568f-4948-9ab4-f1dcda8642a1)

4. **stylization(img, sigma_s=10, sigma_r=0.1)**

  - Purpose: Applies a stylized effect to the input image.
  - Parameters:
    - img: The input image in BGR color space.
    - sigma_s: Filter sigma in the color space.
    - sigma_r: Filter sigma in the coordinate space.
  - Returns: The stylized version of the input image.
  - Example Usage:
    ```python
    stylized_image = stylization(img, sigma_s=15, sigma_r=0.3)
    ```

    ![Screenshot 2024-07-11 042404](https://github.com/Mahmedorabi/filterapp_with_streamlit/assets/105740465/652e2821-969e-4ab3-95a9-25f48b3f534b)

6. **Brightness(img, level)**

  - Purpose: Adjusts the brightness of the input image.
  - Parameters:
    - img: The input image in BGR color space.
    - level: The level to adjust brightness. Positive values increase brightness, while negative values decrease it.
  - Returns: The image with adjusted brightness.
  - Example Usage:
    ```python
    brighter_image = Brightness(img, level=20)
    ```

    ![Screenshot 2024-07-11 042414](https://github.com/Mahmedorabi/filterapp_with_streamlit/assets/105740465/903b98e4-e6fe-4d0e-8239-8b3a168a2007)

## Code Workflow
1. **Streamlit Header:**
 - Sets up the main header of the application.
 ```python

st.header("Filter Application")
```
2. **File Upload:**

 - Allows users to upload an image file
 ```python

  upload = st.file_uploader("Choose an Image", ('jpg', 'png'))
```
3. **Image Processing:**
  - If an image is uploaded, it is decoded and displayed.
  - The user can select a filter from a dropdown menu and adjust its parameters.
  - The processed image is then displayed alongside the original image.
  ```python

if upload is not None:
    raw_bytes = np.asarray(bytearray(upload.read()), dtype=np.uint8)
    img = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

    input_col, output_col = st.columns(2)
    with input_col:
        st.header("Original Image")
        st.image(img, channels='BGR', use_column_width=True)

    st.header("Filter List")
    option = st.selectbox("Choose a filter", ["None", 'Black&White', 'vignette', 'pencil_sketch', 'HDR', 'stylization', 'Brightness'])

    if option == 'None':
        output = img
    elif option == 'Black&White':
        output = BlackWhite(img)
        color = 'GRAY'
    elif option == 'vignette':
        level = st.slider("level", 0, 10, 2, 2)
        output = vignette(img, level)
    elif option == 'pencil_sketch':
        ksize = st.slider("Ksize", 1, 11, 5, 2)
        output = pencil_sketch(img, ksize)
        color = 'GRAY'
    elif option == 'HDR':
        output = HDR(img)
    elif option == 'stylization':
        sigma = st.slider("Sigma", 1, 20, 5, 2)
        output = stylization(img, sigma)
    elif option == 'Brightness':
        level = st.slider("level", -50, 50, 0, 5)
        output = Brightness(img, level)
    else:
        pass

    with output_col:
        st.header("Output Image")
        st.image(output, channels=color)
   ```
  

