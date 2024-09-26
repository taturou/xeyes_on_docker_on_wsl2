# これはなに

WSL2上のDockerコンテナで動いているxeysなどを、Windowsで表示する (GUI表示する)

# 準備

1. WindowsにWSL2をインストールする
1. WSL2に適当なUbuntu 22.04をインストールする
1. Ubuntu 22.04にDockerをインストールする
1. Ubuntu 22.04上にこのリポジトリを git clone する

# 使い方

## コンテナ操作

### コンテナを起動

```sh
$ ./docker_up.sh
```

### コンテナのログを表示

```sh
$ ./docker_logs.sh
```

### コンテナを終了

```sh
$ ./docker_down.sh
```

## アプリケーション

### xeyesを表示

```sh
$ ./xeyes.sh
```

### turtleを表示する

```sh
$ ./turtle.sh
```

操作方法

* 上キー: 前進
* 下キー: 後進
* 右キー: 右回転
* 左キー: 左回転
* `c` キー: クリアー
* ウィンドウをクリック: 終了

# 参考文献

* [【WSL 2】dockerコンテナでGUIアプリを実行してWindowsで表示させたい](https://dev.classmethod.jp/articles/wsl2-docker-gui-app-windows-display/?utm_source=pocket_saves)

