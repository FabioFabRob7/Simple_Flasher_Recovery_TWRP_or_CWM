import subprocess
import webbrowser

print("///////////////////////////////////////////////\n/     Simple_Flasher_Recovery_TWRP_or_CWM     /\n/               By_FabioFabRob7               /\n///////////////////////////////////////////////\n")
print("---------------------------------------------------------------------------------------\n-I am not responsible for any problems with your smartphone so proceed with caution!!!-\n---------------------------------------------------------------------------------------\n")

print("First of all unlock the bootloader with my app (only official guided methods)")
webbrowser.open("https://github.com/FabioFabRob7/Android_Unlocker")
input("When you're done unlocking via my app hit enter. . .")
def OS():
    OS_select = input("Select your PC OS:\n1) Windows\n2) Linux\n")
    if OS_select == "1":
        print("The phone will restart in bootloader mode")
        subprocess.call(["adb.exe", "reboot", "bootloader"])
        input("Official webpage for TWRP download, REMEMBER TO SELECT YOUR DEVICE OR YOU WILL DAMAGE IT. Press enter when you have the recovery img. . .")
        webbrowser.open("https://twrp.me/Devices/")
        dir_recovery = input("Enter the directory of the .img file TWRP or CWM (REMEMBER THAT THE RECOVERY MUST BE OF YOUR SMARTPHONE MODEL, remember to write the name of recovery.img as well as the directory)")
        subprocess.call(["fastboot.exe", "flash", "recovery", dir_recovery])
        subprocess.call(["fastboot.exe", "reboot"])
    elif OS_select == "2":
        ADB_FB_L()
        print("The phone will restart in bootloader mode")
        subprocess.call(["adb", "reboot", "bootloader"])
        input("Official webpage for TWRP download, REMEMBER TO SELECT YOUR DEVICE OR YOU WILL DAMAGE IT. Press enter when you have the recovery img. . .")
        webbrowser.open("https://twrp.me/Devices/")
        dir_recovery = input("Enter the directory of the .img file TWRP or CWM (REMEMBER THAT THE RECOVERY MUST BE OF YOUR SMARTPHONE MODEL, remember to write the name of recovery.img as well as the directory)")
        subprocess.call(["fastboot", "flash", "recovery", dir_recovery])
        subprocess.call(["fastboot", "reboot"])
    else:
        OS()

def ADB_FB_L():
    ADB_FASTBOOT_value = input("ADB (Android Debug Bridge) and Fastboot will be downloaded, you want to continue Y/N:")
    if ADB_FASTBOOT_value == "y" or ADB_FASTBOOT_value == "Y":
        subprocess.call(["sudo","apt","install","adb","fastboot"])
    elif ADB_FASTBOOT_value == "n" or ADB_FASTBOOT_value == "N":
        exit
    else:
        ADB_FB_L()

OS()
