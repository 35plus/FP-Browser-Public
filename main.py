import argparse
from driver import Driver
import time


def parse_params(argparse):
    """
    解析参数
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-uuid", "--uuid", help="设备序列号", default='')
    parser.add_argument("-appium_port", "--appium_port", help="appium 端口", default='4723')
    parser.add_argument("-url", "--url", help="访问的目标链接", default='https://fingerprintjs.github.io/fingerprintjs/')
    parser.add_argument("-version", "--version", help="Chrome 驱动的版本号", default='102.0.5005.27')

    args = parser.parse_args()
    url = args.url
    uuid = args.uuid
    appium_port = int(args.appium_port)
    version = args.version

    return url, uuid, appium_port, version


def merge_dict(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def get_driver(config: dict = None, custom_url=None):
    """
    获得驱动
    """
    # 解析参数
    url, uuid, appium_port, version = parse_params(argparse)

    # 访问目标链接
    if custom_url:
        url = custom_url

    config = merge_dict(config, {"url": url})

    # 获得 driver
    appium_driver = Driver.handle(uuid, version, config, appium_port)

    # 设置页面超时
    appium_driver.set_page_load_timeout(15)

    appium_driver.get(url)

    return appium_driver, config


if __name__ == "__main__":
    driver, config = get_driver(config={
        "global.setting-version": "0.1",
        "global.setting-timestamp": "1345678768",
        "global.disable-settings": "0",
        "webgl.vendor": "Qualcomm",
        "webgl.renderer": "Adreno (TM) 640",
        "navigator.user-agent": "Mozilla/5.0 (Linux; Android 11; ASUS_I005DA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
        "navigator.webdriver-status": "0",
        "navigator.platform": "Linux armv8l",
        "navigator.max-touch-points": "5",
        "navigator.hardware-concurrency": "8",
        "navigator.device-memory": "4",
        "navigator.language": "zh",
        "navigator.languages": "zh,en",
        "battery-manager.charging": "1",
        "battery-manager.level": "0.76",
        "connection.effective-type": "4g",
        "connection.type": "wifi",
        "fingerprint.canvas-rand-value": "0.001",
    }, custom_url="http://tyua07.github.io/FP-Browser-Detect/")

    # sleep 防止浏览器退出
    time.sleep(1000)
