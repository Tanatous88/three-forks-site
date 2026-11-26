import sys
out=sys.argv[1]
CSS='''
  /* Full-page (US Letter) version */
  @page { size: 8.5in 11in; margin: 0; }
  .card { width: 8.5in; height: 11in; padding: 0.6in 0.7in 0.55in; }
  .photo { height: 3.75in; border-radius: 0.16in; }
  .eyebrow { font-size: 11.5pt; margin: 0.3in 0 0.09in; }
  h1 { font-size: 38pt; margin: 0 0 0.16in; }
  p { font-size: 14.5pt; line-height: 1.5; margin: 0 0 0.13in; }
  .sign { font-size: 21pt; margin-top: 0.06in; }
  .more { gap: 0.34in; padding-top: 0.24in; }
  .qr { width: 1.75in; height: 1.75in; border-radius: 0.12in; }
  .more h2 { font-size: 22pt; margin: 0 0 0.08in; }
  .more p { font-size: 13pt; margin: 0 0 0.1in; }
  .url { font-size: 13.5pt; }
  .brand { font-size: 13.5pt; margin-top: 0.22in; }
'''
for s in ['garage','bunkhouse','studio','midnight-nook','cosmopolitan','cottage','all']:
    src=f'{out}/welcome-card-{s}.html' if s!='all' else f'{out}/welcome-cards-all.html'
    h=open(src,encoding='utf-8').read()
    assert '</style>' in h
    h=h.replace('</style>',CSS+'</style>',1).replace('Welcome card','Welcome page').replace('Welcome cards','Welcome pages')
    dst=f'{out}/welcome-page-{s}.html' if s!='all' else f'{out}/welcome-pages-all.html'
    open(dst,'w',encoding='utf-8').write(h)
