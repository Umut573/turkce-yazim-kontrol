#!/bin/bash
echo "📱 Native Gradle Kurulumu Başlıyor..."

# Mimari Kontrolü
ARCH=$(uname -m)
if [[ "$ARCH" != "aarch64" && "$ARCH" != "arm64" ]]; then
    echo "❌ Bu araç şu an sadece ARM64 (Termux/Android) için optimize edilmiştir."
    exit 1
fi

# Gerekli paketleri kur
pkg update -y
pkg install proot-distro -y

# Alpine Linux üzerinden GLIBC desteği sağla (En hızlı ve hafif yol)
if ! proot-distro list | grep -q "alpine.*installed"; then
    echo "📦 Hafif çalışma ortamı kuruluyor (Alpine)..."
    proot-distro install alpine
fi

# Binary'yi sistem yoluna ekle
echo "⚙️ Yapılandırılıyor..."
proot-distro login alpine -- bash -c "apk add --no-cache gcompat libc6-compat"

echo "✅ Kurulum tamamlandı!"
echo "🚀 Artık 'gradle-native' komutunu kullanabilirsiniz."
