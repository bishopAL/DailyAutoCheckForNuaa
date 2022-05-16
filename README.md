# DailyAutoCheckForNuaa
本项目基本全盘采用了https://github.com/1003389754/nuaa_check_action 项目的代码，由于有些打卡选项有了更新，所以这边重新做了一遍抓包，进行了一些修改，供大家学习使用。还请大家遵守校内纪律和相关法规，对自己和大家负责，希望疫情早日结束！

## 功能
实现自动化定时i南航打卡，完成后将打卡结果发送到指定邮箱。

## 如何使用
1. 下载本Repository，将userData中的信息修改为自己的。其中SenderMail是发件邮箱，SenderMailPassword是密码，SenderMailHost是邮箱smtp地址，比如qq邮箱为smtp.qq.com，南航邮箱为smtp.exmail.qq.com（邮箱需要打开smtp权限，以qq邮箱为例可参考https://service.mail.qq.com/cgi-bin/help?subtype=1&no=166&id=28 ），ReceiverMail为消息接收邮箱。
2. 创建一个**私人**（涉及到账后密码建议不要公开）的新Repository，将1中修改后的整个项目push到新Repository中。
3. 设置Github的Action，过程参考https://github.com/1003389754/nuaa_check_action 的step3。
4. 每日打卡时间可于DailyAutoCheckForNuaa/.github/workflows/main.yml设置，默认设置为0点，但由于Github服务器在美国，因此Github在0点（执行有大约半小时延迟）自动执行脚本，大家可以在国内时间8:30左右收到成功通知。

## 如何抓包
笔者用的是ios平台的stream软件，软件具体如何使用可以百度。在我们的案例中，在i南航的app上填好相关打卡选项，切换到stream点开始抓包，然后切换到i南航打卡，最后切换到stream点结束。抓包信息中POST的第一个包就是我们需要的。包信息如何填写请参考DailyAutoCheck.py。为了更快地解析、复制、粘贴包的内容，可以使用packageProcessor.py，将print得到的内容直接粘贴进代码即可（注意有些例如时间、uid、地址等信息保持原样）。

## 如果收到打卡失败是啥情况
最大的原因可能是打卡项目有更新！遇到失败，请在当天手动打卡。如果这个项目没有更新，则说明手动打卡后软件可以正常使用；如有更新，请升级到最新版本！

## 欢迎issue讨论
