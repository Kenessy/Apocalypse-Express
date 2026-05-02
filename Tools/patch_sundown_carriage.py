from pathlib import Path

MARK = 'SUNDOWN_SALOON_V2'
path = Path('docs/character-creation.html')
html = path.read_text(encoding='utf-8')
if MARK in html:
    print('Sundown Saloon already integrated')
    raise SystemExit(0)

css = r'''

/* SUNDOWN_SALOON_V2 - integrated carriage map */
.sundown-section{background:linear-gradient(180deg,rgba(14,12,24,.88),rgba(14,12,24,.94));border:.5px solid rgba(201,156,90,.30);border-radius:var(--r-card);box-shadow:inset 0 0 0 .5px rgba(201,156,90,.12),0 8px 28px rgba(0,0,0,.45);padding:28px 32px}.sundown-floor{position:relative;margin-top:22px;padding:42px 34px 52px;border-radius:var(--r-card);border:.5px solid rgba(201,156,90,.24);background:radial-gradient(800px 240px at 50% 0,rgba(201,156,90,.08),transparent 70%),linear-gradient(180deg,#0A0812,#05040A)}.sundown-map{position:relative;margin:auto;width:min(1120px,100%);aspect-ratio:12/4;border-radius:24px;overflow:hidden;border:2px solid var(--gold);background:linear-gradient(90deg,#090712,#16111f,#090712);box-shadow:inset 0 0 0 2px #000,inset 0 0 70px rgba(76,43,112,.55),0 18px 50px #000}.sundown-grid{position:absolute;inset:0;display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(4,1fr);z-index:1}.sundown-cell{border:1px solid rgba(230,207,161,.15);position:relative}.sundown-cell span{position:absolute;top:6px;left:7px;font:10px/1 monospace;color:rgba(230,207,161,.30)}.sundown-label{position:absolute;top:14px;font-size:var(--fs-caption);color:var(--muted);letter-spacing:.12em;text-transform:uppercase}.sundown-label.front{left:34px}.sundown-label.rear{right:34px}.sundown-wall{position:absolute;left:1%;right:1%;height:10px;border-radius:14px;z-index:10;background:linear-gradient(90deg,#1b1023,#08050d,#1b1023);border:1px solid rgba(230,207,161,.45);box-shadow:0 0 20px #000}.sundown-wall.top{top:1.5%}.sundown-wall.bottom{bottom:1.5%}.sundown-door{position:absolute;z-index:11;bottom:5%;width:42px;height:18%;background:#05040A;border:1px solid rgba(230,207,161,.72)}.sundown-door.left{left:-3px;border-radius:0 12px 12px 0}.sundown-door.right{right:-3px;border-radius:12px 0 0 12px}.sundown-passage{position:absolute;left:0;right:0;bottom:0;height:25%;z-index:3;background:linear-gradient(90deg,rgba(5,4,10,.9),rgba(27,31,43,.88),rgba(5,4,10,.9));border-top:2px solid rgba(230,207,161,.72);box-shadow:inset 0 0 28px rgba(40,189,216,.06),0 -12px 24px rgba(0,0,0,.48)}.sundown-passage:after{content:'PASSAGE - THROUGH ROUTE BETWEEN CARRIAGES';position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:var(--fs-ambient);letter-spacing:.12em;color:#d9c8ef;white-space:nowrap}.sundown-barback{position:absolute;left:5%;right:5%;top:5%;height:12%;z-index:5;border-radius:12px;background:linear-gradient(90deg,rgba(40,189,216,.13),rgba(230,207,161,.25),rgba(76,43,112,.28));border:1px solid rgba(230,207,161,.48)}.sundown-barback:after{content:'MIRROR BOTTLE WALL';position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:var(--fs-ambient);color:#d7c7e8;letter-spacing:.08em}.sundown-counter{position:absolute;left:7%;right:7%;top:19%;height:13%;z-index:6;border-radius:12px;background:linear-gradient(180deg,rgba(230,207,161,.33),rgba(76,43,112,.54));border:2px solid rgba(230,207,161,.82);box-shadow:inset 0 0 24px rgba(0,0,0,.72),0 0 18px rgba(201,156,90,.16)}.sundown-counter:before{content:'LUCIFER WALL BAR';position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:var(--fs-caption);font-weight:900;color:#f5ead2;letter-spacing:.12em;white-space:nowrap}.sundown-a1{position:absolute;left:9.5%;top:35%;width:7%;height:17%;z-index:9;clip-path:polygon(25% 0,75% 0,100% 50%,75% 100%,25% 100%,0 50%);background:linear-gradient(180deg,var(--gold2),var(--gold));display:grid;place-items:center;color:#05040A;font-size:var(--fs-caption);font-weight:950;text-align:center}.sundown-saloon{position:absolute;left:4%;right:4%;top:34%;height:38%;z-index:4;border:1px dashed rgba(230,207,161,.24);border-radius:16px;background:radial-gradient(ellipse at 45% 45%,rgba(201,156,90,.12),transparent 60%),linear-gradient(90deg,rgba(76,43,112,.20),rgba(11,14,22,.38))}.sundown-saloon:after{content:'OPEN MIRRORED DRINKING SALOON';position:absolute;left:36%;top:8px;transform:translateX(-50%);font-size:var(--fs-ambient);font-weight:900;color:var(--gold2);letter-spacing:.1em;white-space:nowrap}.sundown-stool{position:absolute;z-index:7;width:22px;height:22px;border-radius:50%;background:radial-gradient(circle,#6b3a2d,#120b12 65%);border:1px solid rgba(230,207,161,.5)}.sundown-stool.s1{left:20%;top:35%}.sundown-stool.s2{left:30%;top:35%}.sundown-stool.s3{left:40%;top:35%}.sundown-stool.s4{left:50%;top:35%}.sundown-stool.s5{left:60%;top:35%}.sundown-booth{position:absolute;z-index:5;border-radius:12px;background:linear-gradient(180deg,rgba(76,43,112,.48),rgba(11,14,22,.88));border:1px solid rgba(230,207,161,.36);display:grid;place-items:center;color:#d8cbe8;font-size:var(--fs-ambient);font-weight:800;text-align:center}.sundown-booth.b1{left:19%;top:49%;width:14%;height:18%}.sundown-booth.b2{left:43%;top:49%;width:14%;height:18%}.sundown-table{position:absolute;z-index:6;width:30px;height:30px;border-radius:50%;background:radial-gradient(circle,#3a2130,#0a0710 70%);border:1px solid rgba(230,207,161,.45)}.sundown-table.ta{left:23%;top:54%}.sundown-table.tb{left:47%;top:54%}.sundown-alcove{position:absolute;right:5%;top:36%;width:22%;height:33%;z-index:8;border-radius:14px;background:linear-gradient(180deg,rgba(5,4,10,.82),rgba(27,31,43,.76));border:1px solid rgba(201,156,90,.55);box-shadow:inset 0 0 22px rgba(0,0,0,.72),0 0 22px rgba(201,156,90,.10);display:grid;grid-template-rows:auto 1fr;overflow:hidden}.sundown-alcove:before{content:'A/B SLOT';position:absolute;top:7px;right:8px;font:700 8px/1 'IBM Plex Mono';letter-spacing:.14em;color:var(--gold);opacity:.65}.sundown-alcove[data-mode=kitchen]{border-color:rgba(230,207,161,.70)}.sundown-alcove[data-mode=booth]{border-color:rgba(40,189,216,.55)}.sundown-alcove-head{padding:13px 14px 5px;font:700 var(--fs-caption)/1.15 Cinzel,serif;letter-spacing:.06em;color:var(--gold2);text-transform:uppercase}.sundown-alcove-body{display:flex;align-items:center;gap:10px;padding:5px 14px 13px;color:var(--muted);font:400 var(--fs-ambient)/1.45 'IBM Plex Mono'}.sundown-alcove-icon{font-size:26px}.sundown-note-line{position:absolute;left:8%;right:8%;top:70%;z-index:6;text-align:center;color:#c9bedc;font-size:var(--fs-ambient);letter-spacing:.08em}.sundown-axis{position:absolute;left:34px;right:34px;bottom:15px;display:grid;grid-template-columns:repeat(12,1fr);color:rgba(230,207,161,.55);font:11px monospace;text-align:center}.sundown-rowaxis{position:absolute;top:42px;bottom:52px;left:9px;display:grid;grid-template-rows:repeat(4,1fr);color:rgba(230,207,161,.55);font:11px monospace;align-items:center}.sundown-ab{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px}.sundown-card{border:.5px solid rgba(201,156,90,.22);border-radius:var(--r-card);background:rgba(7,7,10,.55);padding:18px;text-align:left;cursor:pointer;color:var(--text);font:inherit}.sundown-card:hover{border-color:rgba(230,207,161,.55)}.sundown-card.is-active{border-color:rgba(230,207,161,.80);box-shadow:inset 0 0 0 .5px rgba(230,207,161,.35),0 0 30px rgba(201,156,90,.12)}.sundown-tag{font:700 var(--fs-ambient)/1 'IBM Plex Mono';letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}.sundown-card h4{font:700 18px/1.1 Cinzel,serif;color:var(--gold2);letter-spacing:.06em;margin-bottom:8px}.sundown-card p{font:400 13px/1.65 'IBM Plex Mono';color:var(--muted)}.sundown-effect{margin-top:12px;padding-top:12px;border-top:.5px dashed rgba(201,156,90,.20);color:var(--text);opacity:.92}.sundown-rules{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:20px}.sundown-note{background:rgba(27,31,43,.70);border:.5px solid rgba(201,156,90,.22);border-radius:var(--r-card);padding:12px}.sundown-note b{display:block;color:var(--gold2);font:700 13px/1.2 'IBM Plex Mono';margin-bottom:6px}.sundown-note p{color:var(--muted);font:400 12px/1.45 'IBM Plex Mono'}@media(max-width:820px){.sundown-ab,.sundown-rules{grid-template-columns:1fr}.sundown-passage:after,.sundown-counter:before,.sundown-barback:after,.sundown-saloon:after{font-size:8px}.sundown-stool{width:16px;height:16px}.sundown-table{width:22px;height:22px}.sundown-booth{font-size:8px}.sundown-alcove-head{font-size:9px}.sundown-alcove-body{font-size:8px}.sundown-alcove-icon{font-size:18px}}
'''

section = r'''

<!-- SUNDOWN_SALOON_V2 -->
<section class="carriage-section sundown-section" data-carriage="sundown-saloon">
  <div class="cadence-section-header">
    <div class="bi-eyebrow cath-eyebrow">Carriage 2 · Sundown Saloon</div>
    <h3>Wall bar, open saloon, and one right-side A/B alcove</h3>
    <p>The Sundown Saloon is the Train's social reactor: rumors, favors, debt, hospitality, and trouble. Row 4 remains a clean passage between carriages.</p>
  </div>
  <div class="sundown-floor">
    <div class="sundown-label front">Front / Engine</div><div class="sundown-label rear">Rear / Next Car</div><div class="sundown-rowaxis"><span>1</span><span>2</span><span>3</span><span>4</span></div>
    <div class="sundown-map">
      <div class="sundown-grid" id="sundownGrid" aria-hidden="true"></div>
      <div class="sundown-wall top"></div><div class="sundown-wall bottom"></div><div class="sundown-barback"></div><div class="sundown-counter"></div><div class="sundown-a1">A1<br>HOST</div><div class="sundown-saloon"></div>
      <div class="sundown-stool s1"></div><div class="sundown-stool s2"></div><div class="sundown-stool s3"></div><div class="sundown-stool s4"></div><div class="sundown-stool s5"></div>
      <div class="sundown-booth b1">booth</div><div class="sundown-booth b2">mirror booth</div><div class="sundown-table ta"></div><div class="sundown-table tb"></div>
      <div class="sundown-alcove" id="sundownAlcove" data-mode="kitchen"><div class="sundown-alcove-head" id="sundownAlcoveTitle">Mini-Kitchen</div><div class="sundown-alcove-body"><span class="sundown-alcove-icon" id="sundownAlcoveIcon">♨</span><span id="sundownAlcoveText">Drinks, quick food, emergency team prep.</span></div></div>
      <div class="sundown-note-line">right-side 2x2 alcove slot - does not touch the passage row</div><div class="sundown-passage"></div><div class="sundown-door left"></div><div class="sundown-door right"></div>
    </div>
    <div class="sundown-axis"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span><span>12</span></div>
  </div>
  <div class="sundown-ab" role="group" aria-label="Sundown Saloon A/B alcove options">
    <button class="sundown-card is-active" type="button" data-sundown-mode="kitchen"><div class="sundown-tag">Option A · Utility</div><h4>Mini-Kitchen</h4><p>Small bar-kitchen for drinks, heat, quick meals, and emergency food prep.</p><p class="sundown-effect"><strong>Use when:</strong> the Saloon should support morale, fast hospitality, and backup team logistics.</p></button>
    <button class="sundown-card" type="button" data-sundown-mode="booth"><div class="sundown-tag">Option B · Social</div><h4>Private Booth / Deal Nook</h4><p>Separated VIP alcove for private bargains, faction meetings, blackmail, confessions, and crew drama.</p><p class="sundown-effect"><strong>Use when:</strong> the Saloon should generate favors, secrets, debt, and relationship pressure.</p></button>
  </div>
  <div class="sundown-rules"><div class="sundown-note"><b>A1 Host</b><p>Assignable staff tile. Without A1, structured Saloon actions are limited.</p></div><div class="sundown-note"><b>Wall Bar</b><p>The bar is a wall fixture, not a full backroom. Mirror bottle wall and counter stay flush to rows 1-2.</p></div><div class="sundown-note"><b>Open Saloon</b><p>Middle rows stay social and playable: stools, booths, tables, reputation pressure.</p></div><div class="sundown-note"><b>Passage Row</b><p>Row 4 remains a full through-route between carriages. No plugin can block it.</p></div></div>
</section>
'''

js = r'''

<script>
// SUNDOWN_SALOON_V2
(function(){
  const data={kitchen:{title:'Mini-Kitchen',icon:'♨',text:'Drinks, quick food, emergency team prep.'},booth:{title:'Private Booth',icon:'♟',text:'Private deals, faction meetings, secrets, debt.'}};
  function init(){
    const grid=document.getElementById('sundownGrid');
    if(grid && !grid.children.length){for(let r=1;r<=4;r++)for(let c=1;c<=12;c++){const d=document.createElement('div');d.className='sundown-cell';d.innerHTML='<span>'+c+'.'+r+'</span>';grid.appendChild(d)}}
    const alcove=document.getElementById('sundownAlcove'),title=document.getElementById('sundownAlcoveTitle'),icon=document.getElementById('sundownAlcoveIcon'),text=document.getElementById('sundownAlcoveText');
    const buttons=[...document.querySelectorAll('[data-sundown-mode]')];
    if(!alcove||!title||!icon||!text||!buttons.length)return;
    buttons.forEach(btn=>btn.addEventListener('click',()=>{const mode=btn.dataset.sundownMode,next=data[mode]||data.kitchen;buttons.forEach(b=>b.classList.toggle('is-active',b===btn));alcove.dataset.mode=mode;title.textContent=next.title;icon.textContent=next.icon;text.textContent=next.text;}));
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

style_anchor = html.find('/* FOOTER */')
if style_anchor == -1:
    style_anchor = html.find('</style>')
if style_anchor == -1:
    raise SystemExit('CSS insertion point not found')
html = html[:style_anchor] + css + '\n' + html[style_anchor:]

acq = html.find('acquisition-atlas')
if acq != -1:
    close = html.find('</section>', acq)
    if close == -1:
        raise SystemExit('acquisition-atlas closing section not found')
    html = html[:close + len('</section>')] + section + html[close + len('</section>'):]
else:
    vagon = html.find('id="tab-vagon"')
    if vagon == -1:
        vagon = html.find("id='tab-vagon'")
    if vagon == -1:
        raise SystemExit('Carriages panel not found')
    cadence = html.find('id="tab-cadence"', vagon)
    if cadence == -1:
        cadence = html.find("id='tab-cadence'", vagon)
    close = html.rfind('</section>', vagon, cadence if cadence != -1 else len(html))
    if close == -1:
        raise SystemExit('Carriages closing section not found')
    html = html[:close] + section + html[close:]

body = html.rfind('</body>')
if body == -1:
    raise SystemExit('body close not found')
html = html[:body] + js + html[body:]
path.write_text(html, encoding='utf-8')
print('Integrated Sundown Saloon into docs/character-creation.html')
