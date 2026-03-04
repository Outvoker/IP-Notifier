# IP Uploader - 公网IP自动邮件通知

Windows开机自动获取公网IP并发送到指定邮箱。

## 功能特点

- 自动获取公网IP地址（即使电脑在路由器后面）
- 开机自动执行
- 通过邮件发送IP信息
- 使用uv管理Python依赖

## 安装步骤

### 1. 安装uv

如果还没有安装uv，在PowerShell中运行：
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 配置QQ邮箱SMTP授权码

1. 登录QQ邮箱网页版
2. 点击"设置" -> "账户"
3. 找到"POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"
4. 开启"POP3/SMTP服务"或"IMAP/SMTP服务"
5. 生成授权码（不是QQ密码！）
6. 保存这个授权码

### 3. 配置启动脚本

编辑 `startup.bat` 文件，填入你的邮箱信息：
```batch
set SENDER_EMAIL=your_email@qq.com
set SENDER_PASSWORD=your_qq_smtp_authorization_code
```

**重要**: `SENDER_PASSWORD` 是QQ邮箱的授权码，不是QQ密码！

### 4. 测试运行

在项目目录下双击 `startup.bat` 测试是否正常工作。

### 5. 设置开机自启动

#### 方法一：启动文件夹（推荐）

1. 按 `Win + R` 打开运行对话框
2. 输入 `shell:startup` 并回车
3. 将 `startup.bat` 的快捷方式复制到打开的文件夹中

#### 方法二：任务计划程序

1. 按 `Win + R`，输入 `taskschd.msc` 并回车
2. 点击右侧"创建基本任务"
3. 名称：IP Notifier
4. 触发器：选择"计算机启动时"
5. 操作：选择"启动程序"
6. 程序/脚本：浏览选择 `startup.bat` 的完整路径
7. 起始于：填写 `startup.bat` 所在的文件夹路径
8. 完成

## 文件说明

- `ip_notifier.py` - 主程序脚本
- `pyproject.toml` - uv依赖管理配置
- `startup.bat` - Windows启动批处理文件
- `README.md` - 说明文档

## 环境变量说明

脚本使用以下环境变量（在 `startup.bat` 中设置）：

- `SENDER_EMAIL` - 发件人邮箱（必需）
- `SENDER_PASSWORD` - 邮箱SMTP授权码（必需）
- `SMTP_SERVER` - SMTP服务器（默认：smtp.qq.com）
- `SMTP_PORT` - SMTP端口（默认：587）

## 故障排除

### 邮件发送失败

1. 确认使用的是QQ邮箱的授权码，不是QQ密码
2. 确认已开启QQ邮箱的SMTP服务
3. 检查网络连接

### 无法获取IP

脚本会尝试两个不同的IP查询服务，如果都失败请检查网络连接。

### 开机不自动运行

1. 检查快捷方式路径是否正确
2. 确认 `startup.bat` 中的路径使用绝对路径
3. 查看任务计划程序中的任务历史记录

## 依赖项

- Python >= 3.8
- requests >= 2.31.0

依赖通过uv自动管理，无需手动安装。
