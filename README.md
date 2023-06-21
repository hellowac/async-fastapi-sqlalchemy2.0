# 使用 FastAPI + SQLAlchemy 2.0 的异步webAPI

## 安装

```shell
# 准备虚拟环境
$ python3 -m venv venv
# 激活虚拟环境
$ . venv/bin/activate
(venv) $ pip install -r requirements.lock
```

## 使用数据库以及创建表

```shell
(venv) $ APP_CONFIG_FILE=local alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> a8483365f505, initial_empty
INFO  [alembic.runtime.migration] Running upgrade a8483365f505 -> 24104b6e1e0c, add_tables
```

## 运行

```shell
(venv) $ APP_CONFIG_FILE=local uvicorn app.main:app --host "0.0.0.0" --port 8000  --reload --reload-dir app
INFO:     Will watch for changes in these directories: ['/Users/rhoboro/go/src/github.com/rhoboro/async-fastapi-sqlalchemy/app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [49448] using WatchFiles
INFO:     Started server process [49450]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

现在可以访问 [localhost:8000/docs](http://localhost:8000/docs) 查看API文档

## 测试

```shell
(venv) $ pip install -r requirements_test.txt
(venv) $ black app
(venv) $ ruff app
(venv) $ mypy app
# 禁用警告
(venv) $ pytest app  --disable-warnings --log-format="[%(asctime)s] - %(pathname)s:%(lineno)d %(message)s"
```
