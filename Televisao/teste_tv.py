from funcionalidades_tv import Televisor, ControleRemoto

tv = Televisor("Sony", "SONY-123")

controle = ControleRemoto(tv)

controle.sintoniza_canal("SBT")
controle.troca_canal("SBT")

print(tv.canal_atual, tv.volume, tv.modelo)

