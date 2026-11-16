cask "tegaro" do
  version "0.1.74"
  sha256 "c7caf7e701877c4eff40aaf0bb0795a653a38d76b0f81d491080db6d8c657cac"

  url "https://releases.klavadabra.com/Tegaro-#{version}.dmg"
  name "Tegaro"
  desc "Menu bar toolkit with keyboard layout fixer, clipboard history and dictation"
  homepage "https://tegaro.app/"

  # The app's own SUFeedURL; shipped builds poll this exact URL (docs/wiki/16-naming.md).
  livecheck do
    url "https://klavadabra.com/appcast.xml"
    strategy :sparkle, &:short_version
  end

  auto_updates true
  depends_on macos: :ventura

  app "Tegaro.app"

  # The bundle id and data folders keep the pre-rename Klavadabra names on purpose
  # (docs/wiki/16-naming.md). The launch-at-login agent goes only with zap: uninstall also
  # runs on `brew upgrade`, which must not switch launch at login off.
  uninstall quit: "com.klavadabra.menubar"

  zap trash: [
    "~/Library/Application Support/com.klavadabra.menubar",
    "~/Library/Application Support/Klavadabra",
    "~/Library/Caches/com.klavadabra.menubar",
    "~/Library/Caches/Klavadabra",
    "~/Library/HTTPStorages/com.klavadabra.menubar",
    "~/Library/HTTPStorages/com.klavadabra.menubar.binarycookies",
    "~/Library/LaunchAgents/com.klavadabra.menubar.plist",
    "~/Library/Preferences/com.klavadabra.menubar.plist",
    "~/Library/Saved Application State/com.klavadabra.menubar.savedState",
  ]
end
