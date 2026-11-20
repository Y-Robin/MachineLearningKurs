"""Erzeugt PDF, ausführbares Notebook und Overleaf-Quelle aus denselben Inhalten.

PDF-Build: gebündelte Python-Laufzeit mit reportlab und pdfplumber.
Rezepte vorher mit der Kursumgebung durch ml_pruefen.py ausführen.
"""
from pathlib import Path
import argparse, json, html, textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from ml_inhalte import PAGES, COMMON

parser = argparse.ArgumentParser()
parser.add_argument('--results', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()
out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
results = json.loads((Path(args.results)/'results.json').read_text(encoding='utf-8'))
versions = json.loads((Path(args.results)/'versions.json').read_text(encoding='utf-8'))
for name, file in [('Body','arial.ttf'),('Bold','arialbd.ttf'),('Code','consola.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/'+file))
W,H = A4; M = 40; WIDTH = W-2*M
ORANGE=HexColor('#ff5900'); DARK=HexColor('#091219'); GRAY=HexColor('#53606a')
c=canvas.Canvas(str(out/'Machine_Learning_CheatSheet.pdf'), pagesize=A4)
c.setTitle('Machine Learning CheatSheet | ROBNEXUS | Kursmethoden mit Python')
c.setAuthor('ROBNEXUS')
style=ParagraphStyle('body',fontName='Body',fontSize=9.1,leading=12,textColor=DARK)
small=ParagraphStyle('small',parent=style,fontSize=7.4,leading=9.4,textColor=GRAY)
bold=ParagraphStyle('head',parent=style,fontName='Bold',textColor=ORANGE,fontSize=9.5,leading=12)
inbox=ParagraphStyle('box',parent=style,textColor=white,fontSize=9,leading=12)
y=0; bounds=[]
def para(s, sty=style, x=M, width=WIDTH, gap=6):
    global y
    p=Paragraph(html.escape(s).replace('\n','<br/>'),sty)
    _,h=p.wrap(width,1000); p.drawOn(c,x,y-h); y-=h+gap
def label(s): para(s,bold,gap=3)
def block(code, output=False):
    global y
    lines=code.splitlines()
    if output:
        lines=[wrapped for line in lines for wrapped in
               (textwrap.wrap(line, width=103, break_long_words=True,
                              break_on_hyphens=False) or [''])]
    size=7.8 if output else 8.05
    leading=9.6 if output else 10.2
    for line in lines:
        assert pdfmetrics.stringWidth(line.expandtabs(4),'Code',size)<=WIDTH-20, (line,len(line))
    h=len(lines)*leading+16
    c.setFillColor(HexColor('#f2f4f6') if not output else HexColor('#fff1e8'))
    c.roundRect(M,y-h,WIDTH,h,5,fill=1,stroke=0)
    c.setFillColor(DARK);c.setFont('Code',size)
    for i,line in enumerate(lines): c.drawString(M+10,y-12-i*leading,line.expandtabs(4))
    y-=h+9
def table(rows):
    global y
    cells=[[Paragraph(html.escape(s), small) for s in row] for row in rows]
    t=Table(cells,colWidths=[WIDTH*.32,WIDTH*.68])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
        ('BACKGROUND',(0,0),(-1,0),HexColor('#fff1e8')),
        ('LINEBELOW',(0,0),(-1,-1),.3,HexColor('#dde2e6')),
        ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
        ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    _,h=t.wrap(WIDTH,1000);t.drawOn(c,M,y-h);y-=h+10
for n,p in enumerate(PAGES,1):
    original_id=p.get('original_id')
    c.bookmarkPage(f'p{n}');c.addOutlineEntry(p['title'],f'p{n}',level=0)
    c.setFillColor(ORANGE);c.setFont('Bold',9);c.drawRightString(W-M,H-27,'ROBNEXUS')
    c.setFillColor(ORANGE);c.setFont('Body',8);c.drawString(M,H-52,f'{n:02}  MACHINE LEARNING / KURSREFERENZ')
    y=H-66
    title=Paragraph(html.escape(p['title']),ParagraphStyle('title',fontName='Bold',fontSize=21,leading=24,textColor=DARK))
    _,h=title.wrap(WIDTH,100);title.drawOn(c,M,y-h);y-=h+15
    c.setStrokeColor(ORANGE);c.setLineWidth(2);c.line(M,y,M+45,y);y-=12
    para(p['intro'],gap=9)
    box=Paragraph('<b>MERKSATZ</b><br/>'+html.escape(p['principle']),inbox)
    _,bh=box.wrap(WIDTH-24,1000)
    c.setFillColor(DARK);c.roundRect(M,y-bh-18,WIDTH,bh+18,7,fill=1,stroke=0)
    box.drawOn(c,M+12,y-bh-9);y-=bh+29
    if p['code']:
        label('PYTHON / '+('Ausschnitt im Transfer-Notebook' if not p['run'] else 'Rezept'))
        block(p['code'])
    if p['table']:table(p['table'])
    r=results.get(str(n),{})
    if r.get('text'):
        # Keep printed results compact; full output remains in the notebook.
        text=r['text'].strip()
        if original_id==11:
            text='ROC-AUC / AP: '+text.split('ROC-AUC:')[-1].strip()
        if original_id==14:
            lines=text.splitlines(); text='\n'.join(textwrap.fill(s, width=100) for s in lines)
        if original_id==30:
            text=text.splitlines()[-1]
        lines=text.splitlines()
        if len(lines)>8: text='\n'.join(lines[:8])
        label('ERGEBNIS / ausgeführtes Rezept')
        block(text,output=True)
    # Full-size plots on the additional visual pages; compact plots on methods.
    if (p.get('visual') or original_id in [10,11,12,20,22,23,25,26,27]) and r.get('figures'):
        from PIL import Image
        path=r['figures'][0]
        iw,ih=Image.open(path).size
        height=p.get('figure_height', 114 if original_id in [10,11,23] else
                     (96 if original_id in [20,22] else 108))
        width=min(WIDTH,height*iw/ih);height=width*ih/iw
        c.drawImage(path,M+(WIDTH-width)/2,y-height,width,height,mask='auto')
        y-=height+8
    for title,body in p['notes']:
        label(title);para(body,gap=7)
    bounds.append((n,round(y,1)))
    assert y>60, f'Seite {n} zu voll: y={y}'
    c.setStrokeColor(HexColor('#dce1e5'));c.setLineWidth(.4);c.line(M,45,W-M,45)
    py=33
    source=Paragraph(html.escape(p['source']),small)
    _,sh=source.wrap(WIDTH-36,100)
    source.drawOn(c,M,py-sh+8)
    c.setFillColor(GRAY);c.setFont('Body',8);c.drawRightString(W-M,27,str(n))
    c.showPage()
c.save()

# Notebook: same recipes, real captured stdout and embedded figures.
cells=[]
def md(s): cells.append(dict(cell_type='markdown',metadata={},source=s.splitlines(keepends=True)))
def code(s, outputs=None, count=None):
    cells.append(dict(cell_type='code',metadata={},source=s.splitlines(keepends=True),
                      execution_count=count,outputs=outputs or []))
md('# Machine Learning CheatSheet\n\nRezepte passend zum Kurs. Kernel: Kursumgebung. Von oben nach unten ausführen.\n\n'
   +'Geprüfte Versionen: '+', '.join(f'{k} {v}' for k,v in versions.items())+'.\n'
   +'Der Transfer-Learning-Ausschnitt ist ausdrücklich nur im Originalnotebook ausführbar.')
code(COMMON, count=1)
count=1
import base64
for n,p in enumerate(PAGES,1):
    md(f'## {n:02} {p["title"]}\n\n{p["intro"]}\n\n**Merksatz:** {p["principle"]}\n\nKursbezug: {p["source"]}')
    if p['code']:
        if p['run']:
            count+=1; r=results.get(str(n),{});outputs=[]
            if r.get('text'):outputs.append(dict(output_type='stream',name='stdout',text=r['text'].splitlines(keepends=True)))
            for f in r.get('figures',[]):
                outputs.append(dict(output_type='display_data',metadata={},data={
                    'image/png':base64.b64encode(Path(f).read_bytes()).decode(),
                    'text/plain':['<Figure>']}))
            code(p['setup']+'\n'+p['code']+'\nplt.show()',outputs,count)
        else:md('Im Original-Transfer-Notebook ausführen:\n\n```python\n'+p['code']+'\n```')
    if p['table']:md('\n'.join(['| '+ ' | '.join(p['table'][0])+' |','| --- | --- |']+['| '+' | '.join(r)+' |' for r in p['table'][1:]]))
    for t,b in p['notes']:md('**'+t+'**\n\n'+b)
notebook=dict(cells=cells,metadata={'kernelspec':{'display_name':'Python 3 (Kursumgebung)','language':'python','name':'python3'},
    'language_info':{'name':'python','version':'3'}},nbformat=4,nbformat_minor=5)
for i,cell in enumerate(cells):cell['id']=f'ml-cheatsheet-{i:03}'
(out/'Machine_Learning_CheatSheet.ipynb').write_text(json.dumps(notebook,ensure_ascii=False,indent=1),encoding='utf-8')

# Editable Overleaf source (XeLaTeX). PDF and notebook are the final artifacts.
def esc(s):
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_',
                    '{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(ch,ch) for ch in s)
tex=[r'''\documentclass[10pt,a4paper]{article}
\usepackage[margin=16mm]{geometry}
\usepackage{fontspec}
\setmainfont{TeX Gyre Heros}
\setmonofont{Latin Modern Mono}
\usepackage[ngerman]{babel}
\usepackage{xcolor,tcolorbox,fancyvrb,hyperref}
\definecolor{accent}{HTML}{FF5900}
\definecolor{dark}{HTML}{091219}
\hypersetup{colorlinks=true,urlcolor=accent,linkcolor=accent}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\begin{document}''']
for n,p in enumerate(PAGES,1):
    if n>1:tex.append(r'\clearpage')
    tex.extend([r'\hfill\textcolor{accent}{ROBNEXUS}',r'\par\textcolor{accent}{'+f'{n:02} MACHINE LEARNING / KURSREFERENZ'+r'}',
                r'\section*{'+esc(p['title'])+'}',esc(p['intro']),
                r'\begin{tcolorbox}[colback=dark,coltext=white,colframe=dark,title=MERKSATZ]',esc(p['principle']),r'\end{tcolorbox}'])
    if p['code']:tex += [r'\begin{Verbatim}[fontsize=\scriptsize,frame=single]',p['code'],r'\end{Verbatim}']
    if p['table']:
        tex += [r'\begin{tabular}{p{.29\linewidth}p{.65\linewidth}}']
        tex += [esc(a)+' & '+esc(b)+r'\\' for a,b in p['table']]
        tex += [r'\end{tabular}']
    for t,b in p['notes']:tex += [r'\textcolor{accent}{\textbf{'+esc(t)+r'}}\par '+esc(b)]
    tex += [r'\vfill{\footnotesize '+esc(p['source'])+'}']
tex += [r'\end{document}']
(out/'Machine_Learning_CheatSheet.tex').write_text('\n'.join(tex),encoding='utf-8')
(out/'layout_check.json').write_text(json.dumps(bounds),encoding='utf-8')
print('Erstellt:', out, '\nSeiten:',len(PAGES),'\nUnterste Inhaltspunkte:', bounds)
