moedeiro = {'2e': 0,
			'1e': 0,
			'50c': 0,
			'20c': 0,
			'10c': 0,
			'5c': 0,
		}

deep = {}

for chave, valor in moedeiro.items():
	deep[chave] = valor

moedeiro['2e'] = 3
moedeiro.pop ('1e')
print (moedeiro)

print (deep)

