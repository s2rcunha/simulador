# Remonta esquema.html com os SVGs de assets/2d embutidos (rode depois de ferramentas/gera2d.py).
import json, os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
c=json.load(open(os.path.join(R,'assets','2d','catalogo.json'),encoding='utf-8'))
for it in c['itens']+c['fundos']: it['svg']=open(os.path.join(R,it['arquivo']),encoding='utf-8').read()
t=open(os.path.join(R,'ferramentas','esquema_modelo.html'),encoding='utf-8').read().replace('/*CATALOGO*/null',json.dumps(c,ensure_ascii=False))
open(os.path.join(R,'esquema.html'),'w',encoding='utf-8').write(t); print('esquema.html atualizado')
