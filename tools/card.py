import segno, io, sys, re
out=sys.argv[1]
qr=segno.make('https://threeforksaccommodations.com', error='q')
buf=io.BytesIO(); qr.save(buf, kind='svg', scale=10, border=2, dark='#2a211c', light='#ffffff', xmldecl=False, svgns=True, nl=False, omitsize=True)
svg=buf.getvalue().decode()
open(out+'/qr-threeforksaccommodations.svg','w').write(svg)
html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Three Forks Accommodations welcome card</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  @page {{ size: 5in 7in; margin: 0; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; }}
  body {{ background: #d9d2c6; font-family: "Inter", "Helvetica Neue", Arial, sans-serif; color: #2a211c; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .card {{ width: 5in; height: 7in; margin: 0 auto; background: #faf6ef; padding: 0.32in; display: flex; flex-direction: column; overflow: hidden; }}
  .photo {{ height: 2.25in; border-radius: 0.12in; overflow: hidden; flex: none; }}
  .photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 62%; display: block; }}
  .eyebrow {{ font-size: 7.5pt; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; color: #981e32; margin: 0.2in 0 0.07in; }}
  h1 {{ font-family: "Fraunces", Georgia, serif; font-weight: 600; font-size: 25pt; line-height: 1.05; letter-spacing: -0.01em; margin: 0 0 0.11in; text-wrap: balance; }}
  p {{ font-size: 9.6pt; line-height: 1.5; margin: 0 0 0.08in; }}
  .sign {{ font-family: "Fraunces", Georgia, serif; font-style: italic; font-size: 13pt; color: #981e32; margin: 0.02in 0 0; }}
  .more {{ margin-top: auto; display: flex; gap: 0.2in; align-items: center; border-top: 1px solid #e0d5c4; padding-top: 0.16in; }}
  .qr {{ width: 1.3in; height: 1.3in; flex: none; background: #fff; border-radius: 0.08in; overflow: hidden; }}
  .qr svg {{ width: 100%; height: 100%; display: block; }}
  .more h2 {{ font-family: "Fraunces", Georgia, serif; font-weight: 600; font-size: 14pt; line-height: 1.15; margin: 0 0 0.05in; }}
  .more p {{ font-size: 8.6pt; line-height: 1.45; color: #5d4f45; margin: 0 0 0.06in; }}
  .url {{ font-weight: 600; font-size: 9pt; color: #2a211c; }}
  .brand {{ font-family: "Fraunces", Georgia, serif; font-weight: 600; font-size: 9.5pt; margin-top: 0.14in; display: flex; justify-content: space-between; align-items: baseline; }}
  .brand i {{ font-weight: 400; color: #981e32; }}
  .brand span:last-child {{ font-family: "Fraunces", Georgia, serif; font-style: italic; font-weight: 400; color: #981e32; }}
  @media screen {{ body {{ padding: 24px 0; }} .card {{ box-shadow: 0 6px 24px rgba(0,0,0,.18); }} }}
</style>
</head>
<body>
<div class="card">
  <div class="photo"><img src="../images/monkeybread-1.jpg" alt="Fresh monkey bread on a wooden cake stand"></div>
  <p class="eyebrow">Welcome to Pullman</p>
  <h1>The monkey bread is for you.</h1>
  <p>We bake it for every guest, so pull it apart while it&rsquo;s warm. Make yourself at home, and message us on the Airbnb app if you need anything at all. We reply fast.</p>
  <p class="sign">Bruce &amp; Sue</p>
  <div class="more">
    <div class="qr">{svg}</div>
    <div>
      <h2>Coming back to Pullman?</h2>
      <p>We host six places around town, from a farm with mini Highland cows to a karaoke suite. Scan to see them all, or bring a bigger group next time.</p>
      <div class="url">threeforksaccommodations.com</div>
    </div>
  </div>
  <div class="brand"><span>Three Forks <i>Accommodations</i></span><span>Go Cougs!</span></div>
</div>
</body>
</html>
'''
open(out+'/welcome-card.html','w',encoding='utf-8').write(html)
