2020年，来自印度海德拉巴大学和英国巴斯大学的团队，在ACM MM2020发表了的一篇论文《A Lip Sync Expert Is All You Need for Speech to Lip Generation In The Wild 》，在文章中，他们提出一个叫做Wav2Lip的AI模型，只需要一段人物视频和一段目标语音，就能够让音频和视频合二为一，人物嘴型与音频完全匹配。

https://bhaasha.iiit.ac.in/lipsync/  这个网站，Wav2Lip，有时间可以玩玩





---

教程(https://www.bilibili.com/video/BV1ZG4y1Z7Ed/?spm_id_from=333.337.search-card.all.click&vd_source=684fbeefd6e908cc5946b9e46ff75133)

食用方法：

- 下载，github链接：https://github.com/Rudrabha/Wav2Lip

- 配置环境，获取模型

  - ffmpeg（*FFmpeg*是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序，下载方式 https://www.cnblogs.com/chadlas/p/15911072.html）

  - ```python
    #python环境，我的3.7.6
    librosa==0.7.0
    numpy==1.17.1
    opencv-contrib-python>=4.2.0.34
    opencv-python==4.1.0.25
    torch==1.1.0 #1.7.0  
    #pip install torch==1.7.0 torchvision==0.8.1 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    #(https://blog.csdn.net/qq_27093891/article/details/123694741)
    
    torchvision==0.3.0  #0.8.0
    tqdm==4.45.0
    numba==0.48
    ```
    
  - 下载模型文件

    ```xml
    	Model	              					Description	                     
    Wav2Lip							Highly accurate lip-sync					415MB（可直接食用）
    Wav2Lip + GAN					Slightly inferior lip-sync, but better visual quality	 416MB（可用）
    Expert Discriminator			Weights of the expert discriminator	            188MB(需要搭配文件食用)
    Visual Quality Discriminator	Weights of the visual disc trained in a GAN setup	 161MB（需配文件）
    ```

    

  - 报错

    ```python
    #AttributeError: partially initialized module ‘cv2‘ has no attribute ‘gapi_wip_gst_GStreamerPipeli
    #底层调用了其他模块，却没有安装依赖的模块所以报错了
    pip install opencv-python install "opencv-python-headless<4.3
    ```

    

  - 装CUDA（https://www.bilibili.com/video/BV1nL4y1b7oT/?spm_id_from=333.337.search-card.all.click&vd_source=684fbeefd6e908cc5946b9e46ff75133）

    

    

- 运行

  - ```python
    python inference.py --checkpoint_path checkpoints/wav2lip.pth --face data/zhuangzhongxu.jpg --audio data/boy.mp3
    ```



---

