# 🚀 Native Gradle Fast-Launcher (Multi-Arch)

![Termux Support](https://img.shields.io/badge/Termux-Supported-folly?style=for-the-badge&logo=android)
![Speed](https://img.shields.io/badge/Speed-Cold_Start_0.07s-green?style=for-the-badge)

Java'nın hantallığını geride bırakın. Bu proje, Gradle'ın **GraalVM AOT** ile derlenmiş sürümlerini sunar.

## ⚡ Neden Bu Proje?
Termux'ta standart `gradle` komutu Java VM'in ayağa kalkması nedeniyle çok yavaştır. Bu native binary, Java'ya ihtiyaç duymadan (veya çok az duyarak) anında tetiklenir.

## 📱 Termux Kurulumu (Hızlı Yol)
Termux içindeyken şu komutu kopyalayıp yapıştırın:
```bash
curl -sSL https://raw.githubusercontent.com/Umut573/Native-Gradle-Fast-Launcher/main/install.sh | bash
```

## 🏗️ Manuel Kullanım
Eğer manuel çalıştırmak isterseniz:
1. `bin/arm64/gradle-arm64` dosyasını indirin.
2. `chmod +x` ile izin verin.
3. GLIBC uyumluluğu için `gcompat` yüklü bir proot ortamında çalıştırın.

## 📊 Performans
| Ortam | Standart | Native |
| :--- | :--- | :--- |
| **Android (Termux)** | 6.5s | **0.2s** |
| **Linux (x86)** | 4.2s | **0.08s** |

---
*Created by Umut573*
