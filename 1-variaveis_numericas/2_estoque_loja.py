# Uma loja de eletrônicos vendeu dois lotes de fones de ouvido de uma vez. 
# O primeiro lote tinha 10 fones e cada um custou R$ 50. O segundo lote era maior, tinha 40 fones e cada um custou R$ 80. 
# O dono da loja quer saber o valor médio real que cada fone custou no estoque dele.

quantidade_fones_lote_1 = 10
quantidade_fones_lote_2 = 40
quantidade_total_fones = (quantidade_fones_lote_1 + quantidade_fones_lote_2)

valor_lote_1 = (quantidade_fones_lote_1 * 50)
valor_lote_2 = (quantidade_fones_lote_2 * 80)

media_real = (valor_lote_1 + valor_lote_2) / quantidade_total_fones

print(media_real)