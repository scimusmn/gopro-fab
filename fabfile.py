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
def mode_stack_o_papers():
    """Switch to Stack o' Papers mode """
    print
    print mode_stack_o_papers.__doc__
    command_send('camera', 'CM', '02')


@task
def mode_timer_camera():
    """Switch to Timer Camera mode """
    print
    print mode_timer_camera.__doc__
    command_send('camera', 'CM', '03')


@task
def mode_timelapse():
    """Switch to Timelapse mode - DOESN'T WORK """
    print
    print mode_timelapse.__doc__
    command_send('camera', 'CM', '04')


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
    """Switch to Settings mode """
    print
    print mode_settings.__doc__
    command_send('camera', 'CM', '07')


def command_send(device, command, value, debug=False):
    url = 'http://' + IP + '/' + device + '/' + command + \
          '?t=' + PASSWORD + '&' + 'p=%' + value

    f = urllib.urlopen(url)
    if debug:
        print 'Response code'
        print f.getcode()
