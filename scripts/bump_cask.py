#!/usr/bin/env python3
"""Moves Casks/tegaro.rb to the newest build in Tegaro's Sparkle feed.

The feed is the app's own SUFeedURL, the one the cask's livecheck reads too. A build is taken only
when its DMG downloads at the length the feed advertises and hashes to the checksum the release
published beside it. The cask follows the feed both ways: a rolled-back release moves it back.
"""
import hashlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

FEED = "https://klavadabra.com/appcast.xml"
RELEASES = "https://releases.klavadabra.com"
SPARKLE = "{http://www.andymatuschak.org/xml-namespaces/sparkle}"
CASK = Path(__file__).resolve().parent.parent / "Casks" / "tegaro.rb"


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "homebrew-tegaro-bump"})
    return urllib.request.urlopen(request, timeout=120)


def newest_build():
    """(build, version, url, length) of the feed's newest default-channel item."""
    items = []
    for item in ET.fromstring(fetch(FEED).read()).iter("item"):
        if item.find(f"{SPARKLE}channel") is not None:
            continue  # beta channels are not for Homebrew
        enclosure = item.find("enclosure")
        build = item.findtext(f"{SPARKLE}version") or enclosure.get(f"{SPARKLE}version")
        version = item.findtext(f"{SPARKLE}shortVersionString") or enclosure.get(f"{SPARKLE}shortVersionString")
        items.append((int(build), version, enclosure.get("url"), int(enclosure.get("length"))))
    if not items:
        sys.exit("the feed has no items")
    return max(items)


def main():
    build, version, url, length = newest_build()
    text = CASK.read_text(encoding="utf-8")
    current = re.search(r'^  version "([^"]+)"$', text, re.M).group(1)
    if current == version:
        print(f"up to date: {version} (build {build})")
        return
    expected = f"{RELEASES}/Tegaro-{version}.dmg"
    if url != expected:
        sys.exit(f"the feed's DMG {url} is not the cask's URL {expected}")
    digest = hashlib.sha256()
    size = 0
    with fetch(url) as response:
        for chunk in iter(lambda: response.read(1 << 20), b""):
            digest.update(chunk)
            size += len(chunk)
    if size != length:
        sys.exit(f"downloaded {size} bytes, the feed says {length}")
    published = fetch(f"{RELEASES}/Tegaro-{version}.sha256").read().decode().split()[0]
    if digest.hexdigest() != published:
        sys.exit(f"the DMG hashes to {digest.hexdigest()}, the release published {published}")
    text = re.sub(r'^  version "[^"]+"$', f'  version "{version}"', text, count=1, flags=re.M)
    text = re.sub(r'^  sha256 "[0-9a-f]{64}"$', f'  sha256 "{published}"', text, count=1, flags=re.M)
    CASK.write_text(text, encoding="utf-8")
    print(f"moved {current} -> {version} (build {build})")


if __name__ == "__main__":
    main()
