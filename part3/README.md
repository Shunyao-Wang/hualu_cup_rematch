[TOC]



# Part3 : 字段识别 

代码等文件可在以下链接下载：

链接：https://pan.baidu.com/s/1yp-pEZONKWneAtsG-0MAcg 密码：v6vo

## 数据集说明：

主要使用了两个公开数据集：

* 中科院HWDB，用于手写汉字识别的模型模型训练。
* EMNIST，用于阿拉伯数字与英文大小写字母的模型训练。

## 功能说明：

接收`Part2:文字切割`部分的切割结果，输出初步识别后包含每份简历、每个字段的submit.csv，

## 格式说明：

* 输入文件格式：

  以`result/`命名的文件夹，下含以下子文件夹（字段）：

  * blood.jpg/            
  * graduate_name.jpg/  
  * high_school_degree.jpg/  
  * high_school_pass.jpg/  
  * junior_college_degree.jpg/  
  * junior_college_pass.jpg/  
  * sex.jpg/                   
  * undergraduate_name.jpg/  
  * weight.jpg/ 
  * graduate_degree.jpg/  
  * graduate_pass.jpg/  
  * high_school_major.jpg/   
  * high_school_time.jpg/  
  * junior_college_major.jpg/   
  * junior_college_time.jpg/  
  * undergraduate_degree.jpg/  
  * undergraduate_pass.jpg/
  * graduate_major.jpg/   
  * graduate_time.jpg/  
  * high_school_name.jpg/    
  * hometown.jpg/          
  * junior_college_name.jpg/    
  * nation.jpg/               
  * undergraduate_major.jpg/   
  * undergraduate_time.jpg/



## 代码文件功能说明：

* 0-1-filetree-transformation.ipynb：

  将`Part2:文字切割` 的输出文件夹`result/` 转化成 `Part3:字段识别` 所需要的格式。处理完成后，`result/` 文件夹转化为 `test/` 文件夹，下含以下子文件夹：

  - blood/            
  - graduate_name/  
  - high_school_degree/  
  - high_school_pass/  
  - junior_college_degree/  
  - junior_college_pass/  
  - sex/                   
  - undergraduate_name/  
  - weight/ 
  - graduate_degree/  
  - graduate_pass/  
  - high_school_major/   
  - high_school_time/  
  - junior_college_major/   
  - junior_college_time/  
  - undergraduate_degree/  
  - undergraduate_pass/
  - graduate_major/   
  - graduate_time/  
  - high_school_name/    
  - hometown/          
  - junior_college_name/    
  - nation/               
  - undergraduate_major/   
  - undergraduate_time/

* 0-2-extract_universities_name+subjects_name.ipynb：

  抽取出`全国高校名称字典` 与`一级二级学科名称字典` ，并序列化。

* 0-3-EMINST2images.ipynb：

  从以下四个文件 `emnist-byclass-test-images-idx3-ubyte` ，`emnist-byclass-test-labels-idx1-ubyte` ，`emnist-byclass-train-images-idx3-ubyte` ， `emnist-byclass-train-labels-idx1-ubyte` ，中，提取出EMNIST的trainset、validset。

* 0-4-EMNISTset_(padding+invert_blackwhite+adjust_constrast+sharpen).ipynb：

  对提取后的EMNIST数据集进行padding、黑白反转、对比度增强、锐化 等处理。

* 1-train-EMNIST-resnext50-unpretrained-dropout0.65.ipynb：

  EMNIST _dropout0.65 的模型训练，该模型用于识别数字与字母。

* 1-train-general-resnext50-unpretrained-usethis.ipynb：

  HDWB 的模型训练，该模型用于识别汉字。

* 2-test-EMNISTincluded.ipynb：

  inference阶段，输出submit.csv。

* 3-Corrections.ipynb

  对部分字段进行初步的校正。

* train-EMNIST-resnext50-unpretrained-dropout0.25_usethis.ipynb：

  EMNIST _dropout0.25 的模型训练，该模型用于识别数字与字母。

* train-EMNIST-resnext50-unpretrained-dropout0.35_usethis.ipynb：

  EMNIST _dropout0.35 的模型训练，该模型用于识别数字与字母。

* train-EMNIST-resnext50-unpretrained-dropout0.5_dropit.ipynb：

  无用模型

* train-EMNIST-resnext50-unpretrained-dropout0.8_dropit.ipynb

  无用模型

* train-resnext-dropout0.9_dropit.ipynb

  无用模型





## 运行说明

依次执行以上.ipynb。