from blueqat import Circuit

c = Circuit().h[0].cx[0,1].m[:].run(shots=100)
# cx[0,1] で量子ビット0をコントロールビット
#   量子ビット1をターゲットビットとして
#   CXゲート(CNOTゲート)を設置する
# CNOTゲートは，コントロールビットが1のとき
#   ターゲットビットを反転する
# 量子ビット1の初期値は0なので
#   量子ビット0と量子ビット1の値は等しくなる(量子もつれ)

print(c)
# Counter({'11': 51, '00': 49})
# '00'と'11'がおよそ50回ずつ観測できる