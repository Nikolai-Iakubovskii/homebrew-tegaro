# Homebrew tap for Tegaro

[Tegaro](https://tegaro.app/) is a native Swift and AppKit menu-bar app for macOS 13 or later,
on Apple silicon and Intel. It combines twelve tools in one app.

- Text and voice: [EN ↔ RU layout correction](https://tegaro.app/keyboard),
  [clipboard history](https://tegaro.app/clipboard), and [on-device dictation](https://tegaro.app/dictation).
- Capture: [screenshots and OCR](https://tegaro.app/screenshots), [screen recording](https://tegaro.app/video),
  and [bot-free meeting recording and local transcription](https://tegaro.app/meetings).
- System: [display controls](https://tegaro.app/displays), [battery and power](https://tegaro.app/power),
  [disk analysis and cleanup](https://tegaro.app/disk), [sound controls](https://tegaro.app/sound),
  [AI usage limits](https://tegaro.app/ai-usage), and [menu-bar critters](https://tegaro.app/critter).

Meetings requires macOS 14.2 or later and screen recording requires macOS 15 or later.
Optional AI features can send text to the provider you choose, with your permission.
See the [network and privacy details](https://tegaro.app/privacy).

```sh
brew install --cask nikolai-iakubovskii/tegaro/tegaro
```

The direct build includes a 14-day trial without a card or account. A Lifetime license is
$100 once for one person on up to two Macs. [Trial, Free and Pro details](https://tegaro.app/terms).

Tegaro updates itself after installation, so `brew upgrade` leaves it alone unless you pass
`--greedy`. `brew uninstall --zap tegaro` also removes its settings and downloaded dictation models.

The cask follows the app's own update feed: a workflow checks it every hour and moves the version
and checksum when a new build appears. Questions and problems: [tegaro.app/support](https://tegaro.app/support).

## По-русски

Tegaro объединяет 12 инструментов в строке меню. Работает на macOS 13 и новее на Apple silicon
и Intel. Запись встреч без бота требует macOS 14.2 или новее, запись экрана — macOS 15 или новее.

```sh
brew install --cask nikolai-iakubovskii/tegaro/tegaro
```

Ставит Tegaro с сайта, дальше приложение обновляется само. `brew uninstall --zap tegaro` удаляет
его вместе с настройками и скачанными моделями диктовки.

Первые 14 дней доступны все инструменты без карты и регистрации. Бессрочная лицензия стоит
$100 для одного человека на двух Mac. [Условия](https://tegaro.app/ru/terms) · [Приватность](https://tegaro.app/ru/privacy).
