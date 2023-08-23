import pyautogui
import time
import random
import sys

# SHIPARRAY = [1, 2, 3, 4, 5, 6, 7]  # 哪几个队伍要刷怪
# MONSTERARRAY = [1, 2, 1, 1, 2, 2, 1]  # 对应SHIPARRAY要刷的怪物


SHIPARRAY = input("出动的舰队:")
SHIPARRAY = SHIPARRAY.split(" ")
SHIPARRAY = [int(i) for i in SHIPARRAY]

MONSTERARRAY = input("对应的目标:")
MONSTERARRAY = MONSTERARRAY.split(" ")
MONSTERARRAY = [int(i) for i in MONSTERARRAY]

# 各项找图的范围
alertRegion = (616, 348, 1298, 730)  # 攻击高等级
strikeRegion = (1122, 296, 1306, 361)  # 关闭闪击者
repairRegion = (842, 894, 1084, 964)  # 每一回合后的维修
finalRepairRegion = (1039, 965, 1167, 1067)  # 船爆之后的维修
noTargetRegion = (646, 366, 1283, 726)  # 无目标
huhangRegion = (826, 351, 1123, 472)  # 只能护送自己的舰队
spoilsRegion = (831, 128, 1083, 230)  # 关闭战利品
underAttackRegion = (766, 360, 1132, 465)  # 关闭舰队遭到攻击
joinRegion = (746, 963, 876, 1064)  # 底部的加入
loadingRegion = (679, 287, 1190, 749)  # 切换星区加载界面
# 鼠标点击的坐标
FIND = (1635, 95)  # 找到（标记的船）
ATTACK = (828, 1009)  # 攻击
REPAIR = (975, 931)  # 秒修
REPAIRBROKEN = (1111, 1014)  # 船爆了之后的修复
CLOSENOTARGET = (962, 669)  # 关闭找不到目标
CLOSESTRIKE = (1440, 188)  # 关闭闪击者
CLOSEALERT = (868, 670)  # 锁定高等级警报
RANDOMTIME = [0.15, 0.2]  # 设置每次点击后暂停几秒
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

shipMonsterDict = dict(zip([1, 2, 3, 4, 5, 6, 7], [Mark1, Mark2, Mark3, Mark4, Mark5, Mark6, Mark7]))

print("2秒后开始脚本--多队伍刷图")
time.sleep(2)


def closeStrike():
    """
    关闭闪击者
    :return:
    """
    if pyautogui.locateOnScreen("img/strike.png", grayscale=True, confidence=0.95, region=strikeRegion) is not None:
        pyautogui.click(CLOSESTRIKE)
        time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))


while True:
    print("开始新一轮")
    for (i, j) in zip(SHIPARRAY, MONSTERARRAY):
        # 关闭找不到目标弹窗
        if pyautogui.locateOnScreen("img/noTarget.png", grayscale=True, confidence=0.95,
                                    region=noTargetRegion) is not None:
            pyautogui.click(CLOSENOTARGET)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭闪击者
        if pyautogui.locateOnScreen("img/strike.png", grayscale=True, confidence=0.95, region=strikeRegion) is not None:
            pyautogui.click(CLOSESTRIKE)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭舰队遭到攻击
        if pyautogui.locateOnScreen("img/underattack.png", grayscale=True, confidence=0.95,
                                    region=underAttackRegion) is not None:
            pyautogui.click(CLOSEUNDERATTACK)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭“只能护送自己的舰队”
        if pyautogui.locateOnScreen("img/huhang.png", grayscale=True, confidence=0.95, region=huhangRegion) is not None:
            pyautogui.click(huhang)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭高等级警报
        if pyautogui.locateOnScreen("img/alert.png", grayscale=True, confidence=0.8, region=alertRegion) is not None:
            pyautogui.click(CLOSEALERT)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 关闭战利品
        if pyautogui.locateOnScreen("img/spoils.png", grayscale=True, confidence=0.8, region=spoilsRegion) is not None:
            pyautogui.click(CLOSE)
            time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))

        # 选中船编号（先切换到其他舰队，确保能选中）
        pyautogui.press(str(i % 7 + 1))  # 先按一下当前舰队的前一个舰队
        time.sleep(0.1)
        pyautogui.press(str(i))
        time.sleep(1)  # 选中1后等一秒等修船信息跳出来
        # 如果该船正在战斗，则进入下一个船
        if pyautogui.locateOnScreen("img/join.png", grayscale=True, confidence=0.9, region=joinRegion) is not None:
            continue
        # 如果可以免费修则修船
        if pyautogui.locateOnScreen("img/repair.png", grayscale=True, confidence=0.9, region=repairRegion) is not None:
            closeStrike()
            pyautogui.click(REPAIR)
            time.sleep(1)
        # 如果船已经爆了就在船厂点修复，然后退出程序
        # if pyautogui.locateOnScreen("img/brokenRepair.png", grayscale=True, confidence=0.90,
        #                             region=finalRepairRegion) is not None:
        #     pyautogui.click(REPAIRBROKEN)
        #     sys.exit(0)

        # 点击找到
        closeStrike()
        pyautogui.click(BookMarks)
        time.sleep(0.1)
        pyautogui.click(Marked)
        time.sleep(0.1)
        pyautogui.click(shipMonsterDict.get(j))
        time.sleep(0.3)

        # # 一直等待直到星区切换结束
        while (True):
            if pyautogui.locateOnScreen("img/loading.png", grayscale=True, confidence=0.95,
                                        region=loadingRegion) is None:
                time.sleep(0.5)
                break

        # 如果要切换星区地图，则多等待几秒
        # if (i == 1 or i == 3 or i == 5 or i == 7):
        #     time.sleep(6)
        # else:
        #     time.sleep(0.3)

        # 点击攻击,攻击之前需要判定是否真的是攻击（有可能这一秒已经变成了加入或者查看[怪被抢了]）,如果不是攻击，则回到起点
        if pyautogui.locateOnScreen("img/attack.png", grayscale=True, confidence=0.95, region=joinRegion) is None:
            continue
        closeStrike()
        pyautogui.click(ATTACK)
        time.sleep(0.1)
        # 如果有则点击（高等级警报）确认
        if pyautogui.locateOnScreen("img/alert.png", grayscale=True, confidence=0.8, region=alertRegion) is not None:
            closeStrike()
            pyautogui.click(CLOSEALERT)
        time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))
        # 如果有则点击（组队舰队异常危险）确认
        if pyautogui.locateOnScreen("img/huhang.png", grayscale=True, confidence=0.8, region=huhangRegion) is not None:
            closeStrike()
            pyautogui.click(huhang)
        time.sleep(random.uniform(RANDOMTIME[0], RANDOMTIME[1]))

        # 等待20秒后开始下一辆船
        print(f"队伍{i}指令下达")
        time.sleep(1)

    print("一轮结束")
    # time.sleep(4)
