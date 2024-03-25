import cv2
from ultralytics import YOLO
import numpy as np

# 打开视频文件
cap = cv2.VideoCapture("test2.mp4")

# 加载YOLO模型
model = YOLO("yolov5s.pt")

# 获取视频的帧率
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 获取视频的宽度和高度
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定义输出视频的编解码器和输出对象
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

# 初始化人物追踪字典和计数器
person_tracker = {}
person_counter = 0

# 循环读取视频帧
while True:
    # 读取视频帧
    ret, frame = cap.read()
    # 如果无法读取帧则退出循环
    if not ret:
        break

    # 使用YOLO模型检测视频帧中的物体，设备使用CPU
    results = model(frame, device="cpu")
    result = results[0]  # 获取检测结果
    # 获取检测到的边界框坐标和类别
    bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    classes = np.array(result.boxes.cls.cpu(), dtype="int")
    class_names = model.module.names if hasattr(model, 'module') else model.names
    # 遍历每个边界框和类别
    for cls, bbox in zip(classes, bboxes):
        (x, y, x2, y2) = bbox  # 获取边界框坐标
        # 获取类别名称
        class_name = class_names[cls]

        # 如果检测到的是人物
        if class_name == "person":
            # 查看是否有已经追踪的人物与当前框有重叠
            tracked_id = None
            for pid, (tx, ty, tx2, ty2) in person_tracker.items():
                if x >= tx and y >= ty and x2 <= tx2 and y2 <= ty2:
                    tracked_id = pid
                    break

            # 如果没有重叠的已追踪人物，分配一个新的标号
            if tracked_id is None:
                person_counter += 1
                tracked_id = person_counter
                person_tracker[tracked_id] = (x, y, x2, y2)

            # 在图像上绘制边界框和类别以及追踪标号
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 225), 2)  # 绘制边界框
            cv2.putText(frame, f"Person {tracked_id}", (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)  # 绘制类别文本

    # 将处理后的帧写入输出视频文件中
    out.write(frame)

    # 显示处理后的图像
    cv2.imshow("Img", frame)
    # 等待按键输入，按下ESC键退出循环
    key = cv2.waitKey(0)
    if key == 27:
        break

# 释放视频捕获对象并关闭所有窗口
cap.release()
out.release()
cv2.destroyAllWindows()
