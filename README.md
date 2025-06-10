# 🛠️ Tools API

一组常用字符串/时间处理工具的 API 服务，基于 Flask 构建，支持 Docker 多平台部署（`amd64` + `arm64`），可作为 WordPress 等前端系统的后端接口。

---

## ✨ 功能列表

- `quote` / `unquote`: URL 编码与解码
- `remove_extra_spaces`: 删除多余空格
- `remove_whitespace`: 移除所有空白字符
- `base64_encode` / `base64_decode`: Base64 编码与解码
- `url_encode` / `url_decode`: URL 编码与解码
- `timestamp_to_mst`: Unix 时间戳 转 MST 时区时间
- `mst_to_timestamp`: MST 时间 转 Unix 时间戳

---

## 🐳 Docker 使用

```bash
# 构建本地镜像
docker build -t tools-api .

# 启动容器
docker run -d -p 5000:5000 tools-api
