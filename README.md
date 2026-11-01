# Homebrew tap for Tegaro

[Tegaro](https://tegaro.app) is a local-first menu-bar toolkit for the Mac: it fixes text typed in
the wrong EN ↔ RU layout, keeps clipboard history, dictates on device and adds display and power
tools.

```sh
brew install --cask nikolai-iakubovskii/tegaro/tegaro
```

Tegaro updates itself after installation, so `brew upgrade` leaves it alone unless you pass
`--greedy`. `brew uninstall --zap tegaro` also removes its settings and downloaded dictation models.

The cask follows the app's own update feed: a workflow checks it every hour and moves the version
and checksum when a new build appears. Questions and problems: [tegaro.app/support](https://tegaro.app/support).

## По-русски

```sh
brew install --cask nikolai-iakubovskii/tegaro/tegaro
```

Ставит Tegaro с сайта, дальше приложение обновляется само. `brew uninstall --zap tegaro` удаляет
его вместе с настройками и скачанными моделями диктовки.
