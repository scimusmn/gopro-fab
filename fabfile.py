import urllib

from fabric.api import *
from fabric.api import run

# Default GoPro Cherokee webserver IP and port
IP = '10.5.5.9'
API_URL = 'http://' + IP
WEB_URL = 'http://' + IP + ':8080'

# Default GoPro wireless password
PASSWORD = 'goprohero'


@task
def power_off():
    """Turn camera off """
    print
    print power_off.__doc__
    command_send('bacpac', 'PW', '00')


@task
def power_on():
    """Turn camera on """
    print
    print power_on.__doc__
    command_send('bacpac', 'PW', '01')


@task
def switch_mode():
    """Switch camera modes """
    print
    print switch_mode.__doc__
    command_send('bacpac', 'PW', '02')


@task
def capture_stop():
    """Stop the current capture """
    print
    print capture_stop.__doc__
    command_send('bacpac', 'SH', '00')


@task
def capture_start():
    """Start the current capture """
    print
    print capture_start.__doc__
    command_send('bacpac', 'SH', '01')


@task
def preview_off():
    """Turn the preview off """
    print
    print preview_off.__doc__
    command_send('camera', 'PV', '00')


@task
def preview_on():
    """Turn the preview on """
    print
    print preview_on.__doc__
    command_send('camera', 'PV', '02')


@task
def mode_video():
    """Switch to Video mode """
    print
    print mode_video.__doc__
    command_send('camera', 'CM', '00')


@task
def mode_photo():
    """Switch to Photo mode """
    print
    print mode_photo.__doc__
    command_send('camera', 'CM', '01')


@task
def mode_photo_burst():
    """Switch to Photo Burst mode """
    print
    print mode_photo_burst.__doc__
    command_send('camera', 'CM', '02')


@task
def mode_timelapse():
    """Switch to Timelapse mode """
    print
    print mode_timelapse.__doc__
    command_send('camera', 'CM', '03')


@task
def mode_playback():
    """Switch to Playback mode """
    print
    print mode_playback.__doc__
    command_send('camera', 'CM', '05')


@task
def mode_video_02():
    """Switch to Video mode - duplicate """
    print
    print mode_video_02.__doc__
    command_send('camera', 'CM', '06')


@task
def mode_settings():
    """Not working - Switch to Settings mode """
    print
    print mode_settings.__doc__
    command_send('camera', 'CM', '07')


@task
def orientation_up():
    """Set the orientation on the LCD screen on the camera to up"""
    print
    print orientation_up.__doc__
    command_send('camera', 'UP', '00')


@task
def orientation_down():
    """Set the orientation on the LCD screen on the camera to upsidedown"""
    print
    print orientation_down.__doc__
    command_send('camera', 'UP', '01')


"""
Setting Video resolutions

The VR command sets the video resolution but doesn't seem to controll
all the possible resolutionson the Go Pro Hero 3 Black. Here's a list of
commands that used to work for video resolution but now are causing problems.

Cmd - what it used to do - Current response
http://10.5.5.9/camera/VR?t=goprohero&p=%00 - WVGA-60 - 410
http://10.5.5.9/camera/VR?t=goprohero&p=%01 - WVGA-120 - 410
http://10.5.5.9/camera/VR?t=goprohero&p=%04 - 960-30 - 410
http://10.5.5.9/camera/VR?t=goprohero&p=%05 - 960-30 - 200 odd status on LCD
http://10.5.5.9/camera/VR?t=goprohero&p=%08 - ? - 200 reboots camera
http://10.5.5.9/camera/VR?t=goprohero&p=%09 - ? - 410
http://10.5.5.9/camera/VR?t=goprohero&p=%10-* - ? - 410

"""


@task
def video_4k_12fps():
    """Set the video resolution to 4K Cinema at 12 frames per second"""
    print
    print video_res_4k_12fps.__doc__
    command_send('camera', 'VR', '02')


@task
def video_2_7k_24fps():
    """Set the video resolution to 2.7k Cinema at 24 frames per second"""
    print
    print video_res_2_7k_24fps.__doc__
    command_send('camera', 'VR', '03')


@task
def video_960_60_fps():
    """Set the video resolution to 1280x960 4:3 at 48 frames per second"""
    print
    print video_960_test.__doc__
    # 06 - appears to set the same resolution
    # command_send('camera', 'VR', '07')
    command_send('camera', 'VR', '07')


@task
def fov_wide():
    """Change the Field of View to Wide """
    print
    print fov_wide.__doc__
    command_send('camera', 'FV', '00')


@task
def fov_medium():
    """Change the Field of View to Medium """
    print
    print fov_medium.__doc__
    command_send('camera', 'FV', '01')


@task
def fov_narrow():
    """Change the Field of View to Narrow """
    print
    print fov_narrow.__doc__
    command_send('camera', 'FV', '02')


def command_send(device, command, value, debug=True):
    url = 'http://' + IP + '/' + device + '/' + command + \
          '?t=' + PASSWORD + '&' + 'p=%' + value
    print url

    f = urllib.urlopen(url)
    if debug:
        print 'Response code'
        print f.getcode()
