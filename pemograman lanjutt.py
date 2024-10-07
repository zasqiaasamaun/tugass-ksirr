def hitung_harga_boneka(jumlah_boneka):
  """Fungsi untuk menghitung total harga boneka berdasarkan jumlah pembelian.

  Args:
    jumlah_boneka: Jumlah boneka yang dibeli.

  Returns:
    Total harga boneka.
  """

  if jumlah_boneka <= 12:
    harga_per_boneka = 20000
  elif 13 <= jumlah_boneka <= 24:
    harga_per_boneka = 19500
  elif 25 <= jumlah_boneka <= 50:
    harga_per_boneka = 18000
  else:
    harga_per_boneka = 17000

  total_harga = jumlah_boneka * harga_per_boneka
  return total_harga

# Contoh penggunaan:
jumlah_boneka_dibeli = int(input("Masukkan jumlah boneka yang dibeli: "))
total_harga = hitung_harga_boneka(jumlah_boneka_dibeli)

print("Total harga yang harus dibayar: Rp.", total_harga)