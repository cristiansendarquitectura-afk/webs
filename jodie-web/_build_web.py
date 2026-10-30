# Genera la PÁGINA WEB de Patagonia Glow a partir de la APP (../jodie/index.html).
# La app no se toca. Cuando cambie algo en la app, se vuelve a correr:  python _build_web.py
import os, shutil
AQUI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(AQUI, '..', 'jodie')
s = open(os.path.join(APP, 'index.html'), encoding='utf-8').read()
shutil.copy(os.path.join(APP, 'logo-montana.png'), AQUI)
if os.path.isdir(os.path.join(AQUI, 'img')): shutil.rmtree(os.path.join(AQUI, 'img'))
shutil.copytree(os.path.join(APP, 'img'), os.path.join(AQUI, 'img'))

CSS = r"""
/* ===== PÁGINA WEB (30-oct) — generada desde la app por _build_web.py =====
   Menú arriba, cada pantalla de la app es una página con su ruta (#/agenda, #/tratamientos…),
   fichas en ventana central. Mismos datos y funciones que la app. */
@media all{
  body{display:block;min-height:100vh;background-attachment:fixed}
  .web{display:block;position:sticky;top:0;z-index:70;background:rgba(240,219,215,.86);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid rgba(240,217,216,.95)}
  .phone{position:relative;max-width:none!important;width:100%;height:auto!important;background:transparent;border-radius:0!important;box-shadow:none!important;overflow:visible}
  .notch,.status,.nav,.grab{display:none!important}
  .screen{position:static!important;inset:auto;opacity:1!important;height:auto!important}
  .screen.on{display:block!important}
  .scroll{flex:none!important;height:auto!important}
  .screen.on{display:block}
  #splash,#home{display:none!important}
  .head{max-width:1120px;margin:0 auto;padding:40px 40px 6px;text-align:left}
  .head .back{position:static!important;font-size:14px;font-family:'Poppins',sans-serif;color:var(--muted);margin-bottom:10px;display:block}
  .head .back::after{content:' Volver'}
  .head h3{font-size:34px;letter-spacing:0;text-transform:none;font-weight:500}
  .scroll{overflow:visible;max-width:1120px;margin:0 auto;padding:14px 40px 72px!important}
  #agenda .scroll,#evalprev .scroll,#privacidad .scroll,#faq .scroll,#test .scroll,#giftcards .scroll,#perfil .scroll,#mejorar .scroll{max-width:820px}
  #agenda .head,#evalprev .head,#privacidad .head,#faq .head,#test .head,#giftcards .head,#perfil .head,#mejorar .head{max-width:820px}
  #catList,#favList,#histList{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
  #catList>*,#favList>*,#histList>*{margin:0!important}
  .sheet-bg{position:fixed}
  .sheet{position:fixed;left:50%;top:50%;right:auto;bottom:auto;width:min(760px,92vw);max-height:88vh;border-radius:26px;
    transform:translate(-50%,-47%);opacity:0;pointer-events:none;transition:opacity .25s ease,transform .25s ease;padding:22px 36px 32px}
  .sheet.on{transform:translate(-50%,-50%);opacity:1;pointer-events:auto}
  .toast{position:fixed;left:auto;right:32px;bottom:32px;width:400px}
  .wafab{position:fixed;right:28px;bottom:28px}
  .w-home{display:none}
  body[data-r="home"] .w-home{display:block}
  .w-foot{display:flex}
  .subhello{text-align:left!important}
}
@media(max-width:999px){
  .w-in,.head{padding-left:20px!important;padding-right:20px!important}
  .scroll{padding-left:20px!important;padding-right:20px!important}
  .w-top{flex-wrap:wrap!important;gap:10px!important}
  .w-nav{order:3;width:100%;margin-left:0!important;overflow-x:auto;gap:18px!important;padding-bottom:4px;scrollbar-width:none}
  .w-nav::-webkit-scrollbar{display:none}
  .w-top .w-btn{margin-left:auto}
  .w-hero{grid-template-columns:1fr!important;padding:28px 0 20px!important;gap:28px!important}
  .w-hero h1{font-size:44px!important}
  .w-band{flex-direction:column!important;align-items:flex-start!important;padding:28px 24px!important}
  .head h3{font-size:28px}
  .sheet{width:94vw;padding:18px 20px 26px}
  .toast{right:16px;left:16px;width:auto;bottom:16px}
}
.w-in{max-width:1120px;margin:0 auto;padding:0 40px}
.w-top{display:flex;align-items:center;gap:18px;padding-top:14px;padding-bottom:14px}
.w-logo{display:flex;align-items:center;gap:12px;cursor:pointer}
.w-logo img{width:40px}
.w-logo b{font-family:'Playfair Display',serif;font-weight:500;letter-spacing:.18em;color:#A88452;font-size:15px;white-space:nowrap}
.w-nav{display:flex;gap:16px;margin-left:auto}
.w-nav a{color:var(--ink);text-decoration:none;font-size:13.5px;opacity:.78;white-space:nowrap;padding:6px 2px;border-bottom:2px solid transparent}
.w-nav a:hover{opacity:1;color:var(--rose-deep)}
.w-nav a.sel{opacity:1;color:var(--rose-deep);border-bottom-color:var(--rose)}
.w-btn{border:0;border-radius:30px;padding:12px 22px;font-family:'Poppins',sans-serif;font-size:14px;font-weight:500;cursor:pointer;white-space:nowrap;
  background:linear-gradient(135deg,var(--rose-mid),var(--rose-deep));color:#fff;box-shadow:var(--shadow-sm)}
.w-btn:hover{filter:brightness(1.05)}
.w-btn.alt{background:var(--white);color:var(--rose-deep);border:1px solid var(--line);box-shadow:none}
.w-hero{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center;padding:64px 0 40px}
.w-eyebrow{font-size:12px;letter-spacing:.22em;color:#A88452;margin-bottom:18px}
.w-hero h1{font-family:'Playfair Display',serif;font-weight:500;color:var(--rose-deep);font-size:clamp(46px,4.8vw,68px);line-height:1.05}
.w-hero h1 em{font-style:italic}
.w-hero p{font-size:17px;color:var(--muted);max-width:520px;margin:20px 0 30px;line-height:1.6}
.w-hero .ph{border-radius:28px;overflow:hidden;box-shadow:var(--shadow)}
.w-hero .ph img{width:100%;display:block}
.w-ctas{display:flex;gap:12px;flex-wrap:wrap}
.w-chips{display:flex;gap:10px;flex-wrap:wrap;margin-top:28px}
.w-chips span{background:rgba(255,255,255,.7);border:1px solid var(--line);border-radius:30px;padding:8px 14px;font-size:13px;color:#8E6A70}
.w-sec{padding:48px 0 8px}
.w-sec h2{font-family:'Playfair Display',serif;font-weight:500;color:var(--rose-deep);font-size:34px;margin-bottom:8px}
.w-sec .w-lead{color:var(--muted);font-size:15px;margin-bottom:24px;max-width:640px;line-height:1.6}
.w-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.w-card{background:var(--white);border:1px solid var(--line);border-radius:20px;padding:20px;display:flex;flex-direction:column;gap:8px;
  box-shadow:0 4px 14px rgba(165,76,92,.06);transition:transform .2s,box-shadow .2s}
.w-card:hover{transform:translateY(-2px);box-shadow:var(--shadow-sm)}
.w-card .e{font-size:26px;width:50px;height:50px;border-radius:50%;background:var(--rose-ghost);display:flex;align-items:center;justify-content:center}
.w-card h3{font-family:'Playfair Display',serif;font-weight:500;font-size:19px;color:var(--ink)}
.w-card small{color:var(--muted);font-size:12.5px}
.w-card p{font-size:13.5px;color:#7A5A60;line-height:1.55;flex:1}
.w-card .acts{display:flex;gap:8px;margin-top:6px}
.w-card .acts button{flex:1;padding:9px 10px;font-size:13px}
.w-fotos{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px}
.w-fotos img{width:100%;border-radius:14px;cursor:zoom-in;box-shadow:0 4px 14px rgba(181,114,111,.18);transition:transform .2s}
.w-fotos img:hover{transform:scale(1.02)}
.w-band{margin:56px 0 8px;background:linear-gradient(120deg,#F6DBD9,#F3C9CD);border-radius:26px;padding:36px 40px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.w-band h3{font-family:'Playfair Display',serif;font-weight:500;color:var(--rose-deep);font-size:26px}
.w-band p{color:#8E6A70;font-size:14.5px;margin-top:6px}
.w-foot{max-width:1120px;margin:0 auto;padding:28px 40px 40px;border-top:1px solid var(--line);justify-content:space-between;gap:20px;flex-wrap:wrap;font-size:13px;color:var(--muted)}
.w-foot a{color:var(--rose-deep);cursor:pointer}
"""

HEAD = """<div class="web" id="web"></div>
<div class="phone">"""

JS = r"""
/* ===== PÁGINA WEB: rutas + menú + portada (mismos datos y funciones de la app) ===== */
function esWeb(){ return true; }
const RUTAS={home:'inicio',catalogo:'tratamientos',agenda:'agenda',resultados:'resultados',cuidados:'cuidados',giftcards:'gift-cards',
  sobre:'nosotras',faq:'preguntas',perfil:'mi-perfil',favoritos:'favoritos',historial:'historial',resenas:'resenas',
  mejorar:'lo-que-buscas',evalprev:'evaluacion-previa',privacidad:'privacidad',test:'test'};
const MENU=[['home','Inicio'],['catalogo','Tratamientos'],['resultados','Resultados'],['cuidados','Cuidados'],['giftcards','Gift Cards'],['sobre','Nosotras'],['faq','Preguntas'],['perfil','Mi perfil']];
function slug(t){ return t.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''); }
var _go=go, _open=openDetail, _close=closeDetail, rutaActual='home';
go=function(id){
  _go(id); rutaActual=id; document.body.dataset.r=id;
  if(id!=='splash' && RUTAS[id]){ var h='#/'+RUTAS[id]; if(location.hash!==h) history.pushState(null,'',h); }
  document.querySelectorAll('.w-nav a').forEach(function(a){ a.classList.toggle('sel',a.dataset.s===id); });
  if(esWeb()) window.scrollTo(0,0);
};
openDetail=function(i){ _open(i); var h='#/tratamiento/'+slug(TREATMENTS[i].n); if(location.hash!==h) history.pushState(null,'',h); };
closeDetail=function(){ _close(); var h='#/'+(RUTAS[rutaActual]||'inicio'); if(location.hash!==h) history.replaceState(null,'',h); };
window.go=go; window.openDetail=openDetail; window.closeDetail=closeDetail;
function aplicarRuta(){
  var r=location.hash.replace(/^#\/?/,'');
  if(r.indexOf('tratamiento/')===0){
    var i=TREATMENTS.findIndex(function(t){ return slug(t.n)===r.slice(12); });
    if(i>=0){ if(rutaActual!=='catalogo'){ go('catalogo'); } _open(i); history.replaceState(null,'','#/'+r); return; }
  }
  _close();
  var id=Object.keys(RUTAS).find(function(k){ return RUTAS[k]===r; });
  if(id) go(id); else if(esWeb()) go('home');
}
window.addEventListener('popstate',aplicarRuta);
(function renderWeb(){
  var w=document.getElementById('web'); if(!w) return;
  w.innerHTML='<div class="w-in w-top"><div class="w-logo" onclick="go(\'home\')"><img src="logo-montana.png" alt=""><b>PATAGONIA GLOW</b></div>'
   +'<nav class="w-nav">'+MENU.map(function(m){ return '<a href="#/'+RUTAS[m[0]]+'" data-s="'+m[0]+'" onclick="go(\''+m[0]+'\');return false">'+m[1]+'</a>'; }).join('')+'</nav>'
   +'<button class="w-btn" style="padding:10px 18px" onclick="go(\'agenda\')">Agendar</button></div>';
  var gal=TREATMENTS.filter(function(t){ return t.galeria; });
  var home=document.createElement('div'); home.className='w-home w-in';
  home.innerHTML='<section class="w-hero"><div><div class="w-eyebrow">ESTÉTICA · SALUD · BIENESTAR</div>'
   +'<h1>Tu piel,<br>tu bienestar,<br><em>tu glow.</em></h1>'
   +'<p>Tratamientos faciales y de bienestar con evaluación profesional personalizada, en Santiago y Punta Arenas.</p>'
   +'<div class="w-ctas"><button class="w-btn" onclick="go(\'agenda\')">Agendar una evaluación</button>'
   +'<button class="w-btn alt" onclick="openTest()">Descubrir mi cuidado ideal</button></div>'
   +'<div class="w-chips"><span>Jodie Berríos · Enfermera</span><span>Santiago · Punta Arenas</span><span>Evaluación personalizada</span></div></div>'
   +(gal.length?'<div class="ph"><img src="img/labios/labios-01.jpg" alt="Resultado real de aumento de labios"></div>':'')+'</section>'
   +'<section class="w-sec"><h2>Tratamientos</h2><div class="w-lead">Cada tratamiento se define en una evaluación profesional personalizada. Abre su ficha para ver en qué consiste, sus cuidados y contraindicaciones.</div><div class="w-grid">'
   +TREATMENTS.map(function(t,i){
      return '<div class="w-card"><div class="e">'+t.e+'</div><h3>'+t.n+'</h3><small>⏱ '+t.dur+(t.eval?' · requiere evaluación':'')+'</small>'
       +'<p>'+(t.d||t.resumen||'')+'</p><div class="acts"><button class="w-btn alt" onclick="openDetail('+i+')">Ver ficha</button><button class="w-btn" onclick="agendarDe('+i+')">Agendar</button></div></div>';
    }).join('')+'</div></section>'
   +gal.map(function(t){ return '<section class="w-sec"><h2>Resultados reales</h2><div class="w-lead">'+t.galeria.t+' con '+t.n.toLowerCase()+'. Pacientes reales de Patagonia Glow, publicadas con su autorización. Los resultados pueden variar entre personas.</div><div class="w-fotos">'+galFotos(t.galeria)+'</div></section>'; }).join('')
   +'<div class="w-band"><div><h3>¿No sabes qué tratamiento elegir?</h3><p>Responde unas preguntas y te orientamos. Siempre se confirma en tu evaluación.</p></div><button class="w-btn" onclick="openTest()">Hacer el test</button></div>';
  w.after(home);
  var f=document.createElement('footer'); f.className='w-foot';
  f.innerHTML='<span>© Patagonia Glow · Estética, salud y bienestar · Santiago · Punta Arenas</span>'
   +'<span><a onclick="go(\'privacidad\')">Privacidad</a> · <a onclick="go(\'faq\')">Preguntas</a> · <a onclick="waGeneral()">WhatsApp</a></span>';
  document.body.appendChild(f);
  if(location.hash) aplicarRuta(); else if(esWeb()) go('home');
})();
"""

a = '</style>'
k = s.rfind(a); assert k > 0; s = s[:k] + CSS + s[k:]   # al FINAL del estilo: así manda sobre las reglas de la app
assert s.count('<div class="phone">') == 1; s = s.replace('<div class="phone">', HEAD)
c = '\n</script>\n</body>'
assert s.count(c) == 1; s = s.replace(c, '\n' + JS + '</script>\n</body>')
s = s.replace('<title>Patagonia Glow · App</title>', '<title>Patagonia Glow · Estética, salud y bienestar</title>')
s = s.replace('<meta name="apple-mobile-web-app-title" content="Patagonia Glow">', '')
s = s.replace(', maximum-scale=1.0, user-scalable=no', '')
open(os.path.join(AQUI, 'index.html'), 'w', encoding='utf-8').write(s)
print('ok')
