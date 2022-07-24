# duoqin-mark
用于小米duoqin手机资源分享（基于python3.10）

### 1. 创建虚拟环境
***
假设项目放在用户根目录下，这里是C:\Users\admin  
```
PS C:\Users\admin\Desktop> cd ~/duoqin-mark
PS C:\Users\admin\duoqin-mark> python -m venv venv  
PS C:\Users\admin\duoqin-mark\venv\Scripts> cd venv/Scripts  
PS C:\Users\admin\duoqin-mark\venv\Scripts> ./activate  
(venv) PS C:\Users\admin\duoqin-mark\venv\Scripts>
```

### 2. 安装依赖
***
在项目目录下，用虚拟环境运行pip install -r requirements.txt  
```
(venv) PS C:\Users\admin\duoqin-mark\venv\Scripts> cd ~/duoqin-mark  
(venv) PS C:\Users\admin\duoqin-mark> pip install -r requirements.txt 
```

### 3. 启动服务
***
```
(venv) PS C:\Users\admin\duoqin-mark> hypercorn --bind "0.0.0.0:8000" main:app
```