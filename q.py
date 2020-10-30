[33mcommit ebdef5645e0cf69613d48e63b6a2618d57f20dae[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: Mauro Interliche de Oliveira <interlich@gmail.com>
Date:   Wed Oct 28 13:35:18 2020 -0300

    teste com arquivo pyy

[1mdiff --git a/ListasParImpar.pyy b/ListasParImpar.pyy[m
[1mnew file mode 100644[m
[1mindex 0000000..b43a01b[m
[1m--- /dev/null[m
[1m+++ b/ListasParImpar.pyy[m
[36m@@ -0,0 +1,29 @@[m
[32m+[m[32m#exercício 85[m
[32m+[m
[32m+[m[32mvalor = 0[m
[32m+[m[32mvalores = list()[m
[32m+[m[32mpares = list()[m
[32m+[m[32mimpares = list()[m
[32m+[m[32mwhile True:[m
[32m+[m[32m    valor = int(input('Digite um número qualquer: '))[m
[32m+[m
[32m+[m[32m    if (valor % 2 == 0):[m
[32m+[m[32m        pares.append(valor)[m
[32m+[m[32m        valores.append((valor))[m
[32m+[m[41m        [m
[32m+[m[32m    else:[m
[32m+[m[32m        impares.append(valor)[m
[32m+[m[32m        valores.append(valor)[m
[32m+[m
[32m+[m[32m    resp = str(input('Quer sair? [S/N]'))[m
[32m+[m[32m    if resp == 'S':[m
[32m+[m[32m       break[m
[32m+[m
[32m+[m[32mvalores.sort()[m
[32m+[m[32mpares.sort()[m
[32m+[m[32mimpares.sort()[m
[32m+[m
[32m+[m[32mprint('=-' * 30)[m
[32m+[m[32mprint(f'A lista completa é {valores}')[m
[32m+[m[32mprint(f'A lista de pares é {pares}')[m
[32m+[m[32mprint(f'A lista de ímpares é {impares}')[m
