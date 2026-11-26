import sys, re, html
out=sys.argv[1]
base=open(out+'/welcome-card.html',encoding='utf-8').read()
UNITS=[
 ('garage','The Garage',
  'The mini Highland cows, pigs and fainting goats next door love visitors, and there are treats for feeding them.',
  'Bringing more people?','The Bunkhouse, right next door, sleeps four more. Scan to see it and our four other places around Pullman.'),
 ('bunkhouse','The Bunkhouse',
  'The mini Highland cows, pigs and fainting goats in the stables love visitors. Catch the sunset from The Chair up in the back field.',
  'Bringing more people?','The Garage, right next door, sleeps four more. Scan to see it and our four other places around Pullman.'),
 ('studio','The Studio',
  'The karaoke room, the arcade machine and the 100-inch movie screen are all yours. Warm up your voice.',
  'Bringing a bigger group?','We have two more places just down the street, a three-minute walk away. Together with The Studio they sleep twelve. Scan to see all six of our stays.'),
 ('midnight-nook','The Midnight Nook',
  'The coffee and snack bar is stocked for you, and the fireplace is one switch away.',
  'Bringing more people?','The Cosmopolitan, right upstairs, sleeps four more. Scan to see it and our four other places around Pullman.'),
 ('cosmopolitan','The Cosmopolitan',
  'The kitchen is stocked and ready to cook in, and the fireplace is one switch away.',
  'Bringing more people?','The Midnight Nook, right downstairs, sleeps two more. Scan to see it and our four other places around Pullman.'),
 ('cottage','The Cottage',
  'The whole house is yours: the media lounge downstairs, the grill out back and the porch out front.',
  'Coming back to Pullman?','We host five other places around town, from a farm with mini Highland cows to a karaoke suite. Scan to see them all.'),
]
old_body=re.search(r'<p>We bake it.*?</p>',base,re.S).group(0)
old_h2=re.search(r'<h2>.*?</h2>\s*<p>.*?</p>',base,re.S).group(0)
names=[]
for slug,name,tip,h2,cross in UNITS:
    h=base.replace('Welcome to Pullman','Welcome to '+html.escape(name))
    h=h.replace(old_body,f'<p>We bake it for every guest, so pull it apart while it&rsquo;s warm.</p>\n  <p>{html.escape(tip)}</p>\n  <p>Need anything at all? Message us on the Airbnb app. We reply fast.</p>')
    h=h.replace(old_h2,f'<h2>{html.escape(h2)}</h2>\n      <p>{html.escape(cross)}</p>')
    h=h.replace('<title>Three Forks Accommodations welcome card</title>',f'<title>Welcome card: {html.escape(name)}</title>')
    h=h.replace('.photo {{ height: 2.25in','.photo {{ height: 2.25in').replace('.photo { height: 2.25in','.photo { height: 1.9in')
    IMG={'garage':('garage-1','The Garage living area'),'bunkhouse':('bunkhouse-1','The Bunkhouse living room'),'studio':('studio-1','The Studio living room'),'midnight-nook':('nook-1','The Midnight Nook lounge'),'cosmopolitan':('cosmo-1','The Cosmopolitan living room'),'cottage':('cottage-1','The Cottage exterior')}[slug]
    assert 'monkeybread-1.jpg' in h
    h=h.replace('../images/monkeybread-1.jpg','../images/'+IMG[0]+'.jpg').replace('Fresh monkey bread on a wooden cake stand',IMG[1]).replace('object-position: 50% 62%','object-position: 50% 50%')
    assert name in h and tip.split()[1] in h and cross[:12] in h
    open(f'{out}/welcome-card-{slug}.html','w',encoding='utf-8').write(h); names.append(slug)
# combined print file: all six cards, one per page
cards=[re.search(r'<div class="card">.*</div>\s*</body>',open(f'{out}/welcome-card-{s}.html',encoding='utf-8').read(),re.S).group(0).replace('</body>','') for s in names]
head=re.search(r'.*<body>',open(f'{out}/welcome-card-{names[0]}.html',encoding='utf-8').read(),re.S).group(0).replace('.card {','.card { break-after: page;').replace(f'Welcome card: The Garage','Welcome cards: all six units')
open(f'{out}/welcome-cards-all.html','w',encoding='utf-8').write(head+'\n'+'\n'.join(cards)+'\n</body>\n</html>\n')
print(' '.join(names))
