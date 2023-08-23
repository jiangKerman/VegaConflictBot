# 针对服务器做1024*

import pyautogui
import time
import sys
import os

# SHIPARRAY = [1, 2, 3, 4, 5, 6, 7]  # 哪几个队伍要刷怪
# MONSTERARRAY = [1, 2, 1, 1, 2, 2, 1]  # 对应SHIPARRAY要刷的怪物

size = pyautogui.size()
if size.width == 1024 and size.height == 768:
    print(f"resolving: {size.width} X {size.height} ")
else:
    print(f"please change resolving to 1024*768")
    time.sleep(2)
    sys.exit()

SHIPARRAY = input("shipArray:")
SHIPARRAY = SHIPARRAY.split(" ")
SHIPARRAY = [int(i) for i in SHIPARRAY]

MONSTERARRAY = input("targetArray:")
MONSTERARRAY = MONSTERARRAY.split(" ")
MONSTERARRAY = [int(i) for i in MONSTERARRAY]

# 各项找图的范围


sleepTime = 0.5  # 每次点击后暂停0.4秒
interrupted = False  # 标记是否被闪击者打断过，打断过则本轮重来

alertRegion = (452, 222, 551, 283)  # 攻击高等级 done
strikeRegion = (955, 13, 1021, 58)  # 关闭闪击者 done
repairRegion = (396, 601, 618, 665)  # 每一回合后的维修 done
finalRepairRegion = (595, 677, 715, 762)  # 船爆之后的维修 done
noTargetRegion = (646, 366, 1283, 726)  # 无目标
huhangRegion = (826, 351, 1123, 472)  # 只能护送自己的舰队
spoilsRegion = strikeRegion  # 关闭战利品
underAttackRegion = (342, 219, 640, 294)  # 关闭舰队遭到攻击    done
joinRegion = (305, 672, 427, 763)  # 底部的加入  done
loadingRegion = (679, 287, 1190, 749)  # 切换星区加载界面
reconnectRegion = (414, 484, 609, 540)  # 短线重连点ok
reconnectAcceptRegion = (553, 453, 638, 510)  # 断线重连点偏右面的接收
# 鼠标点击的坐标
FIND = (741, 97)  # 找到（标记的船）    done
ATTACK = (371, 719)  # 攻击   done
REPAIR = (520, 634)  # 秒修   done
REPAIRBROKEN = (661, 719)  # 船爆了之后的修复   done
CLOSENOTARGET = (495, 512)  # 关闭找不到目标      done  找不到目标和高等级一样
CLOSESTRIKE = (992, 38)  # 关闭闪击者        done 大类窗口叉叉都一样
CLOSEALERT = CLOSENOTARGET  # 锁定高等级警报   done 和找不到目标一样
RANDOMTIME = [0.15, 0.2]  # 设置每次点击后暂停几秒

ReconnectAccept = (594, 485)  # 点击请检查您的网络连接
CLOSEUNDERATTACK = (554, 508)  # 关闭“舰队遭到攻击"     done
huhang = CLOSENOTARGET  # 关闭“只能护送自己的舰队” and 关闭“组团舰队异常危险”，这两个是同一个注意和关闭坐标    done
CLOSE = CLOSESTRIKE  # 关闭战利品、闪击者这类大窗口

# 用于找船
BookMarks = (825, 40)  # 屏幕右上角的标签   done
Marked = (246, 101)  # 已经标记的       done
Mark1 = (110, 154)  # done
Mark2 = (110, 198)  # done
Mark3 = (110, 259)  # done
Mark4 = (110, 315)  # done
Mark5 = (110, 368)  # done
Mark6 = (110, 433)  # done
Mark7 = (110, 480)  # done
# --各项找图的范围

shipMonsterDict = dict(zip([1, 2, 3, 4, 5, 6, 7], [Mark1, Mark2, Mark3, Mark4, Mark5, Mark6, Mark7]))


def closeStrike():
    """
    关闭闪击者
    :return:
    """
    while pyautogui.locateOnScreen("img1024_768/strike.png", grayscale=True, confidence=0.95,
                                   region=strikeRegion) is not None:
        pyautogui.click(CLOSESTRIKE)
        interrupted = True
        time.sleep(sleepTime)


def closeUnderAttack():
    """
    关闭舰队遭到攻击
    :return:
    """
    # 关闭舰队遭到攻击
    if pyautogui.locateOnScreen("img1024_768/underattack.png", grayscale=True, confidence=0.95,
                                region=underAttackRegion) is not None:
        pyautogui.click(CLOSEUNDERATTACK)
        time.sleep(sleepTime)


print("start in 2s")
time.sleep(2)
while True:
    print("start new epoch")
    for (i, j) in zip(SHIPARRAY, MONSTERARRAY):
        while True:  # do while，只有不被打断才进行下一个
            # 打怪之前先判断断线重连，点击中间的ok
            if pyautogui.locateOnScreen("img1024_768/reconnect_ok.png", grayscale=True, confidence=0.90,
                                        region=reconnectRegion) is not None:
                pyautogui.click(huhang)
                time.sleep(sleepTime)
            # 打怪之前先判断断线重连，偏右边的接收
            if pyautogui.locateOnScreen("img1024_768/reconnectAccept.png", grayscale=True, confidence=0.90,
                                        region=reconnectAcceptRegion) is not None:
                pyautogui.click(ReconnectAccept)
                time.sleep(sleepTime)

            interrupted = False  # 标记是否被闪击者打断过，打断过则本轮重来
            # 关闭找不到目标弹窗
            if pyautogui.locateOnScreen("img1024_768/noTarget.png", grayscale=True, confidence=0.95,
                                        region=noTargetRegion) is not None:
                pyautogui.click(CLOSENOTARGET)
                time.sleep(sleepTime)
            # 关闭“只能护送自己的舰队”
            if pyautogui.locateOnScreen("img1024_768/huhang.png", grayscale=True, confidence=0.95,
                                        region=huhangRegion) is not None:
                pyautogui.click(huhang)
                time.sleep(sleepTime)
            # 关闭高等级警报
            if pyautogui.locateOnScreen("img1024_768/alert.png", grayscale=True, confidence=0.8,
                                        region=alertRegion) is not None:
                pyautogui.click(CLOSEALERT)
                time.sleep(sleepTime)
            closeUnderAttack()
            closeStrike()
            # 选中船编号（先切换到其他舰队，确保能选中）
            pyautogui.press(str(i % 7 + 1))  # 先按一下当前舰队的前一个舰队
            time.sleep(0.1)
            pyautogui.press(str(i))
            time.sleep(1)  # 选中1后等一秒等修船信息跳出来
            # 如果该船正在战斗，则进入下一个船
            if pyautogui.locateOnScreen("img1024_768/join.png", grayscale=True, confidence=0.9,
                                        region=joinRegion) is not None:
                print(f"ship {i} attacking")
                break
            # 如果可以免费修则修船
            if pyautogui.locateOnScreen("img1024_768/repair.png", grayscale=True, confidence=0.9,
                                        region=repairRegion) is not None:
                closeStrike()
                closeUnderAttack()
                pyautogui.click(REPAIR)
                time.sleep(1)
            # 如果船已经爆了就在船厂点修复，然后退出程序
            if pyautogui.locateOnScreen("img1024_768/brokenRepair.png", grayscale=True, confidence=0.90,
                                        region=finalRepairRegion) is not None:
                pyautogui.click(REPAIRBROKEN)
                print("repair")
                # os.system("shutdown -s -t 60")
                # sys.exit(0)

            # 点击找到,点书签还是直接找到（键入0）
            if j == 0:
                pyautogui.click(FIND)
            else:
                closeStrike()
                closeUnderAttack()
                pyautogui.click(BookMarks)
                time.sleep(0.1)
                pyautogui.click(Marked)
                time.sleep(0.1)
                pyautogui.click(shipMonsterDict.get(j))
                time.sleep(0.3)

            # # 一直等待直到星区切换结束
            while True:
                if pyautogui.locateOnScreen("img1024_768/loading.png", grayscale=True, confidence=0.95,
                                            region=loadingRegion) is None:
                    time.sleep(0.5)
                    break

            # 如果要切换星区地图，则多等待几秒
            # if (i == 1 or i == 3 or i == 5 or i == 7):
            #     time.sleep(6)
            # else:
            #     time.sleep(0.3)

            # 点击攻击,攻击之前需要判定是否真的是攻击（有可能这一秒已经变成了加入或者查看[怪被抢了]）,如果不是攻击，则回到起点
            if pyautogui.locateOnScreen("img1024_768/attack.png", grayscale=True, confidence=0.95,
                                        region=joinRegion) is None:
                continue
            closeStrike()
            closeUnderAttack()
            pyautogui.click(ATTACK)
            time.sleep(0.1)
            # 如果有则点击（高等级警报）确认
            if pyautogui.locateOnScreen("img1024_768/alert.png", grayscale=True, confidence=0.8,
                                        region=alertRegion) is not None:
                closeStrike()
                closeUnderAttack()
                pyautogui.click(CLOSEALERT)
            time.sleep(sleepTime)
            # 如果有则点击（组队舰队异常危险）确认
            if pyautogui.locateOnScreen("img1024_768/huhang.png", grayscale=True, confidence=0.8,
                                        region=huhangRegion) is not None:
                closeStrike()
                closeUnderAttack()
                pyautogui.click(huhang)
            time.sleep(sleepTime)

            # 等待20秒后开始下一辆船
            print(f"ship {i} command send")
            time.sleep(1)
            if not interrupted:
                break

print("end one epoch")
# time.sleep(4)
