import click
from turkyazim.turkyazim import TurkceYazim


@click.command()
@click.argument("metin", type=str)
@click.option("--rapor", is_flag=True, help="Detaylı rapor göster.")
@click.option("--duzelt", is_flag=True, help="Düzeltme yap.")
@click.option("--ekle", help="Özel kelime ekle.")
def main(metin, rapor, duzelt, ekle):
    yazim = TurkceYazim()

    if ekle:
        yazim.ozel_kelime_ekle(ekle)
        click.echo(f"'{ekle}' kelimesi özel sözlüğe eklendi.")

    if rapor:
        sonuc = yazim.raporla(metin)
        click.echo("Orijinal Metin:\n" + sonuc["orijinal_metin"])
        click.echo("\nDüzeltilmiş Metin:\n" + sonuc["duzeltilmis_metin"])
        click.echo("\nHatalar:")
        for hata in sonuc["hatalar"]:
            click.echo(f"{hata['kelime']} → {', '.join(hata['oneriler'])}")
    elif duzelt:
        sonuc = yazim.duzelt(metin)
        click.echo("Düzeltilmiş Metin:\n" + sonuc)
    else:
        click.echo("Lütfen --rapor veya --duzelt seçeneğini kullanın.")


if __name__ == "__main__":
    main()
