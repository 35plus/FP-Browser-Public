import sys
import os
import json
from appium import webdriver


class Driver(object):

    @staticmethod
    def get_wd_host(port):
        """
        获得 wd 端口
        """
        return 'http://localhost:{}/wd/hub'.format(port)

    @staticmethod
    def format_chrome_driver_options(settions):
        """
        重新组合配置 dict
        """
        params = []

        for (key, item) in settions.items():
            params.append('--{0}={1}'.format(key, item))
        return params

    @staticmethod
    def get_chrome_driver(version):
        """
        获得 chrome 驱动路径
        """
        platform = sys.platform
        dir = r'./drives/' + version
        if os.path.isdir(dir):
            if platform.startswith('win32'):
                path = dir + '/chromedriver.exe'
            elif platform.startswith('darwin'):
                path = dir + '/chromedriver_mac64'
            else:
                path = dir + '/chromedriver_linux64'

            return os.path.abspath(path)
        else:
            raise Exception()

    @staticmethod
    def android_appium_desired_caps(uuid, config, version):
        default_args = [
            "--disable-popup-blocking",
            "--ignore-certificate-errors",
            "--ignore-ssl-errors",
            "--disable-web-security",
            "--incognito",
        ]
        chrome_agrs = default_args + Driver.format_chrome_driver_options(settions=config)
        desired_caps = dict(
            # Platform
            platformName="Android",
            deviceName=uuid,
            udid=uuid,
            browserName="chromium-browser",

            # Common
            noReset=False,
            nativeWebTap=True,
            clearSystemFiles=True,
            newCommandTimeout=60 * 10,  # 最大等待时间，如果超过这个时间没有动作，则自动退出

            # Android Only
            automationName='UiAutomator2',
            deviceReadyTimeout=100,
            skipLogcatCapture=True,
            ensureWebviewsHavePages=True,
            ignoreHiddenApiPolicyError=True,
            chromedriverDisableBuildCheck=True,
            chromedriverExecutable=Driver.get_chrome_driver(version),
            chromeOptions={
                "w3c": False,
                "args": chrome_agrs,
            },
            pageLoadStrategy='none',
        )

        return desired_caps

    @staticmethod
    def handle(
            uuid,
            version,
            config,
            appium_port
    ):
        """
        获得 driver 对象
        """
        # 获得 wd host
        wd_host = Driver.get_wd_host(appium_port)

        return webdriver.Remote(
            wd_host,
            Driver.android_appium_desired_caps(
                uuid=uuid,
                config=config,
                version=version
            )
        )
