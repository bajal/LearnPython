import pyautogui, time

def fillform():
	time.sleep(2)
	pyautogui.click(579,137)
	pyautogui.typewrite(['down', '\t', '\t'])
	time.sleep(.25)
	pyautogui.typewrite(['down','down', '\t'])

	pyautogui.typewrite(['down','down','down','\t'])

	pyautogui.typewrite(['down','down','down','down', '\t'])

	pyautogui.typewrite('Hello world!')
	pyautogui.typewrite(['enter'])
	pyautogui.typewrite('Hello world!')

	pyautogui.typewrite(['\t'])
	pyautogui.typewrite('Some random Reason', 0.15)


	find = pyautogui.locateOnScreen('btn.png')
	coord = pyautogui.center(find)
	pyautogui.click(coord)
	time.sleep(1)
	pyautogui.typewrite(['enter'])
	
def resetform():
	find = pyautogui.locateOnScreen('reset.png')
	coord = pyautogui.center(find)
	pyautogui.click(coord)
	time.sleep(1)	


fillform()
resetform()
fillform()	