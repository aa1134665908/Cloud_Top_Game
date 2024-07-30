import cv2
import numpy as np
import pyautogui
import time
import random
from PIL import ImageGrab
import keyboard
import threading

# 全局变量来控制程序运行状态
running = False
exit_program = False


def human_like_click(x, y, click_type='single'):
    pyautogui.moveTo(x + random.randint(-2, 2), y + random.randint(-2, 2), duration=0.1)
    pyautogui.mouseDown()
    time.sleep(0.05 + random.random() * 0.05)
    pyautogui.mouseUp()
    if click_type == 'double':
        time.sleep(0.1 + random.random() * 0.1)
        pyautogui.mouseDown()
        time.sleep(0.05 + random.random() * 0.05)
        pyautogui.mouseUp()


def find_and_click_multiple(template_paths, region=None, threshold=0.7, scales=[1.0, 0.9, 1.1], click_type='single'):
    if region:
        screenshot = np.array(pyautogui.screenshot(region=region))
    else:
        screenshot = np.array(pyautogui.screenshot())
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    results = []

    for template_path in template_paths:
        template = cv2.imread(template_path, 0)

        max_val = -np.inf
        max_loc = None
        max_scale = None

        for scale in scales:
            resized_template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
            w, h = resized_template.shape[::-1]

            res = cv2.matchTemplate(screenshot_gray, resized_template, cv2.TM_CCOEFF_NORMED)
            min_val, local_max_val, min_loc, local_max_loc = cv2.minMaxLoc(res)

            if local_max_val > max_val:
                max_val = local_max_val
                max_loc = local_max_loc
                max_scale = scale

        if max_val >= threshold:
            if region:
                click_x = region[0] + max_loc[0] + int(template.shape[1] * max_scale / 2)
                click_y = region[1] + max_loc[1] + int(template.shape[0] * max_scale / 2)
            else:
                click_x = max_loc[0] + int(template.shape[1] * max_scale / 2)
                click_y = max_loc[1] + int(template.shape[0] * max_scale / 2)

            human_like_click(click_x, click_y, click_type)

            results.append({
                'template': template_path,
                'position': (click_x, click_y),
                'confidence': max_val,
                'scale': max_scale
            })

            print(f"找到图像 {template_path} 并点击at ({click_x}, {click_y}), 匹配度: {max_val:.2f}, 缩放比例: {max_scale:.2f}")
        else:
            print(f"没有找到匹配的图像 {template_path}，最高匹配度: {max_val:.2f}")

    return results


def main_loop():
    global running, exit_program
    template_paths = [
        r'C:\Users\Administrator\Desktop\qianjue.jpg',
        r'C:\Users\Administrator\Desktop\naer.jpg',
        r'C:\Users\Administrator\Desktop\aoen.jpg',
        r'C:\Users\Administrator\Desktop\kaiying.jpg',
        r'C:\Users\Administrator\Desktop\erluoyi.jpg',
        r'C:\Users\Administrator\Desktop\sheng.jpg',
        r'C:\Users\Administrator\Desktop\yatuokesi.jpg',
        r'C:\Users\Administrator\Desktop\leikesai.jpg',
        # ... 可以添加更多图片路径
    ]

    # 获取屏幕尺寸
    screen_width, screen_height = pyautogui.size()
    # 设置扫描区域为屏幕下半部分
    region = (0, screen_height // 2, screen_width, screen_height)

    while not exit_program:
        if running:
            print("正在扫描...")
            results = find_and_click_multiple(template_paths, region=region, threshold=0.85,
                                              scales=[1.0], click_type='single')
            if results:
                print(f"找到 {len(results)} 个匹配的图像")
                for result in results:
                    print(
                        f"模板: {result['template']}, 位置: {result['position']}, 匹配度: {result['confidence']:.2f}, 缩放: {result['scale']:.2f}")
            else:
                print("没有找到任何匹配的图像")
        time.sleep(0.3)  # 每次扫描间隔1秒


def toggle_running():
    global running
    running = not running
    print("程序已" + ("启动" if running else "暂停"))


def exit_app():
    global exit_program
    exit_program = True
    print("程序正在退出...")


# 设置快捷键
keyboard.add_hotkey('ctrl+shift+s', toggle_running)  # Ctrl+Shift+S 开始/暂停
keyboard.add_hotkey('ctrl+shift+q', exit_app)  # Ctrl+Shift+Q 退出程序

# 启动主循环
print("程序已启动。按 Ctrl+Shift+S 开始/暂停扫描，按 Ctrl+Shift+Q 退出程序。")
main_thread = threading.Thread(target=main_loop)
main_thread.start()

# 保持程序运行
keyboard.wait('ctrl+shift+q')