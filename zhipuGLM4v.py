from zhipuai import ZhipuAI
import os
import base64
import json
from io import BytesIO


p = os.path.dirname(os.path.realpath(__file__))
#get path
#获取项目地址

def get_ZhipuAI_api_key():
    try:
        config_path = os.path.join(p, 'config.json')#合并KEY的地址
        with open(config_path, 'r') as f:  
            config = json.load(f)
        api_key = config["ZHIPUAI_API_KEY"]
    except:
        print("出错啦 Error: API key is required")
        return ""
    return api_key



class GLM4_Vsion_IMGURL:

    def __init__(self):
        pass
        
    #配置参数
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "先理解这个图片上面的内容，然后生成描绘主体对象的[[英文]]短语，语言是english。生成规范是，记住你需要描绘我提供给你的图片细节尽可能的多，角度尽可能更加丰富，多写[逗号‘，']相连接的英文短语,切记一定需要在生成的prompt文本当中中添加下面这堆prompt，[[best quality, high resolution, 4k, high quality]]，描绘人称都用第三人称", "multiline": True}),
                "image_url": ("STRING", {"default": "https://pic1.zhimg.com/v2-5f79c0d9466907a2227200620140835c_r.jpg"}),
                "model_name": (["glm-4v"],),#选用什么模型
                "api_key":  ("STRING", {  #输入gpt4v的KEY，
                    #get OpenAI API Key
                    "multiline": False,
                    "default": get_ZhipuAI_api_key()
                
                }),    
            }
        }
    
    #配置
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("GETPrompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "BlinkNodes_PROMPT"


    def generate_prompt(self, api_key,image_url,prompt,model_name):
        
        self.api_key = api_key

        if image_url == None:
            raise ValueError("GLM needs image")
        if prompt is None:
            raise ValueError("Prompt is required") 
        
        #判断是否正常传入image和prompt，如果没有的话马上中断
        #Determine if image and prompt are being passed in properly, if not break immediately

        client = ZhipuAI(api_key=api_key) # 填写APIKey Fill in APIKey
        response = client.chat.completions.create(
        model=model_name,  # 选择需要调用的模型名称  Select model 
        messages=[
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": prompt
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url
                }
            }
                        ]
        }
            ]
                )
        response = str(response.choices[0].message.content)
        return (response,) #传出一定要是列表，这个逗号不能省略
    



class GLM4_CHAT:

    def __init__(self):
        pass
        
    #配置参数
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "你好，你是谁呀", "multiline": True}),
                "model_name": (["glm-4"],),#选用什么模型
                "api_key":  ("STRING", {  #输入gpt4v的KEY，Add api_key as an input
                    #get OpenAI API Key
                    "multiline": False,
                    "default": get_ZhipuAI_api_key()
                
                }),    
            }
        }

    
    #配置
    #config
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "generate_prompt"
    CATEGORY = "BlinkNodes_PROMPT"


    def generate_prompt(self, api_key,prompt,model_name):
        
        self.api_key = api_key

        if prompt is None:
            raise ValueError("Prompt is required") 
        #判断是否正常传入image和prompt，如果没有的话马上中断
        #Determine if image and prompt are being passed in properly, if not break immediately

        client = ZhipuAI(api_key=api_key)           # 填写APIKey Fill in APIKey
        response = client.chat.completions.create(
        model=model_name,                           # 选择需要调用的模型名称  Select model 
        messages=[
            {"role": "user", "content": "你好"},
            {"role": "assistant", "content": "我是人工智能助手"},
            {"role": "user", "content": "你叫什么名字"},
            {"role": "assistant", "content": "我叫chatGLM"},
            {"role": "user", "content": prompt}
        ],
        )
        response = str(response.choices[0].message.content)
        return (response,) #传出一定要是列表，这个逗号不能省略



class GLM3_turbo_CHAT:

    def __init__(self):
        pass
        
    #配置参数
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "你好，你是谁呀", "multiline": True}),
                "model_name": (["glm-3-turbo"],),#选用什么模型
                "api_key":  ("STRING", {  #输入gpt4v的KEY，Add api_key as an input
                    #get OpenAI API Key
                    "multiline": False,
                    "default": get_ZhipuAI_api_key()
                
                }),    
            }
        }

    
    #配置
    #config
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "generate_prompt"
    CATEGORY = "BlinkNodes_PROMPT"


    def generate_prompt(self, api_key,prompt,model_name):
        
        self.api_key = api_key

        if prompt is None:
            raise ValueError("Prompt is required") 
        #判断是否正常传入image和prompt，如果没有的话马上中断
        #Determine if image and prompt are being passed in properly, if not break immediately

        client = ZhipuAI(api_key=api_key)           # 填写APIKey Fill in APIKey
        response = client.chat.completions.create(
        model=model_name,                           # 选择需要调用的模型名称  Select model 
        messages=[
            {"role": "user", "content": "你好"},
            {"role": "assistant", "content": "我是人工智能助手"},
            {"role": "user", "content": "你叫什么名字"},
            {"role": "assistant", "content": "我叫chatGLM"},
            {"role": "user", "content": prompt}
        ],
        )
        response = str(response.choices[0].message.content)
        return (response,) #传出一定要是列表，这个逗号不能省略

