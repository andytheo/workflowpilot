"""Render original, branded PNG cards for every content pack. Requires Pillow."""
from pathlib import Path
import csv, re, textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def font(size,bold=False):
    for path in ([BOLD,FONT] if bold else [FONT,BOLD]):
        try: return ImageFont.truetype(path,size)
        except OSError: pass
    return ImageFont.load_default()
def wrap(draw,text,f,max_width):
    words=text.split(); lines=[]; current=""
    for word in words:
        test=(current+" "+word).strip()
        if draw.textbbox((0,0),test,font=f)[2]>max_width and current:
            lines.append(current);current=word
        else:current=test
    if current:lines.append(current)
    return lines
def render(path,title,subtitle,label,size):
    w,h=size
    img=Image.new("RGB",size,(13,28,49));d=ImageDraw.Draw(img)
    accent=(63,150,246); margin=int(w*.075)
    d.rounded_rectangle((margin,int(h*.10),w-margin,int(h*.105)+9),radius=4,fill=accent)
    d.text((margin,int(h*.14)),"WORKFLOWPILOT  /  "+label,font=font(max(20,int(w*.027)),True),fill=(148,194,255))
    title_font=font(int(w*.067),True)
    lines=wrap(d,title,title_font,w-2*margin)
    line_h=int(w*.087); y=int(h*.27)
    for line in lines[:7]:
        d.text((margin,y),line,font=title_font,fill="white");y+=line_h
    y=max(y+int(h*.05),int(h*.62))
    d.rounded_rectangle((margin,y,w-margin,min(h-margin,y+int(h*.20))),radius=20,fill=(27,54,86))
    f=font(int(w*.036))
    for line in wrap(d,subtitle,f,w-2*margin-55)[:4]:
        y+=int(w*.055);d.text((margin+25,y),line,font=f,fill=(226,238,255))
    d.text((margin,h-int(h*.075)),"Practical automation. No hype.",font=font(int(w*.026)),fill=(162,185,210))
    path.parent.mkdir(parents=True,exist_ok=True)
    img.save(path,optimize=True)

with (ROOT/"content/calendar.csv").open(encoding="utf-8",newline="") as fp: rows=list(csv.DictReader(fp))
for row in rows:
    slug=re.sub(r"[^a-z0-9]+","-",row["topic"].lower()).strip("-")
    out=ROOT/"production"/f'{int(row["id"]):02d}-{slug}'/"assets"
    title=row["topic"]
    for name,heading,subtitle in [
        ("01-hook.png",title,"A clear question to stop the scroll"),
        ("02-explain.png","Make the process simpler","Show a real example or verified screen recording here"),
        ("03-cta.png","Get the full guide","workflowpilot / guides  •  Link in bio")]:
        render(out/name,heading,subtitle,"SHORT  /  9:16",(1080,1920))
    render(out/"cover.png",title,"Free practical guide","COVER  /  9:16",(1080,1920))
    render(out/"blog-feature.png",title,"Practical tutorials for creators and small businesses","BLOG  /  1200x630",(1200,630))
print(f"Generated {len(rows)*5} PNG assets across {len(rows)} content packs")
