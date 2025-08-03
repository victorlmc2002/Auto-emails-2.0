def formatar_texto_inquilino(devedor):
    partes = [f"Aluguel: R$ {devedor._aluguel:.2f}"]

    if not isinstance(devedor._iptu, str) and devedor._iptu is not None and devedor._iptu > 0:
        partes.append(f"IPTU: R$ {devedor._iptu:.2f}")
    if not isinstance(devedor._cond, str) and devedor._cond is not None and devedor._cond > 0:
        partes.append(f"Taxa de condomínio: R$ {devedor._cond:.2f}")
    if devedor._cotas_extras:
        partes.append("<br><b>Descontos/Reembolsos:<br></b>")
        for cota in devedor._cotas_extras:
            for chave, valor in cota.items():
                if valor > 0:
                    partes.append(f"{chave}: R$ {valor:.2f}")

    partes.append(f"<br><b>Valor do Boleto: R$ {devedor._valor:.2f}<br><br>Atenciosamente,<br>Vigor Negócios<br></b>")
    return "<br>".join(partes)

def formatar_texto_proprietario(devedor):
    partes = [f"Receita: R$ {devedor._valor:.2f}", "<br><b>Reembolso de Despesas:</b><br>"]

    if not isinstance(devedor._iptu, str) and devedor._iptu is not None and devedor._iptu > 0:
        partes.append(f"IPTU: R$ {devedor._iptu:.2f}")
    if not isinstance(devedor._cond, str) and devedor._cond is not None and devedor._cond > 0:
        partes.append(f"Taxa de condomínio: R$ {devedor._cond:.2f}")
    if not isinstance(devedor._taxa, str) and devedor._taxa is not None and devedor._taxa > 0:
        partes.append(f"Taxa de administração: R$ {devedor._taxa:.2f}")
    if not isinstance(devedor._tarifa, str) and devedor._tarifa is not None and devedor._tarifa > 0:
        partes.append(f"Tarifa de transferência: R$ {devedor._tarifa:.2f}")

    partes.append(f"<br><b>Valor do Repasse: R$ {devedor._repasse:.2f}</b>")
    return "<br>".join(partes)