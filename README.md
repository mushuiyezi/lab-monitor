# 实验室系统监控

这是一个用于监控实验室系统状态的简单 Python 项目。它会周期性采集 CPU 和内存使用率，并把结果写入日志文件，方便后续分析和展示。

## 1. 项目简介

这个项目的目标是：
- 采集系统的 CPU 和内存使用情况
- 将数据记录到日志文件中
- 便于后续做实验室环境监控、性能分析或演示

## 2. 快速开始（Conda 版）

### 2.1 创建并激活环境

```bash
conda env create -f environment.yml
conda activate lab-monitor
```

### 2.2 运行程序

```bash
python monitor.py
```

运行后会在项目目录下生成日志文件：

```bash
logs/system_stats.txt
```

### 2.3 导出环境清单

如果你修改了依赖，可以执行：

```bash
conda env export > environment.yml
```

## 3. 快速开始（Docker 版）

### 3.1 构建镜像

```bash
docker build -t lab-monitor:v1.0 .
```

### 3.2 运行容器

```bash
docker run --rm -v "${PWD}/logs:/app/logs" lab-monitor:v1.0
```

说明：
- `-v "${PWD}/logs:/app/logs"` 会把宿主机当前目录下的 `logs` 文件夹挂载到容器中的 `/app/logs`
- 这样即使容器被删除，日志仍然保存在宿主机上
- 你可以在宿主机上直接查看：

```bash
cat logs/system_stats.txt
```

## 4. Git 初始化与分支协作

### 4.1 初始化仓库

```bash
git init --initial-branch=master
git add .
git commit -m "Initial commit"
```

### 4.2 创建开发分支

```bash
git checkout -b dev-yourname
```

### 4.3 推送到 GitHub/Gitee

```bash
git remote add origin https://github.com/mushuiyezi/lab-monitor.git
git push -u origin master
git push -u origin dev-yourname
```

## 5. 依赖说明

项目依赖文件如下：
- [requirements.txt](requirements.txt)
- [environment.yml](environment.yml)

## 6. 目录说明

- [monitor.py](monitor.py)：主程序
- [Dockerfile](Dockerfile)：容器配置
- [logs/](logs)：运行后生成的日志目录
