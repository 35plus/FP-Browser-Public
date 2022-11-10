## 联系我
微信: @tyua07

![wechat](https://github.com/tyua07/FP-Browser-Detect/raw/master/docs/wechat.jpg)

## 项目介绍
这是一个移动端指纹浏览器项目，我们通过收集需要测试的手机型号的配置，使用虚拟化创建模拟器，再通过代码方式注入到模拟器的浏览器运行时环境，从而达到动态修改浏览器运行时环境的功能，让模拟器里的浏览器环境和真机里的环境保持一致。
这种方式相当于是底层修改了手机配置，能通过任何 js 检测，并且动态注入后，配置在浏览器是永久生效。
通过虚拟化的技术还可以实时动态扩容模拟器，从而实现像云计算那种便捷高效的管理浏览器容器。

## 核心优势

* 多版本指纹浏览器。因为随着 web 的发展 w3c 的标准也会随着变化。对此，我们提供了多版本兼容的指纹浏览器方案。
* 多架构平台 app。我们提供 arm、arm64、x84_64 等平台的浏览器。当然如果您有需求，我们还可以提供更多。
* 分布式测试。我们拥有完整的分布式测试的解决方案，让您可以快速、高效的进行大批量数据测试。
* 客户端 SDK。示例中我们实际是拿一个 json 去注入，这样可能会造成参数格式错误。对此，我们完成了注入项的全部 sdk 功能开发，以确保每个参数的合法性。并且我们还会提供每个参数的详细解释，来确保用户的场景准确性。
* [浏览器检测](https://github.com/tyua07/FP-Browser-Detect) 。公开的项目我们只是提供了部分的检测项。在完整版中，对于每一项修改项都有完整的单元测试检测。

## 相关开源项目
* [FP-Browser-Public 浏览器底层动态注入](https://github.com/tyua07/FP-Browser-Public) 
* [FP-Browser-Detect 浏览器属性检测](https://github.com/tyua07/FP-Browser-Detect)

## 动态注入前后对比

案例中使用的是一台雷电模拟器，模拟器的配置是：4核 + 4GB 的三星机型。因为是在 windows 64 操作系统下，所以检测出来的 navigator.platform 是 Linux x86_64位。
通过注入以下参数，我们让模拟器的运行时环境强制改变。

```json
{
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
    "battery-manager.charging": "0",
    "battery-manager.level": "0.76",
    "connection.effective-type": "4g",
    "connection.type": "wifi",
    "fingerprint.canvas-rand-value": "0.001"
}
```

### 静态网站检测
我们开源了这些浏览器属性的检测项源码，可以直接参考 [FP-Browser-Detect](https://github.com/tyua07/FP-Browser-Detect) 进行对照。

### 注入前

![之前](https://github.com/tyua07/FP-Browser-Public/raw/master/docs/before_1.png)
![之前](https://github.com/tyua07/FP-Browser-Public/raw/master/docs/before_2.png)

### 注入后

![之前](https://github.com/tyua07/FP-Browser-Public/raw/master/docs/after_1.png)
![之前](https://github.com/tyua07/FP-Browser-Public/raw/master/docs/after_2.png)

### 注入对比
以下两张 GIF 截图展示一下：

* [改机后](https://imgur.com/a/1GI3dMx)
* [改机前](https://imgur.com/a/aD1jXqj)

## 注入选项

注意：请在使用前配置好设备的运行时环境，比如语言、时间等。

#### 状态类型

待确认：暂未验证。<br />通过：通过检测（一般是指：通过专业逻辑检测通过）。<br />通过（自身）：通过自身的检测逻辑（如果以后有专业检测逻辑，还需要通过专业检测逻辑进行检测）。<br />异常：检测未通过。<br />暂不处理：暂时不需要处理。

#### 列表
| **系统相关** | **参数名** | **验证** | **描述** | **示例** |
| --- | --- | --- | --- | --- |
|  | basic.disable-window-chrome | 通过 | 是否禁用 window.chrome「1：true; 0：false」 | 1 |
|  | basic.timezone | 通过 |  时区 | Asia/Shanghai |
|  | basic.init-history-length | 通过 | 设置初始化的历史记录数量 | 10 |
|  | basic.inject-js | 通过 | 注入的js | 详细请看「[注入 js](#EzXob)」 |
|  | basic.inject-system-js |  | 注入的js（由系统控制，不允许客户端注入） |  |
|  | basic.allow-permissions | 通过 | 直接允许的权限**（详细请看“权限枚举列表”）** | [3] |
|  | basic.reject-permissions | 通过 | 直接拒绝的权限**（详细请看“权限枚举列表”）** | [4] |
| **版本信息** | version-info.product-name | 通过 | 产品名称 | Google Chrome |
|  | version-info.number | 通过 | 版本号 | 89.0.0.4389 |
| **字体相关** | font.list-json | 通过 | 注入字体**（注意：有小概率注入不成功）** | ["Marlett","Haettenschweiler"] |
| **Navigator 相关** | navigator.webdriver-status | 通过 | 设置  webdriver 状态「1：true; 0：false」 | 0 |
|  | navigator.user-agent | 通过 | 设置 User-Agent | Mozilla/5.0 (Linux; Android 9; vivo X22A Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.3440.91 Mobile Safari/537.36 |
|  | navigator.user-agent-auto-match | 通过 | 修改 UserAgent 里的版本号，自动对应 "version-info.number" 字段的值 | 1 |
|  | navigator.reduced-major-in-minor-version-number | 通过 | 强制只获取主版本号（例如：把 96.0.4664.104 变成 96.0.0.0） | 0 |
|  | navigator.platform | 通过 | 平台 | Linux armv8l（详细请看「[Platform](#Mq7Nr)」） |
|  | navigator.vendor | 通过 | 浏览器供应商的名称 | Apple Computer, Inc. 和 Google Inc. |
|  | navigator.max-touch-points | 通过 | 设备能够支持的最大同时触摸的点数「移动端：5; PC:1」 | 5 |
|  | navigator.hardware-concurrency | 通过 | 处理器数量 | 8 |
|  | [navigator.device-memory](https://github.com/w3c/device-memory#the-web-exposed-api) | 通过 | 设备内存数 | 4 |
|  | [navigator.do-not-track](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/doNotTrack) | 通过 | 设置 Do Not Track（如果强制不追踪就设置为 “1”，否则请不要设置该值。） | 1 |
|  | navigator.enable-plugin | 通过 | 是否启用插件（注意：如果是移动端建议**关闭**）「1：true; 0：false」 | 1 |
|  | navigator.plugin-json | 通过 | 插件（只有 enable-plugin 设置为 1，该属性才生效） | 详细请看「[插件](#HqV4F)」 |
|  | navigator.enable-fake-plugin | 通过 | 是否启用默认 PC 端自带的五个插件「1：true; 0：false」（（只有 navigator-enable-plugin 设置为 1，该属性才生效。如果是 PC 端建议**开启**，如果是移动端建议**关闭**） | 1 |
|  | navigator.online | 通过 | 是否在线「1：true; 0：false」（**注意：建议强烈设置成 1**） | 1 |
|  | navigator.java-enabled | 通过 | javaEnabled「1：true; 0：false」**(注意：建议设置成对应机型的值)** | 1 |
|  | navigator.pdf-viewer-enabled | 通过 | pdfViewerEnabled「1：true; 0：false」**(注意：建议设置成对应机型的值)** | 1 |
|  | navigator.bluetooth-availability | 通过 | 蓝牙可用性「1：true; 0：false」（**注意：建议强烈设置成 1**） |  1 |
|  | navigator.language | 通过 | 用户偏好语言 | zh-CN |
|  | navigator.languages | 通过 | 浏览器支持语言（多个请用**","**符号连接） | zh-CN,zh,en |
| **Client Hints** | client-hints.disable | 通过 | 是否启用 client hints「1：true; 0：false」 | 1 |
|  | client-hints.disable-json | 通过 | 禁用指定的 ua-client-hints 属性 | ["15"] |
|  | client-hints.viewport-width | 通过 | 宽度 | 980 |
|  | client-hints.viewport-height | 通过 | 高度 | 980 |
|  | client-hints.prefers-color | 通过 | 显示模式 「dark；light」 | dark |
|  | client-hints.mobile | 通过 | 是否是手机「1：true; 0：false」 | 1 |
|  | client-hints.platform | 通过 | 平台 | Android |
|  | client-hints.platform-version | 通过 | 平台版本 | 12.0.0 |
|  | client-hints.architecture | 通过 | 平台架构的字符串。例如，"x86" | arm |
|  | client-hints.bitness | 通过 | 架构位数的字符串。例如，"64" | 64 |
|  | client-hints.wow64 | 通过 | 如果二进制文件是在 32 位模式下构建并在 64 位上运行，则返回 true；否则返回 false。「1：true; 0：false」 | 0 |
|  | client-hints.model | 通过 | 手机型号 | Redmi Note 9 Pro |
| **性能相关** | performance.match-json | 通过 | 多组匹配修改：type、redirect-count、timing 等<br />如何导航到该页面，详细请查看链接：[https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigation/type](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigation/type) | {     "target_url": "https://so.com",     "match_type": "1",     "match_break": "1",     "navigation_type": "1",     "navigation_redirect_count": "78",     "timing_connectEnd_offset": "0",     "timing_connectStart_offset": "0",     "timing_domComplete_offset": "0",     "timing_domContentLoadedEventEnd_offset": "0",     "timing_domContentLoadedEventStart_offset": "0",     "timing_domInteractive_offset": "0",     "timing_domLoading_offset": "0",     "timing_domainLookupEnd_offset": "0",     "timing_domainLookupStart_offset": "0",     "timing_fetchStart_offset": "0",     "timing_loadEventEnd_offset": "0",     "timing_loadEventStart_offset": "0",     "timing_navigationStart_offset": "0",     "timing_redirectEnd_offset": "190.8",     "timing_redirectStart_offset": "0",     "timing_requestStart_offset": "0",     "timing_responseEnd_offset": "0",     "timing_responseStart_offset": "0",     "timing_secureConnectionStart_offset": "0",     "timing_unloadEventEnd_offset": "0",     "timing_unloadEventStart_offset": "0" } |
| **运行内存相关** | memoryinfo.total-js | 通过 | 可使用的内存 | 95301723 |
|  | memoryinfo.used-js | 通过 | JS 对象（包括V8引擎内部对象）占用的内存数 | 92349659 |
|  | memoryinfo.limit-js | 通过 | 内存大小限制 通常，usedJSHeapSize不能大于totalJSHeapSize，如果大于，有可能出现了内存泄漏 | 4294705152 |
| **窗口相关** | frame.disable-alert | 通过 | 是否禁用 alert 弹框「1：true; 0：false」 | 1 |
|  | frame.disable-window-open | 通过 | 是否禁用 window.open 弹框「1：true; 0：false」 | 1 |
|  | frame.confirm | 通过 | 强制 confirm 弹框的值「1：true; 0：false」 | 1 |
| ** | media.list-json | 通过 | 硬件设备信息 | 详细请看「硬件设备信息」 |
|  | media.matchs-json | 通过 | 媒体查询 | 详细请看「修改 window.matchs 匹配」 |
| **Screen 相关** | screen.color-depth | 通过 | colorDepth（屏幕的色彩深度） | 30 |
|  | screen.width | 通过 | 屏幕宽度（单位：px） | 393 |
|  | screen.height | 通过 | 屏幕高度（单位：px） | 851 |
|  | screen.avail-width | 通过 | 可用空间的屏幕宽度（单位：px） | 393 |
|  | screen.avail-height | 通过 | 可用空间的屏幕高度（单位：px） | 851 |
|  | screen.avail-left | 通过 | 可用空间的左边边界的第一个像素点 | 0 |
|  | screen.avail-top | 通过 | 可用空间的顶部边界的第一个像素点 | 0 |
|  | screen.orientation-angle | 通过 | 屏幕方向「0、90、180、270」，注意：请配合 “<br />ScreenOrientationType” 搭配使用。 | 0 |
|  | screen.orientation-type | 通过 | 屏幕方向「"portrait-primary"、"landscape-primary"、"landscape-secondary"」<br />，注意：请配合 “<br />ScreenOrientationAngle” 搭配使用。 | portrait-primary |
|  | screen.device-pixel-ratio | 通过 | 设备像素比 | 3 |
| **Rect 相关** | rect.width | 通过 | 可视区域页面宽度 | 350 |
|  | rect.height | 通过 | 可视区域页面高度 | 780 |
| **Document 相关** | document.match-json | 通过 | 多组匹配修改：标题、referrer、当前链接 | https://qq.com/index.html |
|  | document.is-trusted | 通过 | 是否是用户执行的事件「1：true; 0：false」（**注意：建议强烈设置成 1**） | 1 |
|  | document.compat-mode | 通过 | 渲染模式 | CSS1Compat |
|  | document.charset | 通过 | 文档编码 | GBK |
|  | document.lastModified | 通过 | 文档最后更新时间 | 15874423673 |
|  | document.video-support-mime-types-json | 通过 | 支持播放的视频格式<br />详细请看：「[模糊匹配视频支持格式](#n6919)」 | [ { "type": "dmlkZW8vb2dnOyBjb2RlY3M9InRoZW9yYSI=", "support": "maybe", } ] |
| **Header 相关** | header.x-requested-with | 通过 | 设置 X-Requested-With 的值 | com.xunmeng.pinduoduo |
|  | header.extra-json | 通过 | 额外的 header（**注意：如果强制设置原本存在的 key，不会有效果**） | { "name": "header1", "value": "value1" }, { "name": "header2", "value": "value2" } |
| **Cookie 相关** | cookie.status | 通过 | 是否开启 cookie 「1：true; 0：false」 | 0 |
|  | cookie.json | 通过 | 注入 Cookie 值 | [ { "port": "80", "domain": ".baidu.com", "name": "BAIDUID", "value": "xxxxx6B7E8F02313:FG=1" }, { "port": "80", "domain": ".so.com", "name": "name2", "value": "aaaaa2" } ] |
| **电量相关** | battery-manager.charging | 通过 | 是否正在充电「1：true; 0：false」 | 0 |
|  | battery-manager.charging-time | 通过 | 距离充电完毕还需多少秒，如果为0则充电完毕（double 类型，可以 infinity 和 - infinity） | null |
|  | battery-manager.discharging-time | 通过 | 距离电池耗电至空且挂起需要多少秒（double 类型，可以 infinity 和 - infinity） | null |
|  | battery-manager.level | 通过 | 电量（单位是两位小数。例如：0.28 代表百分之 28 的电量。最大为 1，代表百分之百电量。） | 0.98 |
| **网络相关** | connection.effective-type | 通过 | [网络有效类型](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/effectiveType) | 4g |
|  | connection.type | 通过 | [网络类型](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/type)<br />详细请看「[ConnectionType 类型](#lCUHi)」 | cellular |
|  | connection.downlink | 通过 | 网络下行速度 | 1.75 |
|  | connection.downlink-max | 通过 | 网络最大下行速度 | 100 |
|  | connection.rtt | 通过 | 估算的往返时间 | 100 |
|  | connection.save-data | 通过 | 打开/请求数据保护模式「1：true; 0：false」 | 0 |
| ** | fingerprint.audio-rand-value | 通过 | 音频指纹**偏移量「范围：**99.000 ~ 0.999**」** | 0.98 |
|  | fingerprint.canvas-rand-value | 通过 | Canvas 指纹**偏移量「范围：**99.000 ~ 0.999**」** | 0.32 |
|  | fingerprint.webgl-rand-value | 通过 | Webgl 指纹**偏移量「范围：**0.000 ~ 0.999**」** | 0.001 |
| **显卡相关** | webgl.vendor | 通过 | 显卡供应商 | Qualcomm |
|  | webgl.renderer | 通过 | 显卡型号 | Adreno (TM) 612 |
| [**加速度**](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEventAcceleration) | device-motion.interval | 通过 | 加速度获取间隔（建议不设置该值，由系统自动生成） |  |
|  | device-motion.x1 | 通过 | X加速度 | -0.1509007066488266 |
|  | device-motion.x1-left | 通过 | X加速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.x1-right | 通过 | X加速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.y1 | 通过 | Y加速度 | -0.0059375762939453125 |
|  | device-motion.y1-left | 通过 | Y加速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.y1-right | 通过 | Y加速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.z1 | 通过 | Z加速度 | 0.04666939377784729 |
|  | device-motion.z1-left | 通过 | Z加速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.z1-right | 通过 | Z加速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** |  |
| [**加速度（该值包括重力的影响）**](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/accelerationIncludingGravity) | device-motion.x2 | 通过 | X加速度（**该值包括重力的影响**） | -0.4155784845352173 |
|  | device-motion.x2-left | 通过 | X加速度（**该值包括重力的影响**）(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.x2-right | 通过 | X加速度（**该值包括重力的影响**）(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.y2 | 通过 | Y加速度（**该值包括重力的影响**） | 9.564980506896973 |
|  | device-motion.y2-left | 通过 | Y加速度（**该值包括重力的影响**）(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.y2-right | 通过 | Y加速度（**该值包括重力的影响**）(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.z2 | 通过 | Z加速度（**该值包括重力的影响**） | 0.26034310460090637 |
|  | device-motion.z2-left | 通过 | Z加速度（**该值包括重力的影响**）(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  |
|  | device-motion.z2-right | 通过 | Z加速度（**该值包括重力的影响**）(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** |  |
| [**设备围绕所有三个轴旋转的速率**](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEventRotationRate) | device-motion.alpha | 通过 | alpha 旋转速度 | -0.7907827602396802 |
|  | device-motion.alpha-left | 通过 | alpha 旋转速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  0.1 |
|  | device-motion.alpha-right | 通过 | alpha 旋转速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** | 0.2 |
|  | device-motion.beta | 通过 | beta 旋转速度 | 0.22675585046165 |
|  | device-motion.beta-left | 通过 | beta 旋转速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  0.1 |
|  | device-motion.beta-right | 通过 | beta 旋转速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** | 0.2 |
|  | device-motion.gamma | 通过 | gamma 旋转速度 | -0.4725504797087403 |
|  | device-motion.gamma-left | 通过 | gamma 旋转速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  0.1 |
|  | device-motion.gamma-right | 通过 | gamma 旋转速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** | 0.2 |
| [**网页的设备的物理方向的信息**](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent) | device-orientation.alpha | 通过 | alpha 旋转速度 | 88.18197488483892 |
|  | device-orientation.alpha-left | 通过 | alpha 旋转速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  0.1 |
|  | device-orientation.alpha-right | 通过 | alpha 旋转速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** | 0.2 |
|  | device-orientation.beta | 通过 | beta 旋转速度 | 37.221763387241076 |
|  | device-orientation.beta-left | 通过 | beta 旋转速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  0.1 |
|  | device-orientation.beta-right | 通过 | beta 旋转速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** | 0.2 |
|  | device-orientation.gamma | 通过 | gamma 旋转速度 | 49.19596650622097 |
|  | device-orientation.gamma-left | 通过 | gamma 旋转速度(偏移量：左)**（注意：设置后，返回的值只保留一位小数）** |  0.1 |
|  | device-orientation.gamma-right | 通过 | gamma 旋转速度(偏移量：右)**（注意：设置后，返回的值只保留一位小数）** | 0.2 |
|  | device-orientation.absolute | 通过 | 设备是否绝对提供方向数据「1：true; 0：false」（**注意：建议不设置该值**） | 0 |
| [**WebRTC相关**](https://developer.mozilla.org/zh-CN/docs/Web/API/WebRTC_API/Protocols) | webrtc.privite-ip | 通过 | 强制设置 stun 协议获得的局域网 IP | 192.168.0.100 |
|  | webrtc.public-ip | 通过 | 强制设置 stun 协议获得的外网 IP | 8.8.8.8 |
|  | webrtc.host-name | 暂不处理 | 强制设置 stun 协议获得的 hostname | 9923c2-459f-beeb-ac5f4ca215cf.local |
| [**位置相关**](https://developer.mozilla.org/zh-TW/docs/Web/API/GeolocationCoordinates) | geo.longitude | 通过 | 经度 | 117.12874 |
|  | geo.latitude | 通过 | 纬度 | 25.3502944 |
|  | geo.accuracy | 通过 | 经度精确值 | 2417.3790234045855 |
|  | geo.altitude | 通过 | 海平面高度（无法提供时为 null） | null |
|  | geo.altitude-accuracy | 通过 | 高度精确值（无法提供时为 null） | null |
|  | geo.heading | 通过 | 前进方向（无法提供时为 null） | null |
|  | geo.speed | 通过 | 速度（无法提供时为 null） | null |
| **剪切板** | clipboard.text | 通过 | 强制设置剪切板内容 | "12121" |
| **语音合成相关** | speech-synthesis-voice.force-override | 通过 | 是否强制覆盖本来的语音信息「1：true; 0：false」 | 0 |
|  | speech-synthesis-voice.append-mode | 通过 | 追加方式：push：尾部追加；insert：顶部追加 |  push |
|  | speech-synthesis-voice.json | 通过 |  注入的语音信息（**注意：如果注入不正确，请参考该链接：**[https://stackoverflow.com/questions/49506716/speechsynthesis-getvoices-returns-empty-array-on-windows](https://stackoverflow.com/questions/49506716/speechsynthesis-getvoices-returns-empty-array-on-windows)） | [     {         "name": "name",         "lang": "lang",         "is_local_service": "0"     } ] |
|  **全局相关** | global.disable-settings | 通过 | 是否禁用全部选项「1：true; 0：false」 |  0 |
| **JA3相关** | ja3.min-version |  | 最小支持的 tls 版本号（**注意：非必要，请不要使用该参数**） | tls1.2 |
|  | ja3.max-version |  | 最大支持的 tls 版本号（**注意：非必要，请不要使用该参数**） | tls1.3 |


## 示例操作

我们通过一个实战案例来展示动态注入浏览器属性的流程（只是展示一些常用的属性，完整版有超过 150 项）。接下来，通过修改以下参数，来对比修改前和修改后的区别。

| **类型** | **选项** | **说明** |
| --- | --- | --- |
| Navigator 相关 | navigator.user-agent | userAgent |
| Navigator 相关 | navigator.platform | 平台 |
| Navigator 相关 | navigator.hardware-concurrency | 处理器数量 |
| Navigator 相关 | navigator.device-memory | 内存大小 |
| Navigator 相关 | navigator.language | 首选项语言 |
| Navigator 相关 | navigator.languages | 支持的语言 |
| Navigator 相关 | navigator.webdriver-status | 是否是自动化测试 |
| Navigator 相关  | navigator.max-touch-points | 多点触控 |
| 电量相关 | battery-manager.charging | 是否充电 |
| 电量相关 | battery-manager.level | 电量 |
| 网络相关 | connection.type | 网络类型 |
| 网络相关 | connection.effective-type | 网络有效类型 |
| 指纹相关 | fingerprint.canvas-rand-value  | canavs 指纹 |
| 显卡硬件相关 | webgl.vendor | 显卡供应商 |
| 显卡硬件相关 | webgl.renderer | 显卡型号 |

### 生成注入参数
> 注意：这里我们使用了 SDK 去完成，实际上传到 git 仓库的是一个 json 配置。虽然两者看起来有差异，但是不影响去使用。

#### UserAgent
UA 里包含的了很多重要的设备相关信息在里面。

1. Android 11：安卓的版本
2. ASUS_I005DA：手机的型号
3. Chrome/102.0.0.0： 浏览器的版本号
> 注意：因为关于浏览器版本号有几个地方都可以获取（比如：navigator.userAgentData ），如果仅仅把 UA 设置成 102.0.0.0 ，会导致和其他地方获取的版本号不一样，所以在完整版中有一个选项是单独针对浏览器版本的设置。而且还有一个是否自动匹配浏览器版本的选项，开启该选择后， UA 里填写的是 102，在单独设置浏览器版本里填写的是 101，则会自动把 UA 里的版本号设置为 101。


```python
navigator = Navigator() \
.set_user_agent(
    "Mozilla/5.0 (Linux; Android 11; ASUS_I005DA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36")
```

#### Platform
平台，如果是 android 一般都是 Linux a 开头，所以虚拟化的设备一定要改掉这个值。
```python
@unique
class Platform(str, Enum):
    LINUX_ARMV8L = "Linux armv8l"
    LINUX_ARMV7L = "Linux armv7l"
    LINUX_ARMV6L = "Linux armv6l"
    LINUX_AARCH64 = "Linux aarch64"
    LINUX_X86_64 = "Linux x86_64"
    LINUX_I686 = "Linux i686"
    MACINTEL = "MacIntel"
    WIN32 = "Win32"
    WIN64 = "Win64"
    WINCE = "WinCE"
    SUNOS = "SunOS"
    IPHONE = "iPhone"
    IPOD = "iPod"
    IPAD = "iPad"
    
navigator = Navigator() \
            .set_platform(Platform.LINUX_ARMV8L)
```
#### hardwareConcurrency
CPU 的处理器数量，一般策略会检测是否是常规数值，如果是很大的数值则可能是异常。
```python
navigator = Navigator() \
            .set_hardware_concurrency(8)
```

#### deviceMemory
内存大小，一般策略会检测是否是常规数值，如果是很大的数值则可能是异常。
```python
navigator = Navigator() \
            .set_device_memory(4)
```

#### language
首选项语言，一般默认是中文
```python
 navigator = Navigator() \
            .set_language("zh")
```
#### 
#### languages
支持的语言
```python
navigator = Navigator() \
            .set_languages("zh,en")
```

#### webdriver
是否是自动化测试，这是一个很危险的属性。
 该属性的正常值一般分为 2 种，第一种是 false，表示没有启用自动化；一种是 undefined，表示没有该属性。chrome 的 88.0.4324.93 后就有该值了，所以可以强制设置为 false 就行了。当然如果想设置为 undefined 的话，在完整版里有注入 js 这个选项，可以把这个属性给强制删除就行了。还有一种办法就是单独编译一个版本强制把这个属性给删除。
```python
navigator = Navigator() \
            .set_webdriver_status(False)
```

#### maxTouchPoints
多点触控点数，移动端一般是 5，电脑端是 1。
> 注意：为什么说移动端一般是 5 呢？因为在我们收集的型号数据里，有些该值并不是 5 的情况。所以一般检测策略会再去判断是否执行 touch 事件。

```python
@unique
class MaxTouchPoint(int, Enum):
    MOBILE = 5
    PC = 1
    
navigator = Navigator() \
            .set_max_touch_points(MaxTouchPoint.MOBILE)
```

#### charging
是否充电中，如果一直插着数据线充电的话，这个值一直是 true。
```python
battery = Battery() \
            .set_charging(False)
```

#### level
电量。有效范围 1- 100
```python
battery = Battery() \
            .set_level(76)
```

#### type
网络有效类型，一般获取到的是 wifi 和 cellular。
```python
@unique
class WebConnectionType(str, Enum):
    CELLULAR = 'cellular'
    BLUETOOTH = 'bluetooth'
    ETHERNET = 'ethernet'
    WIFI = 'wifi'
    WIMAX = 'wimax'
    OTHER = 'other'
    NONE = 'none'
    UNKNOWN = 'unknown'
    
network = Network() \
            .set_type(WebConnectionType.WIFI)
```

#### effectiveType
网络类型，一般获取到的是 4g。
> 注意：如果 type 是 wifi，effectiveType 的值也是 4g。
```python
class WebEffectiveConnectionType(str, Enum):
    kTypeUnknown = '4g'
    kTypeOffline = '4g'
    kTypeSlow2G = 'slow-2g'
    kType2G = '2g'
    kType3G = '3g'
    kType4G = '4g'
    
network = Network() \
            .set_effective_type(WebEffectiveConnectionType.kType4G)
```
#### Canvas
canvas 指纹。这个是很多检测项都会去获取的值，这个可以理解成设备的标识符。所以一般都是随机化，在 SDK 里我们已经做好了自动随机化的，只需要调用 auto_canvas_offset 就可以实现自动随机。
> 注意：这个虽然我把它称为设备标识符，但其实这个是不准确的说法。

```python
 fingerprint_offset = FingerprintOffset() \
            .set_canvas_offset(0.001)
```

#### WebGL Vendor
显卡供应商
```python
basic = Basic() \
            .set_webgl_vendor('Qualcomm')
```

#### WebGL Renderer
显卡型号
```python
 basic = Basic() \
            .set_webgl_renderer('Adreno (TM) 640')
```

### 注入配置
最终我们通过以上代码注入的配置如下：
```json
{
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
    "battery-manager.charging": "0",
    "battery-manager.level": "0.76",
    "connection.effective-type": "4g",
    "connection.type": "wifi",
    "fingerprint.canvas-rand-value": "0.001",
}
```

### apk 安装

我们提供了两款功能一致的 apk，分别对应模拟器和真实设备。下载后请提前安装到对应的设备下。 下载地址：
* [arm_64.apk](https://hloa7xpsow.feishu.cn/file/boxcnXZaMYC1LbFmcv0qkueYJOb) ：普通 arm 的真实手机
* [x86_64.apk](https://hloa7xpsow.feishu.cn/file/boxcn8i5viSOizVYdTYVEbt5nOf) ：模拟器手机

### 环境配置

#### Docker

为了方便，我们提供了一个配置好的 ubuntu 镜像，可以直接运行。因为项目依赖 google 相关东西，需要科学上网，所以就直接打包成 docker 镜像。

下载镜像到本地

下载地址：https://hloa7xpsow.feishu.cn/file/boxcn5JJVcyHz0tXnDt5u2LF6ye

加载镜像

``docker load --input fp_browser_public.image.tar``

创建并进入容器

``docker run --name fp_browser -it fp_browser_public:1.0 /bin/bash``

进入容器

``docker exec -it fp_browser /bin/bash``

### 配置 Appium 环境

> 如果是 docker 环境，则可以跳过该步骤。

#### Windows（以下两种任选一种）

* [Windows 环境下配置 appium 一](https://zhuanlan.zhihu.com/p/62054794)
* [Windows 环境下配置 appium 二](https://zhuanlan.zhihu.com/p/49193525)

### 运行实例代码 

注意：
* 因为在 Windows 下，模拟器和 docker 不能共存，所以接下来我会演示 docker + 真机方式 和 非docker + 模拟器方式。
* 如果我们使用的是 docker 的方式，我们通过 ip 方式连接，因为 docker 内部是不能通过序列号连接模拟器的。
* 在 docker 环境里，事先配置好了全部依赖，所以只需要连接设备和拉去代码就能顺利进行测试了。

#### docker + 真机方式

##### 启动 appium

需要单独开启一个终端进入容器里，在容器里面启动 appium

* 进入容器 `` docker exec -it fp_browser /bin/bash ``
* 执行命令 `` appium ``

> 注意：需要提前安装好 nodejs，如果是 docker 容器的方式，默认就已经有了 appium。

##### 连接真机

> 注意：当前的操作是在宿主机上操作，不是在 docker 容器里。

开启开发者模式后，拿手机设备 USB 连接到电脑，执行 ``adb kill-server && adb devices``，出现了设备后执行 ``adb tcpip 5555``，然后找到设备的局域网 ip，通过执行 ``adb connect ip:5555`` 连接。
这样我们不仅可以在本机也可以用 ip 方式连接，还可以在 docker 容器里面也用这种方式连接。

延伸阅读

* [ADB——连接手机的三种方式](https://www.cnblogs.com/zhuminghui/p/10457674.html)
* [Android中使用adb命令通过IP地址连接手机](https://cloud.tencent.com/developer/article/1741645)

##### 进入容器

``docker exec -it fp_browser /bin/bash``

##### 连接真机

因为我们在宿主电脑上已经可以通过 ip 方式连接设备了，所以在 docker 容器里也可以直接进行连接。
例如：

``adb connect 192.168.0.2:5555``

如果正常连接到设备后，执行 ``adb devices`` 会输出如下：

``
192.168.0.2:5555 device
``

##### 拉取代码

``cd ~ && git clone https://github.com/tyua07/FP-Browser-Public.git``

##### 执行测试

``cd ~/FP-Browser-Public && python3 main.py --uuid=192.168.0.2:5555``

#### 非 docker + 模拟器方式

##### 启动 appium

需要单独开启一个终端然后启动 appium

* 执行命令 `` appium ``

> 注意：需要提前安装好 nodejs。并用 npm 全局安装好 appium ``npm install -g appium ``。详细请参考上面的环境配置章节。

##### 连接模拟器

我们随便下载一款模拟器软件，比如夜神、雷电、甚至官方提供的模拟器也行。然后安装后，创建一个模拟器即可。默认创建的模拟器的名称是 ``emulator-`` 开头的。
执行 ``adb devices``，会出现如下：

```
PS C:\Users\Administrator\Desktop> adb devices
List of devices attached
emulator-5554   device
```
表示连接成功了。

如果出现设备的状态 ``offline`` 则需要强制让设备重新连接连接一下

```
* daemon not running; starting now at tcp:5037
* daemon started successfully
List of devices attached
emulator-5554   offline
```

强制重新连接步骤如下：
* adb reconnect offline
* adb devices

##### 拉取代码

``git clone https://github.com/tyua07/FP-Browser-Public.git``

##### 安装依赖

* ``cd FP-Browser-Public``
* ``pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/``
* ``pip install -r .\requirements.txt``

##### 执行测试

``python main.py --uuid=emulator-5554``

## 其他

### main.py 参数说明

* --uuid：设备序列号或者ip:端口
* --appium_port：appium 的端口号，默认是 4723
* --url：默认浏览器打开的网址，在默认测试中，打开的网址是：http://tyua07.github.io/FP-Browser-Detect/
* --version：Chrome 驱动的版本号

### 强制让配置不生效

在 ``main.py`` 文件的配置里 有 ``global.disable-settings`` 属性，如果设置为 1 则表示不生效改机配置。

### 下载 chromedriver 驱动
默认代码仓库里面已经包含了 chrome driver，也可以去 [官方](https://chromedriver.chromium.org/downloads) 去下载。

注意：默认的驱动是有特征的。 特征如下：

* window.cdc_adoQpoasnfa76pfcZLmcfl_Array
* window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
* window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
* document.$chrome_asyncScriptInfo
* document.$cdc_asdjflasutopfhvcZLmcfl_

所以在完整版中有两种解决方案。

* 一：通过自定义编译，把这些属性都删掉。
* 二：通过完整版中的 js 注入功能，在页面加载前就把属性删掉