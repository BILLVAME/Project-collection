# 目标检测常用的数据集
## PASCAL VOC
PASCAL VOC 2007：9963张图像，24640个标注
</br>
PASCAL VOC 2012：11530张图像，27450个标注
</br>

该数据集有20个分类：
* Person: person
* Animal: bird, cat, cow, dog, horse, sheep
* Vehicle: aeroplane, bicycle, boat, bus, car, motorbike, train
* Indoor: bottle, chair, dining table, potted plant, sofa, tv/monitor
</br>

链接：http://host.robots.ox.ac.uk/pascal/VOC/voc2012/


## MS COCO
COCO(Common Objects Context)数据集包含20万个图像：11.5万多张训练集图像，5千张脸验证集图像，2万多张测试集图像
</br>

80个类别中超过50万个目标标注
</br>

平均每个图像的目标数为7.2
</br>

链接：http://cocodataset.org/
</br>
</br>
</br>

# 目标检测性能指标
## 检测精度
* Precision, Recall, F1 score
* IoU (Intersection over Union)
* P-R curve (Precison-Recall curve)
* AP (Average Precision)
* mAP (mean Average Precision)

## 检测速度
* 前传耗时
* 每秒帧数FPS (Frames Per Second)
* 浮点运算量 (FLOPS)

## 混淆矩阵 (Confusion Matrix)
