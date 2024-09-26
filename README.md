# これはなに

WSL2上のDockerコンテナで動いているxeysを、Windowsで表示する (GUI表示する)

# 使い方

コンテナを起動

```sh
$ ./docker_up.sh
```

コンテナのログを表示

```sh
$ ./docker_logs.sh
```

コンテナを終了

```sh
$ ./docker_down.sh
```

xeyesを表示

```sh
$ ./xeyes.sh
```

PythonでturtleのScrenを表示する

```sh
$ ./bash.sh
root@0f29c8375e34:/usr/src# python3 ./screen.py
```

# 参考文献

【WSL 2】dockerコンテナでGUIアプリを実行してWindowsで表示させたい
https://dev.classmethod.jp/articles/wsl2-docker-gui-app-windows-display/?utm_source=pocket_saves

