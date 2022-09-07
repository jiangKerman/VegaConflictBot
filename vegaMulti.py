# Vega conflict的打怪脚本，打怪，
# 2022年8月22日
# 指定队伍，没有检测能否秒修，如果受损会消耗金币
# 需要pillow和opencv-python
import pyautogui
import time
import random
import sys

FIND = (1635, 95)  # 找到（标记的船）
ATTACK = (828, 1009)  # 攻击
REPAIR = (975, 931)  # 秒修
REPAIRBROKEN = (1111, 1014)  # 船爆了之后的修复
CLOSENOTARGET = (962, 669)  # 关闭找不到目标
CLOSESTRIKE = (1440, 188)  # 关闭闪击者
CLOSEALERT = (868, 670)  # 锁定高等级警报
RANDOMTIME = [0.5, 0.1]  # 设置每次点击后暂停几秒
CLOSEUNDERATTACK = (1057, 663)  # 关闭“舰队遭到攻击"
huhang = (941, 668)  # 关闭“只能护送自己的舰队” and 关闭“组团舰队异常危险”，这两个是同一个注意和关闭坐标
CLOSE = (1436, 186)  # 关闭战利品、闪击者这类大窗口

# 用于找船
BookMarks = (1724, 38)  # 屏幕右上角的标签
Marked = (699, 257)  # 已经标记的
Mark1 = (530, 307)
Mark2 = (594, 364)
Mark3 = (523, 419)
Mark4 = (605, 470)
Mark5 = (614, 523)
Mark6 = (591, 573)
Mark7 = (585, 636)

SHIPARRAY = [1, 2, 3, 4, 5, 6, 7]  # 哪几个队伍要刷怪
# SHIPARRAY = [1]  # 哪几个队伍要刷怪
MONSTERARRAY = [Mark1, Mark2, Mark3, Mark4, Mark1, Mark2, Mark3]  # 对应SHIPARRAY要刷的怪物
# MONSTERARRAY = [Mark1,Mark2 ]  # 对应SHIPARRAY要刷的怪物
# SHIPARRAY = ["2", ]

print("2秒后开始脚本--多队伍刷图")
time.sleep(2)


def closeStrike():
    """
    关闭闪击者
    :return:
    """
    if pyautogui.locateOnScreen("img/strike.png", grayscale=True, confidence=0.95) is not None:
        pyautogui.click(CLOSESTRIKE)
        time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))


while (True):
    print("开始新一轮")
    time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
    for (i, j) in zip(SHIPARRAY, MONSTERARRAY):
        # 关闭找不到目标弹窗
        if pyautogui.locateOnScreen("img/noTarget.png", grayscale=True, confidence=0.95) is not None:
            pyautogui.click(CLOSENOTARGET)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭闪击者
        if pyautogui.locateOnScreen("img/strike.png", grayscale=True, confidence=0.95) is not None:
            pyautogui.click(CLOSESTRIKE)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭舰队遭到攻击
        if pyautogui.locateOnScreen("img/underattack.png", grayscale=True, confidence=0.95) is not None:
            pyautogui.click(CLOSEUNDERATTACK)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭“只能护送自己的舰队”
        if pyautogui.locateOnScreen("img/huhang.png", grayscale=True, confidence=0.95) is not None:
            pyautogui.click(huhang)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭高等级警报
        if pyautogui.locateOnScreen("img/alert.png", grayscale=True, confidence=0.8) is not None:
            pyautogui.click(CLOSEALERT)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭战利品
        if pyautogui.locateOnScreen("img/spoils.png", grayscale=True, confidence=0.8) is not None:
            pyautogui.click(CLOSE)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))

        # 选中船编号（先切换到其他舰队，确保能选中）
        pyautogui.press(str(i % 7 + 1))  # 先按一下当前舰队的前一个舰队
        time.sleep(0.3)
        pyautogui.press(str(i))
        time.sleep(1.5)  # 选中1后等一秒等修船信息跳出来
        # 如果该船正在战斗，则进入下一个船
        if pyautogui.locateOnScreen("img/join.png", grayscale=True, confidence=0.9) is not None:
            continue
        # 如果可以免费修则修船
        if pyautogui.locateOnScreen("img/repair.png", grayscale=True, confidence=0.9) is not None:
            closeStrike()
            pyautogui.click(REPAIR)
            time.sleep(1.5)
        # 如果船已经爆了就在船厂点修复，然后退出程序
        # if pyautogui.locateOnScreen("img/brokenRepair.png", grayscale=True, confidence=0.90) is not None:
        #     pyautogui.click(REPAIRBROKEN)
        #     sys.exit(0)

        # 点击找到
        closeStrike()
        pyautogui.click(BookMarks)
        time.sleep(0.3)
        pyautogui.click(Marked)
        time.sleep(0.3)
        pyautogui.click(j)
        # 一直等待直到星区切换结束
        while (True):
            time.sleep(0.3)
            if pyautogui.locateOnScreen("img/loading.png", grayscale=True, confidence=0.95) is None:
                time.sleep(0.3)
                break

        # 如果要切换星区地图，则多等待几秒
        # if (i == 1 or i == 3 or i == 5 or i == 7):
        #     time.sleep(6)
        # else:
        #     time.sleep(0.3)

        # 点击攻击,攻击之前需要判定是否真的是攻击（有可能这一秒已经变成了加入或者查看[怪被抢了]）,如果不是攻击，则回到起点
        if pyautogui.locateOnScreen("img/attack.png", grayscale=True, confidence=0.95) is None:
            continue
        closeStrike()
        pyautogui.click(ATTACK)
        time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 如果有则点击（高等级警报）确认
        if pyautogui.locateOnScreen("img/alert.png", grayscale=True, confidence=0.8) is not None:
            closeStrike()
            pyautogui.click(CLOSEALERT)
        time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 如果有则点击（组队舰队异常危险）确认
        if pyautogui.locateOnScreen("img/huhang.png", grayscale=True, confidence=0.8) is not None:
            closeStrike()
            pyautogui.click(huhang)
        time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))


        # 等待20秒后开始下一辆船
        print(f"队伍{i}指令下达")
        time.sleep(1.5)

    print("一轮结束")
    # time.sleep(4)
