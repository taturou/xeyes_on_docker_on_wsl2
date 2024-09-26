# これはなに

WSL2上のDockerコンテナで動いているxeysを、Windowsで表示する (GUI表示する)

# 使い方

## コンテナを起動

```sh
$ ./docker_up.sh
```

## コンテナのログを表示

```sh
$ ./docker_logs.sh
```

## コンテナを終了

```sh
$ ./docker_down.sh
```

## xeyesを表示

```sh
$ ./xeyes.sh
```

## turtleを表示する

```sh
$ ./turtle.sh
```

* 上キー: 前進
* 下キー: 後進
* 右キー: 右回転
* 左キー: 左回転
* 画面クリック: 終了

# 参考文献

【WSL 2】dockerコンテナでGUIアプリを実行してWindowsで表示させたい
https://dev.classmethod.jp/articles/wsl2-docker-gui-app-windows-display/?utm_source=pocket_saves

