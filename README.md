# ComfyUI_GLM4Node
Recent：I have successfully load the vision understanding fuction of the GLM4 in COMFYUI. Anyuser could use their own API-KEY to use this fuction
GLM4_vision_node √
GLM4_node        √
GLM3_trubo_node  ×

## FUCTION
### GLM4 Vision Integration
GLM Vision is now integrated into this project. Due to the slow transmission rate of base64 in GLM4, we temporarily support uploading via URL.
The function of this feature is to allow users to upload images for processing via a URL, then user could use this function to chat with GLM4 agent. This enhances the user experience and processing speed.

#### Usage
To use GLM4 Vision, follow the steps below:

Upload your image to a public URL. This can be done via different online hosting platforms. Ensure the image is accessible publicly.
Use the provided function to upload the image URL.
Upload your API key to the node. It’s very important to make sure that your API key is working properly.

#### example of usage

pip install zhipuai

Please be careful when handling your API key to prevent misuse. We are still working to make the process more secure and efficient.

Caution!
This method is in its beta phase. If you find any bug or have any suggestions, feel free to open an issue or a pull request.
my email address is jcandzero@163.com 
