import shutil
from func import *
from param import *
from param import pct_re as re
from param import pct_pc as pc
from param import parametros as pr
from func import resultado as rs


def rodar(val_especifico, val_excec):
    result = rs.Resultado()

    # Teste de Prestação de Contas
    if val_especifico['Pacote'] == 'PC':
        pct_raiz = pct_pc.montar(val_especifico)
        pacote.testar(pct_raiz, result)

        for tipo in pct_raiz.lst_tp_arq:

            val_especifico_sub = val_especifico.copy()
            val_especifico_sub['Local Arquivos'] = val_especifico_sub['Local Arquivos'] + tipo

            if tipo == 'Candidatos':
                pct = pc.montar_cand(val_especifico_sub)
                pacote.testar(pct, result)
                arquivos.testar(pct, val_excec, result)
                try:
                    shutil.rmtree(pct.loc_arq)
                except FileNotFoundError:
                    pass

            elif tipo == 'Órgãos Partidários':
                pct = pc.montar_op(val_especifico_sub)
                pacote.testar(pct, result)
                arquivos.testar(pct, val_excec, result)
                try:
                    shutil.rmtree(pct.loc_arq)
                except FileNotFoundError:
                    pass

    # Teste de Resultado da Eleição
    elif val_especifico['Pacote'] == 'RE':
        pct_raiz = pct_re.montar(val_especifico)
        pacote.testar(pct_raiz, result)

        lst_arq_val = []
        lst_arq_val_tmp = [a for a in pct_raiz.lst_arq_esp if a in pct_raiz.lst_arq]
        for arq_val in lst_arq_val_tmp:
            lst_arq_val.append(arq_val.rsplit('_' + val_especifico['Ano'], 1)[0])

        for tipo in lst_arq_val:
            if tipo == 'votacao_secao':
                pct_vs = re.montar_votacao_secao(val_especifico)
                pacote.testar(pct_vs, result)

                for arq in pct_vs.lst_arq_esp:
                    sub_pct = 'votacao_secao/' + arq.split('.', 1)[0]
                    lst_arq_val.append(sub_pct)

            else:
                val_especifico_sub = val_especifico.copy()
                val_especifico_sub['Local Arquivos'] = val_especifico_sub['Local Arquivos'] + tipo

                tp_eleicao = pr.get_tp_eleicao(val_especifico_sub['Ano'])
                lst_arq_esp = re.get_lst_arq_esp(val_especifico_sub['Ano'], [tipo], tp_eleicao)

                pct = pr.ParamPac(val_especifico_sub, tipo, tp_eleicao, lst_arq_esp)
                pct.unzip = True
                pct = re.set_var_lst_arq(pct)

                pacote.testar(pct, result)
                arquivos.testar(pct, val_excec, result)

                # Apagando pasta descompactada
                try:
                    shutil.rmtree(pct.loc_arq)

                except FileNotFoundError as e:
                    pass

        # Testar relac\
        # relacao.testar(result)

    return result
