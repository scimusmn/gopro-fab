import urllib2
from bs4 import BeautifulSoup

# Default GoPro Cherokee webserver IP and port
IP = '10.5.5.9'
API_URL = 'http://' + IP
WEB_URL = 'http://' + IP + ':8080'
CAPTURE_LIST = WEB_URL + '/videos/DCIM/100GOPRO/'

# Default GoPro wireless password
PASSWORD = 'goprohero'


def power_off():
    """Turn camera off """
    print
    print power_off.__doc__
    command_send('bacpac', 'PW', '00')


def power_on():
    """Turn camera on """
    print
    print power_on.__doc__
    command_send('bacpac', 'PW', '01')


def switch_mode():
    """Switch camera modes """
    print
    print switch_mode.__doc__
    command_send('bacpac', 'PW', '02')


def capture_stop():
    """Stop a capture """
    print
    print capture_stop.__doc__
    command_send('bacpac', 'SH', '00')


def capture_start():
    """Start a capture """
    print
    print capture_start.__doc__
    command_send('bacpac', 'SH', '01')


def preview_off():
    """Turn the preview off """
    print
    print preview_off.__doc__
    command_send('camera', 'PV', '00')


def preview_on():
    """Turn the preview on """
    print
    print preview_on.__doc__
    command_send('camera', 'PV', '02')


def mode_video():
    """Switch to video mode """
    print
    print mode_video.__doc__
    command_send('camera', 'CM', '00')


def mode_photo():
    """Switch to photo mode """
    print
    print mode_photo.__doc__
    command_send('camera', 'CM', '01')


def mode_photo_burst():
    """Switch to photo burst mode """
    print
    print mode_photo_burst.__doc__
    command_send('camera', 'CM', '02')


def mode_timelapse():
    """Switch to timelapse mode """
    print
    print mode_timelapse.__doc__
    command_send('camera', 'CM', '03')


def mode_playback():
    """Switch to playback mode """
    print
    print mode_playback.__doc__
    command_send('camera', 'CM', '05')


def mode_video_02():
    """Switch to video mode - duplicate """
    print
    print mode_video_02.__doc__
    command_send('camera', 'CM', '06')


def mode_settings():
    """Not working - Switch to settings mode """
    print
    print mode_settings.__doc__
    command_send('camera', 'CM', '07')


def orientation_up():
    """Set the orientation on the LCD screen on the camera to up"""
    print
    print orientation_up.__doc__
    command_send('camera', 'UP', '00')


def orientation_down():
    """Set the orientation on the LCD screen on the camera to upsidedown"""
    print
    print orientation_down.__doc__
    command_send('camera', 'UP', '01')


"""
Setting video resolutions

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


def video_4k_12fps():
    """Set the video resolution to 4K Cinema at 12 frames per second """
    command_send('camera', 'VR', '02')


def video_2_7k_24fps():
    """Set the video resolution to 2.7k Cinema at 24 frames per second """
    command_send('camera', 'VR', '03')


def video_960_60_fps():
    """Set the video resolution to 1280x960 4:3 at 48 frames per second """
    # 06 - appears to set the same resolution
    # command_send('camera', 'VR', '07')
    command_send('camera', 'VR', '07')


def fov_wide():
    """Change the field of view to wide """
    print
    print fov_wide.__doc__
    command_send('camera', 'FV', '00')


def fov_medium():
    """Change the field of view to medium """
    print
    print fov_medium.__doc__
    command_send('camera', 'FV', '01')


def fov_narrow():
    """Change the field of view to narrow """
    print
    print fov_narrow.__doc__
    command_send('camera', 'FV', '02')


def beep_off():
    """Set the button beep volume to zero """
    print
    print beep_off.__doc__
    command_send('camera', 'BS', '00')


def beep_quiet():
    """Set the button beep volume to quiet """
    print
    print beep_quiet.__doc__
    command_send('camera', 'BS', '01')


def beep_loud():
    """Set the button beep volume to loud """
    print
    print beep_loud.__doc__
    command_send('camera', 'BS', '02')


def photo_5mp_m():
    """Set the photo resolution to 5 mega-pixels and field of view to medium"""
    print
    print photo_5mp_m.__doc__
    command_send('camera', 'PR', '03')


def photo_7mp_w():
    """Set the photo resolution to 7 mega-pixels and field of view to wide"""
    print
    print photo_7mp_w.__doc__
    command_send('camera', 'PR', '04')


def photo_11mp_w():
    """Set the photo resolution to 11 mega-pixels and field of view to wide"""
    print
    print photo_11mp_w.__doc__
    command_send('camera', 'PR', '05')


def photo_7mp_m():
    """Set the photo resolution to 7 mega-pixels and field of view to medium"""
    print
    print photo_7mp_m.__doc__
    command_send('camera', 'PR', '06')


def delete_last():
    """Delete last capture

    This will delete the last media captured regardless of type """
    print
    print delete_last.__doc__
    command_send('camera', 'DL', '')


def delete_all():
    """Delete all captures

    This will delete all of the media on the camera. """
    print
    print delete_last.__doc__
    command_send('camera', 'DA', '')


def last_capture():
    """Get the most recent capture

    It's probably worth checking this a bit.
    The last item in the list might not be the latest.
    Best to check for the largest number.
    Do these loop over to the begining?
    """
    capture_files = list_captures()
    print 'File: %s' % capture_files[-1]


def list_captures():
    """Get a list of the videos and photo files on the GoPro

    Use BeautifulSoup to parse the GoPro's list of captures
    This list of captures is provided by the Cherokee webserver on the GoPro
    To get this capture the GoPro Hero 3 Black
    """
    page = urllib2.urlopen(CAPTURE_LIST)
    html_page = page.read()
    soup = BeautifulSoup(html_page)
    captures = soup.find_all('a', class_='link')
    capture_files = []
    for capture in captures:
        capture_file = capture.get('href')
        capture_files.append(capture_file)
    return capture_files


def command_send(device, command, value, debug=True):
    """Use the GoPro wireless server to send a command """

    # For some of the commands there are not values. In this case, we doesn
    # not add a % to the value argument
    if value != '':
        value = '%' + value
    url = 'http://' + IP + '/' + device + '/' + command + \
          '?t=' + PASSWORD + '&' + 'p=' + value
    print url

    f = urllib2.urlopen(url)
    if debug:
        print 'Response code'
        print f.getcode()
