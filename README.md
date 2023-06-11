# 目录

- [目录](#目录)
- [版本更新](#版本更新)
- [pywxwork](#pywxwork)
- [企微python接口](#企微python接口)
- [框架结构](#框架结构)
  - [接口](#接口)
    - [接口列表](#接口列表)
- [how to use](#how-to-use)
    - [install pywxwork](#install-pywxwork)
    - [get token](#get-token)
    - [get user list](#get-user-list)


# 版本更新

| ver   | desc               | date     |
| ----- | ------------------ | -------- |
| 1.0.1 | 初始化 | 20230611 |

# pydingtalk

- python wxwork server api
- version==1.0.1


# dingding python接口

- 写一个企微的python库，开箱即用。
- 这个接口库完全用于企微的服务端接口。


# how to use
### install pywxwork
`pip install pydingtalk`

### get token

```python
from pydingtalk.token import token

data = {
	"appKey":"dingasdfasdfasdfasd",
	"appSecret":"asdfasdfasfadsfads"
}

t = token(**data)
logger.debug(t.token)
```