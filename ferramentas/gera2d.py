import json, os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','2d')
os.makedirs(OUT,exist_ok=True)
K='#1d2733'  # contorno
C={'agua':('#2f7fc8','#d4e9fb'),'lge':('#c99400','#fff0bf'),'ar':('#5f6f80','#e4e9ef'),'ele':('#d9661e','#ffe4d1'),'bomba':('#c62828','#f7d3d3'),'metal':('#5b6470','#dfe3e8'),'tubo':('#2f7fc8','#a9d1f5'),'cena':('#3c7d3a','#d9efd5')}
def svg(vb,corpo,titulo):
    w,h=vb
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><title>{titulo}</title><g stroke="{K}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">{corpo}</g></svg>\n'
def flange(x,y,vert=False,r=None):
    return f'<rect x="{x-3}" y="{y-9}" width="6" height="18" rx="1.5" fill="#9aa4b0"/>' if not vert else f'<rect x="{x-9}" y="{y-3}" width="18" height="6" rx="1.5" fill="#9aa4b0"/>'
def borboleta(cor,atuador=True,rot=''):
    s,f=C[cor]
    b=f'<rect x="4" y="52" width="92" height="22" rx="4" fill="{C["tubo"][1]}"/>'+flange(30,63)+flange(70,63)
    b+=f'<circle cx="50" cy="63" r="15" fill="#fff"/><line x1="40" y1="73" x2="60" y2="53" stroke-width="4"/>'
    if atuador:
        b+=f'<rect x="36" y="40" width="28" height="9" fill="#9aa4b0"/><rect x="22" y="10" width="56" height="30" rx="5" fill="{f}" stroke="{s}"/>'
        b+=f'<text x="50" y="30" font-family="Arial" font-size="9" font-weight="700" fill="{s}" stroke="none" text-anchor="middle">{rot}</text>'
        b+=f'<circle cx="30" cy="16" r="3" fill="{s}" stroke="none"/><circle cx="70" cy="16" r="3" fill="{s}" stroke="none"/>'
    return b
I=[]
def add(id,nome,cat,vb,corpo,larg,desc):
    open(f'{OUT}/{id}.svg','w').write(svg(vb,corpo,nome))
    I.append({'id':id,'nome':nome,'categoria':cat,'arquivo':f'assets/2d/{id}.svg','largura':larg,'descricao':desc,'proporcao':round(vb[1]/vb[0],4),'vb':list(vb)})
a,af=C['agua']; l,lf=C['lge']; ar,arf=C['ar']; e,ef=C['ele']; bo,bof=C['bomba']; m,mf=C['metal']; t,tf=C['tubo']; g,gf=C['cena']
# ---------------- reservatorios ----------------
add('tanque_agua','Tanque de água (6100 L)','Reservatórios',(200,120),
 f'<rect x="6" y="14" width="188" height="96" rx="12" fill="{af}" stroke="{a}" stroke-width="3"/>'
 f'<path d="M8 58 Q50 50 100 58 T192 58 V98 Q192 108 182 108 H18 Q8 108 8 98 Z" fill="#7fb9ea" stroke="none" opacity=".9"/>'
 f'<rect x="80" y="4" width="40" height="12" rx="3" fill="#9aa4b0"/><text x="100" y="44" font-family="Arial" font-size="18" font-weight="700" fill="{a}" stroke="none" text-anchor="middle">ÁGUA</text>'
 f'<rect x="92" y="108" width="16" height="10" fill="#9aa4b0"/>'
 f'<rect x="0" y="89" width="9" height="14" rx="2" fill="#9aa4b0"/><rect x="191" y="89" width="9" height="14" rx="2" fill="#9aa4b0"/>',290,'Reservatório principal de polipropileno. Saída embaixo; entradas na tampa e nas duas laterais (abastecimento por pressão e retorno bomba-tanque).')
add('tanque_lge','Tanque de LGE (860 L)','Reservatórios',(120,120),
 f'<rect x="6" y="14" width="108" height="96" rx="10" fill="{lf}" stroke="{l}" stroke-width="3"/>'
 f'<path d="M8 64 Q36 58 60 64 T112 64 V98 Q112 108 102 108 H18 Q8 108 8 98 Z" fill="#f4cf55" stroke="none"/>'
 f'<rect x="44" y="4" width="32" height="12" rx="3" fill="#9aa4b0"/><text x="60" y="48" font-family="Arial" font-size="18" font-weight="700" fill="{l}" stroke="none" text-anchor="middle">LGE</text>'
 f'<rect x="52" y="108" width="16" height="10" fill="#9aa4b0"/>',85,'Reservatório do líquido gerador de espuma.')
# ---------------- bomba e acionamento ----------------
add('bomba_incendio','Bomba de incêndio','Bomba e acionamento',(120,120),
 f'<rect x="8" y="50" width="24" height="20" fill="{tf}"/><rect x="88" y="10" width="20" height="26" fill="{tf}"/>'
 f'<circle cx="60" cy="60" r="38" fill="{bof}" stroke="{bo}" stroke-width="3"/><circle cx="60" cy="60" r="12" fill="#fff"/>'
 f'<path d="M60 60 L60 28 M60 60 L88 76 M60 60 L32 76" stroke="{bo}" stroke-width="5"/><circle cx="60" cy="60" r="5" fill="{K}"/>'
 f'<rect x="54" y="98" width="12" height="16" fill="#9aa4b0"/>',55,'Bomba centrífuga: sucção à esquerda, recalque em cima.')
add('pto_cardan','PTO e cardan','Bomba e acionamento',(200,70),
 f'<rect x="6" y="14" width="42" height="42" rx="6" fill="{mf}" stroke="{m}" stroke-width="3"/><text x="27" y="40" font-family="Arial" font-size="13" font-weight="700" fill="{m}" stroke="none" text-anchor="middle">PTO</text>'
 f'<rect x="48" y="28" width="104" height="14" rx="3" fill="#b9c1ca"/><path d="M60 28v14M140 28v14" />'
 f'<circle cx="60" cy="35" r="10" fill="#fff"/><circle cx="140" cy="35" r="10" fill="#fff"/><rect x="152" y="24" width="42" height="22" rx="4" fill="#9aa4b0"/>',85,'Tomada de força e eixo cardan até a bomba.')
add('bomba_escorva','Bomba de escorva','Bomba e acionamento',(100,100),
 f'<rect x="10" y="30" width="56" height="44" rx="6" fill="{mf}" stroke="{m}" stroke-width="3"/><rect x="66" y="40" width="26" height="24" rx="4" fill="{ef}" stroke="{e}"/>'
 f'<path d="M24 52h28M38 40v24" stroke="{m}" stroke-width="3"/><path d="M78 46l-4 6h6l-4 6" stroke="{e}" fill="none"/>'
 f'<rect x="30" y="74" width="14" height="18" fill="{tf}"/><text x="38" y="22" font-family="Arial" font-size="11" font-weight="700" fill="{m}" stroke="none" text-anchor="middle">VÁCUO</text>',45,'Retira o ar da sucção (máx. 30 s).')
add('bypass','Bypass / regulador de pressão','Bomba e acionamento',(80,110),
 f'<rect x="28" y="4" width="24" height="102" rx="3" fill="{tf}"/><circle cx="40" cy="55" r="20" fill="#fff"/><path d="M40 35v40M30 45l10-10 10 10" stroke="{bo}" stroke-width="3" fill="none"/>'
 f'<path d="M58 40 q10 4 0 8 q-10 4 0 8 q10 4 0 8 q-10 4 0 8" fill="none" stroke="{m}"/>',30,'Recircula água quando as expedições fecham.')
add('ada_proporcionador','Sistema ADA (proporcionador)','Espuma',(110,140),
 f'<rect x="38" y="4" width="34" height="132" rx="6" fill="{tf}"/><path d="M42 50 L55 70 L68 50 Z M42 100 L55 80 L68 100 Z" fill="#fff"/>'
 f'<rect x="72" y="64" width="34" height="12" fill="{lf}" stroke="{l}"/><text x="18" y="74" font-family="Arial" font-size="12" font-weight="700" fill="{l}" stroke="none" text-anchor="middle">ADA</text>',40,'Venturi que aspira o LGE para a sucção.')
add('dosador','Dosador de LGE (3 / 6 %)','Espuma',(90,100),
 f'<circle cx="45" cy="44" r="30" fill="{lf}" stroke="{l}" stroke-width="3"/><path d="M45 44 L65 27" stroke="{K}" stroke-width="6"/><circle cx="45" cy="44" r="6" fill="{K}"/>'
 f'<text x="14" y="94" font-family="Arial" font-size="13" font-weight="700" fill="{K}" stroke="none">3%</text><text x="54" y="94" font-family="Arial" font-size="13" font-weight="700" fill="{K}" stroke="none">6%</text>',22,'Alavanca de dosagem 3 % / 6 %.')
add('valvula_lge','Válvula de LGE (pneumática)','Espuma',(100,110),
 f'<rect x="4" y="66" width="92" height="20" rx="4" fill="{lf}"/><rect x="30" y="56" width="40" height="40" rx="6" fill="#fff"/>'
 f'<rect x="38" y="16" width="24" height="40" rx="4" fill="{arf}" stroke="{ar}"/><path d="M62 30 L88 12" stroke="{K}" stroke-width="5"/><circle cx="62" cy="30" r="4" fill="{K}"/>',30,'Libera o LGE para o ADA (solenoide 2).')
# ---------------- valvulas ----------------
add('valvula_borboleta_pneu','Válvula borboleta com atuador','Válvulas',(100,80),borboleta('ar',True,'ATUADOR'),40,'Tanque-bomba, bomba-tanque, canhões e dispersador.')
add('valvula_borboleta_manual','Válvula borboleta manual','Válvulas',(100,80),
 f'<rect x="4" y="52" width="92" height="22" rx="4" fill="{tf}"/>'+flange(30,63)+flange(70,63)+'<circle cx="50" cy="63" r="15" fill="#fff"/><line x1="40" y1="73" x2="60" y2="53" stroke-width="4"/>'
 f'<rect x="46" y="30" width="8" height="18" fill="#9aa4b0"/><rect x="20" y="22" width="60" height="10" rx="5" fill="{bof}" stroke="{bo}"/>',36,'Borboleta de alavanca.')
add('valvula_esferica','Válvula esférica com alavanca','Válvulas',(100,80),
 f'<rect x="4" y="50" width="92" height="22" rx="4" fill="{tf}"/><circle cx="50" cy="61" r="18" fill="#e9edf1" stroke="{m}" stroke-width="3"/><circle cx="50" cy="61" r="7" fill="#fff"/>'
 f'<rect x="47" y="26" width="6" height="18" fill="#9aa4b0"/><rect x="47" y="20" width="48" height="10" rx="5" fill="#d32f2f"/>',32,'Sucção, expedições, admissão e mangotinho.')
add('junta_expansao','Junta de expansão','Válvulas',(100,70),
 f'<rect x="4" y="24" width="20" height="22" fill="{tf}"/><rect x="76" y="24" width="20" height="22" fill="{tf}"/>'+flange(24,35)+flange(76,35)+
 f'<path d="M27 20 Q35 35 27 50 H73 Q65 35 73 20 Z" fill="#3a3f46"/><path d="M38 22v26M50 22v26M62 22v26" stroke="#7b838c"/>',30,'Rompe acima de 15 bar.')
add('valvula_retencao','Válvula de retenção','Válvulas',(100,70),
 f'<rect x="4" y="24" width="92" height="22" rx="4" fill="{tf}"/><circle cx="50" cy="35" r="18" fill="#fff"/><path d="M40 25 L62 35 L40 45 Z" fill="{K}"/>',30,'Deixa passar num só sentido.')
# ---------------- pneumatica ----------------
add('solenoide_52','Válvula solenoide 5/2 vias','Pneumática',(110,100),
 f'<rect x="8" y="34" width="70" height="38" rx="4" fill="{arf}" stroke="{ar}" stroke-width="3"/><rect x="78" y="38" width="26" height="30" rx="4" fill="{ef}" stroke="{e}"/>'
 f'<path d="M84 44 l8 0 l-8 18 l8 0" fill="none" stroke="{e}"/><circle cx="16" cy="53" r="6" fill="#2b6fd6" stroke="none"/>'
 f'<rect x="22" y="22" width="10" height="12" fill="#3fa34d"/><rect x="50" y="22" width="10" height="12" fill="#3fa34d"/><text x="27" y="17" font-family="Arial" font-size="11" font-weight="700" fill="{K}" stroke="none" text-anchor="middle">A</text><text x="55" y="17" font-family="Arial" font-size="11" font-weight="700" fill="{K}" stroke="none" text-anchor="middle">B</text>'
 f'<rect x="38" y="72" width="10" height="14" fill="#9aa4b0"/><text x="43" y="98" font-family="Arial" font-size="10" font-weight="700" fill="{K}" stroke="none" text-anchor="middle">P</text>',30,'Comanda um atuador (saídas A e B, botão manual azul).')
add('painel_solenoides','Painel de solenoides','Pneumática',(220,100),
 ''.join(f'<rect x="{10+i*35}" y="30" width="28" height="46" rx="3" fill="{arf}" stroke="{ar}"/><rect x="{14+i*35}" y="22" width="8" height="8" fill="#3fa34d"/><rect x="{24+i*35}" y="22" width="8" height="8" fill="#3fa34d"/><text x="{24+i*35}" y="60" font-family="Arial" font-size="13" font-weight="700" fill="{K}" stroke="none" text-anchor="middle">{i+1}</text>' for i in range(6))+
 f'<rect x="4" y="80" width="212" height="10" rx="3" fill="#9aa4b0"/>',120,'Solenoides 1 a 6 alimentados em série.')
add('lubrifil','Lubrifil (filtro, regulador, lubrificador)','Pneumática',(110,120),
 f'<rect x="4" y="18" width="102" height="14" rx="3" fill="#9aa4b0"/>'
 f'<path d="M14 32 h26 v46 q-13 18 -26 0 Z" fill="#dfeef8" stroke="{ar}"/><path d="M70 32 h26 v46 q-13 18 -26 0 Z" fill="#fff2c9" stroke="{l}"/>'
 f'<circle cx="55" cy="58" r="13" fill="#fff"/><path d="M55 58 L62 50" stroke="{bo}" stroke-width="3"/><rect x="47" y="4" width="16" height="14" rx="3" fill="{K}"/>',35,'Filtra, regula e lubrifica o ar.')
add('compressor','Compressor e reservatório de ar','Pneumática',(160,100),
 f'<rect x="10" y="40" width="140" height="44" rx="22" fill="#2a2f36"/><rect x="40" y="16" width="44" height="26" rx="4" fill="{mf}" stroke="{m}"/>'
 f'<circle cx="112" cy="28" r="12" fill="#fff"/><path d="M112 28 L118 22" stroke="{bo}" stroke-width="3"/><rect x="74" y="84" width="10" height="10" fill="#d9a441"/>',60,'Carrega o reservatório (até 8 bar) com o motor ligado.')
add('mangueira_ar','Mangueira de ar (6 mm)','Pneumática',(160,60),
 f'<path d="M14 40 C50 0 110 60 146 20" fill="none" stroke="#2f9e44" stroke-width="7"/><path d="M14 40 C50 0 110 60 146 20" fill="none" stroke="{K}" stroke-width="1"/>'
 f'<rect x="4" y="34" width="14" height="12" rx="2" fill="#d9a441"/><rect x="142" y="14" width="14" height="12" rx="2" fill="#d9a441"/>',60,'Liga solenoide e atuador.')
add('atuador_pneumatico','Atuador pneumático (dupla ação)','Pneumática',(120,80),
 f'<rect x="10" y="16" width="100" height="48" rx="8" fill="{arf}" stroke="{ar}" stroke-width="3"/><rect x="52" y="20" width="10" height="40" fill="#9aa4b0"/>'
 f'<text x="30" y="46" font-family="Arial" font-size="14" font-weight="700" fill="{K}" stroke="none" text-anchor="middle">A</text><text x="88" y="46" font-family="Arial" font-size="14" font-weight="700" fill="{K}" stroke="none" text-anchor="middle">B</text>'
 f'<rect x="22" y="6" width="12" height="10" fill="#3fa34d"/><rect x="82" y="6" width="12" height="10" fill="#3fa34d"/><rect x="52" y="64" width="12" height="12" fill="#9aa4b0"/>',30,'Porta A abre, porta B fecha.')
# ---------------- comandos ----------------
add('painel_central','Painel de comando central','Comandos',(160,130),
 f'<rect x="6" y="6" width="148" height="118" rx="8" fill="#2c333c"/><circle cx="40" cy="38" r="18" fill="#fff"/><circle cx="84" cy="38" r="18" fill="#fff"/>'
 f'<path d="M40 38 L50 28M84 38 L76 26" stroke="{bo}" stroke-width="3"/>'
 +''.join(f'<circle cx="{28+i*26}" cy="84" r="9" fill="#cfd5dc"/><path d="M{28+i*26} 84 l0 -8" stroke="{K}" stroke-width="3"/>' for i in range(5))+
 ''.join(f'<rect x="{120}" y="{20+i*10}" width="22" height="7" rx="2" fill="{["#3fa34d","#3fa34d","#3fa34d","#f2b705","#d32f2f"][i]}" stroke="none"/>' for i in range(5))+
 f'<rect x="22" y="104" width="116" height="10" rx="3" fill="#d32f2f" stroke="none"/>',55,'Chave geral, chaves rotativas, manômetro, vacuômetro e níveis.')
add('painel_cabine','Painel da cabine (PTO e acelerador)','Comandos',(110,90),
 f'<rect x="6" y="6" width="98" height="78" rx="8" fill="#2c333c"/><rect x="18" y="20" width="26" height="40" rx="4" fill="#d32f2f"/><text x="31" y="74" font-family="Arial" font-size="11" font-weight="700" fill="#fff" stroke="none" text-anchor="middle">PTO</text>'
 f'<circle cx="76" cy="40" r="18" fill="#fff"/><path d="M76 40 L86 30" stroke="{bo}" stroke-width="3"/><text x="76" y="74" font-family="Arial" font-size="10" font-weight="700" fill="#fff" stroke="none" text-anchor="middle">ACEL.</text>',35,'Engate do PTO e acelerador.')
add('joystick','Joystick do canhão','Comandos',(80,110),
 f'<rect x="10" y="80" width="60" height="22" rx="6" fill="#2c333c"/><path d="M40 82 L40 40" stroke="{K}" stroke-width="8"/><ellipse cx="40" cy="30" rx="14" ry="20" fill="#3b424b"/><circle cx="34" cy="20" r="5" fill="#d32f2f" stroke="none"/>',22,'Comanda o canhão (botão esquerdo).')
add('painel_parachoque','Painel do canhão de para-choque','Comandos',(110,80),
 f'<rect x="6" y="6" width="98" height="68" rx="8" fill="#2c333c"/><rect x="18" y="20" width="30" height="34" rx="4" fill="#d32f2f" opacity=".85"/><circle cx="33" cy="37" r="7" fill="#cfd5dc"/>'
 f'<circle cx="66" cy="28" r="6" fill="#3fa34d" stroke="none"/><path d="M84 60 L84 34" stroke="#cfd5dc" stroke-width="6"/><circle cx="84" cy="30" r="7" fill="#3b424b"/>',30,'Chave sob proteção, luz e joystick.')
add('bomba_eletrica','Bomba elétrica (inundador)','Comandos',(110,80),
 f'<rect x="8" y="22" width="60" height="40" rx="8" fill="{ef}" stroke="{e}" stroke-width="3"/><circle cx="84" cy="42" r="18" fill="{af}" stroke="{a}" stroke-width="3"/>'
 f'<path d="M30 30l-6 12h10l-6 12" stroke="{e}" fill="none" stroke-width="3"/><rect x="96" y="20" width="10" height="12" fill="{tf}"/>',22,'Bomba 24 V que alimenta o inundador.')
# ---------------- expedicao ----------------
add('canhao_teto','Canhão de teto (monitor)','Expedições',(150,120),
 f'<rect x="58" y="86" width="34" height="30" fill="{tf}"/><path d="M50 90 Q75 60 100 90" fill="#cfd5dc" stroke="{m}" stroke-width="3"/>'
 f'<path d="M66 70 L120 30 L132 44 L80 82 Z" fill="#d32f2f"/><rect x="118" y="26" width="26" height="22" rx="4" transform="rotate(-36 131 37)" fill="#9aa4b0"/>',50,'3000 L/min, alcance ~70 m.')
add('canhao_parachoque','Canhão de para-choque','Expedições',(130,100),
 f'<rect x="46" y="70" width="30" height="26" fill="{tf}"/><path d="M40 74 Q61 50 82 74" fill="#cfd5dc" stroke="{m}" stroke-width="3"/>'
 f'<path d="M54 60 L104 40 L110 54 L62 70 Z" fill="#d32f2f"/><rect x="102" y="36" width="22" height="18" rx="4" transform="rotate(-22 113 45)" fill="#9aa4b0"/>',40,'950 L/min, alcance 50 m.')
add('expedicao_storz','Expedição 2½" com storz','Expedições',(110,80),
 f'<rect x="4" y="30" width="56" height="22" fill="{tf}"/><rect x="58" y="20" width="22" height="42" rx="4" fill="#c9cfd6" stroke="{m}" stroke-width="3"/>'
 f'<path d="M80 26 h14 v10 h10 v10 h-10 v10 h-14 Z" fill="#b8bfc7"/><rect x="20" y="8" width="6" height="22" fill="#9aa4b0"/><rect x="20" y="4" width="34" height="9" rx="4" fill="#d32f2f"/>',30,'Válvula esférica + engate storz.')
add('rolo_mangueira','Rolo de mangueira (15 m)','Expedições',(100,100),
 f'<circle cx="50" cy="50" r="44" fill="#e9edf1" stroke="{m}" stroke-width="3"/>'+''.join(f'<circle cx="50" cy="50" r="{r}" fill="none" stroke="#c8ced6" stroke-width="5"/>' for r in (36,28,20))+f'<circle cx="50" cy="50" r="10" fill="#9aa4b0"/>',35,'Linha de 2½" enrolada.')
add('carretel_mangotinho','Carretel de mangotinho (1" x 30 m)','Expedições',(130,110),
 f'<rect x="10" y="96" width="110" height="10" rx="3" fill="#9aa4b0"/><circle cx="65" cy="52" r="42" fill="#d32f2f"/><circle cx="65" cy="52" r="30" fill="none" stroke="#f6d0d0" stroke-width="6"/>'
 f'<circle cx="65" cy="52" r="10" fill="#cfd5dc"/><rect x="2" y="44" width="16" height="16" rx="3" fill="#cfd5dc"/>',45,'Carretel retrátil com esguicho regulável.')
add('esguicho','Esguicho regulável (pistola)','Expedições',(130,80),
 f'<rect x="4" y="30" width="36" height="16" rx="4" fill="{tf}"/><rect x="40" y="24" width="50" height="28" rx="6" fill="#3b424b"/>'
 f'<path d="M90 26 L120 18 V58 L90 50 Z" fill="#d32f2f"/><path d="M52 52 L48 74 H64 L66 52" fill="#2c333c"/><path d="M56 24 Q66 6 82 24" fill="none" stroke="#9aa4b0" stroke-width="5"/>',22,'Jato compacto ou neblina 30°/60°.')
add('dispersador','Dispersador','Expedições',(130,80),
 f'<rect x="4" y="20" width="64" height="18" fill="{tf}"/><rect x="66" y="14" width="22" height="30" rx="4" fill="#9aa4b0"/>'
 f'<path d="M88 22 L124 6 M88 29 L126 29 M88 36 L124 52" stroke="{a}" stroke-width="3" stroke-dasharray="4 4"/>',30,'Molha o chão à frente (57 L/min).')
add('inundador','Inundador de para-brisa','Expedições',(160,90),
 f'<path d="M14 82 L26 18 H134 L146 82 Z" fill="#cde3f2" stroke="{m}" stroke-width="3"/><rect x="22" y="8" width="116" height="10" rx="4" fill="#9aa4b0"/>'
 + ''.join(f'<path d="M{34+i*22} 18 v{30+((i%2)*14)}" stroke="{a}" stroke-width="3" stroke-dasharray="3 5"/>' for i in range(5))+
 f'<path d="M50 80 L70 40" stroke="{K}" stroke-width="4"/><path d="M110 80 L128 44" stroke="{K}" stroke-width="4"/>',130,'Barra de bicos e limpadores.')
# ---------------- succao e abastecimento ----------------
add('mangote_ralo','Mangote 4" com ralo','Sucção e abastecimento',(110,150),
 f'<path d="M20 10 C20 60 80 60 80 110" fill="none" stroke="#3b424b" stroke-width="16"/><path d="M20 10 C20 60 80 60 80 110" fill="none" stroke="#6b737c" stroke-width="2" stroke-dasharray="3 5"/>'
 f'<rect x="62" y="108" width="36" height="34" rx="6" fill="#cfd5dc" stroke="{m}" stroke-width="3"/>'+''.join(f'<circle cx="{70+(i%3)*10}" cy="{118+(i//3)*10}" r="2.5" fill="{K}" stroke="none"/>' for i in range(9))+
 f'<rect x="10" y="2" width="20" height="10" fill="#9aa4b0"/>',35,'Sucção de manancial; o ralo tem retenção.')
add('admissao','Admissão do tanque (storz)','Sucção e abastecimento',(110,80),
 f'<rect x="4" y="30" width="60" height="22" fill="{tf}"/><rect x="62" y="20" width="22" height="42" rx="4" fill="#c9cfd6" stroke="{m}" stroke-width="3"/>'
 f'<path d="M84 26 h14 v10 h8 v10 h-8 v10 h-14 Z" fill="#b8bfc7"/><rect x="24" y="8" width="6" height="22" fill="#9aa4b0"/><rect x="24" y="4" width="32" height="9" rx="4" fill="#d32f2f"/>',30,'Abastece por hidrante ou esvazia por gravidade.')
add('hidrante','Hidrante de coluna','Sucção e abastecimento',(80,140),
 f'<rect x="18" y="30" width="44" height="100" rx="10" fill="#d32f2f"/><rect x="10" y="20" width="60" height="14" rx="6" fill="#b71c1c"/><rect x="34" y="6" width="12" height="14" fill="#9aa4b0"/>'
 f'<circle cx="16" cy="70" r="9" fill="#cfd5dc"/><circle cx="64" cy="70" r="9" fill="#cfd5dc"/><rect x="8" y="128" width="64" height="8" fill="#9aa4b0"/>',40,'Rede pública com pressão.')
add('manancial','Manancial (poço / represa)','Sucção e abastecimento',(200,110),
 f'<path d="M4 30 H196 V96 Q196 104 188 104 H12 Q4 104 4 96 Z" fill="#8a6a43"/><path d="M14 40 H186 V92 H14 Z" fill="#5aa2e0" stroke="none"/>'
 f'<path d="M20 48 q12 -6 24 0 t24 0 t24 0 t24 0 t24 0 t24 0" fill="none" stroke="#fff" stroke-width="2"/>',200,'Fonte de água abaixo do caminhão.')
# ---------------- tubulacao ----------------
add('tubo_reto','Tubo reto','Tubulação',(200,40),f'<rect x="4" y="10" width="192" height="20" rx="3" fill="{tf}" stroke="{t}" stroke-width="2"/>',100,'Trecho reto (estique e gire).')
add('tubo_curva','Curva 90°','Tubulação',(100,100),f'<path d="M10 40 H40 Q60 40 60 60 V90 H80 V60 Q80 20 40 20 H10 Z" fill="{tf}" stroke="{t}" stroke-width="2"/>',40,'Curva de 90 graus.')
add('tubo_te','Tê','Tubulação',(120,90),f'<path d="M6 30 H114 V50 H70 V84 H50 V50 H6 Z" fill="{tf}" stroke="{t}" stroke-width="2"/>',45,'Derivação em T.')
add('tubo_reducao','Redução','Tubulação',(120,60),f'<path d="M6 10 H50 L80 20 H114 V40 H80 L50 50 H6 Z" fill="{tf}" stroke="{t}" stroke-width="2"/>',40,'Muda o diâmetro.')
add('fio_eletrico','Fio elétrico','Tubulação',(160,60),f'<path d="M10 40 C50 0 110 60 150 20" fill="none" stroke="{e}" stroke-width="5"/><circle cx="10" cy="40" r="5" fill="{K}"/><circle cx="150" cy="20" r="5" fill="{K}"/>',60,'Liga painel e bobinas.')
# ---------------- fundos ----------------
fundo_l=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 460" width="960" height="460"><title>Caminhão CCI 4x4 - vista lateral (1 m = 100 px)</title>
<g fill="none" stroke="#7d8896" stroke-width="3" stroke-linejoin="round">
<path d="M30 330 V170 Q30 120 80 112 L190 100 Q225 98 232 130 L246 210 V330 Z" fill="#eef2f6"/>
<path d="M60 128 L182 116 Q204 116 208 140 L218 196 H60 Z" fill="#dce7f1"/>
<rect x="250" y="60" width="680" height="270" rx="10" fill="#f5f7f9"/>
<path d="M250 330 H930" stroke-width="5"/><rect x="20" y="330" width="920" height="22" rx="6" fill="#d9dee4"/>
<g fill="#3a4048" stroke="#252a30"><circle cx="160" cy="372" r="52"/><circle cx="610" cy="372" r="52"/></g>
<g fill="#aab3bd" stroke="none"><circle cx="160" cy="372" r="20"/><circle cx="610" cy="372" r="20"/></g>
<path d="M290 60 V330 M890 60 V330" stroke-dasharray="8 8" stroke-width="2"/>
</g><g font-family="Arial" font-size="16" fill="#7d8896"><text x="120" y="450">8,95 m · entre-eixos 4,50 m · altura 4,02 m</text></g></svg>
'''
fundo_s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 300" width="960" height="300"><title>Caminhão CCI 4x4 - vista superior (1 m = 100 px)</title>
<g fill="none" stroke="#7d8896" stroke-width="3" stroke-linejoin="round">
<rect x="30" y="25" width="215" height="250" rx="30" fill="#eef2f6"/><rect x="250" y="25" width="680" height="250" rx="10" fill="#f5f7f9"/>
<g fill="#3a4048" stroke="#252a30"><rect x="108" y="6" width="104" height="22" rx="6"/><rect x="108" y="272" width="104" height="22" rx="6"/><rect x="558" y="6" width="104" height="22" rx="6"/><rect x="558" y="272" width="104" height="22" rx="6"/></g>
<path d="M250 150 H930" stroke-dasharray="8 8" stroke-width="2"/></g></svg>
'''
open(f'{OUT}/fundo_caminhao_lateral.svg','w').write(fundo_l); open(f'{OUT}/fundo_caminhao_superior.svg','w').write(fundo_s)
cat={'escala':'1 m = 100 px nos fundos; "largura" = largura sugerida do item em px nessa escala',
     'fundos':[{'id':'lateral','nome':'Caminhão – vista lateral','arquivo':'assets/2d/fundo_caminhao_lateral.svg','largura':960,'altura':460},
               {'id':'superior','nome':'Caminhão – vista superior','arquivo':'assets/2d/fundo_caminhao_superior.svg','largura':960,'altura':300}],
     'itens':I}
json.dump(cat,open(f'{OUT}/catalogo.json','w'),ensure_ascii=False,indent=1)
print(len(I),'itens')
