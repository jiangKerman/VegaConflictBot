import pygetwindow as gw
import time

windows = gw.getWindowsWithTitle("Vega Conflict")
window = windows[0]

# window.resizeTo(200,200)
# time.sleep(1)
window.moveTo(100, 100)

print(window)

# import ctypes
#
# def set_window_no_border(window_handle):
#     GWL_STYLE = -16
#     WS_BORDER = 0x00800000
#     WS_DLGFRAME = 0x00400000
#     WS_CAPTION = 0x00C00000
#     WS_SYSMENU = 0x00080000
#
#     style = ctypes.windll.user32.GetWindowLongPtrW(window_handle, GWL_STYLE)
#     style = style & ~WS_BORDER & ~WS_DLGFRAME & ~WS_CAPTION & ~WS_SYSMENU
#     ctypes.windll.user32.SetWindowLongPtrW(window_handle, GWL_STYLE, style)
#     ctypes.windll.user32.SetWindowPos(window_handle, 0, 0, 0, 0, 0, 0x0002 | 0x0004 | 0x0040)
#
# # 替换为您想要设置为无边框窗口的窗口标题
# window_title = "Vega Conflict"
#
# window = gw.getWindowsWithTitle(window_title)[0]
# window_handle = window._hWnd
#
# set_window_no_border(window_handle)
