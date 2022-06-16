lista=[]
lisnum=[]
lis=['a','b','c','d']
print('Bases disponíveis ')
print('octal')
print('decimal')
print('binário')
print('hexadecimal')
conv=str(input('Deseja fazer a conversão?(Sim/Não):')).lower()
if conv=='sim':
    BDO=str(input('Digite a base de origem:(de acordo com a forma escrita acima)'))
    BDD=str(input('Digite a base de destino:(de acordo com a forma escrita acima)'))
    if BDO=='decimal':
        NAC=int(input('Digite o número a ser convertido:'))
        if BDD=='octal':
            conver=oct(NAC)
            print(conver)
        elif BDD=='hexadecimal':
            conver=hex(NAC)
            print(conver)
        elif BDD=='binário':
            conver=bin(NAC)
            print(conver)
    if BDO=='octal':
        NAC=(input('Digite o número a ser convertido:'))
        if BDD=='decimal':
            for h in NAC:
                lista.append(h)
            lista.reverse()
            dec = 0
            for i in range(len(lista)):
                valor = 1
                for p in range(i):
                    valor *= 8
                valor *= int(lista[i])
                dec += valor
            print(dec)
    if BDO=='binário':
        NAC=(input('Digite o número a ser convertido:'))
        if BDD=='decimal':
          for h in NAC:
                lista.append(h)
          lista.reverse()
          dec = 0
          for i in range(len(lista)):
                valor = 1
                for p in range(i):
                    valor *= 2
                valor *= int(lista[i])
                dec += valor
          print(dec)
    if BDO=='hexadecimal':
      num=str(input('Digite o número a ser convertido:')).lower()
      if BDD=='decimal':
        a = 0
        for i in range(len(num)):
          if num[i].isdigit():
            a=int(num[i])
            lisnum.append(a)
          else:
            for p in range(len(lis)):
              if num[i] == lis[p]:
                a = p + 10
                lisnum.append(a)
        lisnum.reverse()
        nume=0
        for a in range(len(lisnum)):
          nume+=(lisnum[a]*(16**a))
        print(nume)
else:
  print('programa finalizado')