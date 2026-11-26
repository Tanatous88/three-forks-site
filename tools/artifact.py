import re,sys,json,os
site=sys.argv[1]; out=sys.argv[2]
h=open(site+'/index.html',encoding='utf-8').read()
css=open(site+'/styles.css',encoding='utf-8').read()
js=open(site+'/site.js',encoding='utf-8').read()
body=re.search(r'<body>(.*)</body>',h,re.S).group(1).replace('<script src="site.js"></script>','')
extra='''
/* Artifact frame: safe-area gutters and sticky header offset */
.nav,.hero__inner,.stats,.stays,.animals,.groups,.reviews,.know{padding-left:max(clamp(16px,4vw,40px),env(safe-area-inset-left,0px));padding-right:max(clamp(16px,4vw,40px),env(safe-area-inset-right,0px))}
.bread__body,.footer{padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
.nav{top:env(safe-area-inset-top,0px)}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--paper)}
'''
page=f'''<title>Three Forks Accommodations</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;500;600&display=swap">
<style>
{css}{extra}</style>
{body}
<script>
{js}</script>
'''
open(out,'w',encoding='utf-8').write(page)
print(len(page), json.dumps({'images/'+f:'images/'+f for f in sorted(os.listdir(site+'/images')) if f.endswith('.jpg')}))
